#!/usr/bin/env python3
"""单章自检：python3 lint_v3.py <章节.md> [--book general|dental]
检查图的写法（五种围栏）、@include 是否指向通用版已有的图、[[通用版 …]] 是否能解析、表格列数、字数。
没有问题输出 OK；有问题逐条列出，改完再跑，直到 OK。"""
import sys, os, re, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('b3', os.path.join(HERE, 'build_v3.py'))
b3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b3)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__); sys.exit(2)
    path = os.path.abspath(args[0])
    book = 'dental' if '/dental/' in path else 'general'
    if '--book' in sys.argv:
        book = sys.argv[sys.argv.index('--book') + 1]
    md = open(path).read()
    where = os.path.basename(path)
    probs = []

    # 通用版全部已写好的图，供 include 核对
    gdir = os.path.join(b3.V3, 'general')
    if os.path.isdir(gdir):
        for f in sorted(os.listdir(gdir)):
            if f.endswith('.md'):
                b3.collect_figs(open(os.path.join(gdir, f)).read(), 'general/' + f)
    if book == 'general':
        b3.collect_figs(md, 'general/' + where)
    else:
        for m in re.finditer(r'^\s*@include\s+([\w\-]+)\s*$', md, flags=re.M):
            if m.group(1) not in b3.FIGS:
                probs.append('@include %s：通用版里目前还没有 id=%s 的图（通用版写手可能还没写完；确认 id 拼写与 PAGE_TYPE_IDS.md 一致）' % (m.group(1), m.group(1)))
        md = b3.expand_includes(md, where)

    # 围栏配对
    fences = [i for i, l in enumerate(md.split('\n'), 1) if l.lstrip().startswith('```')]
    if len(fences) % 2:
        probs.append('代码围栏 ``` 数量是奇数（有一个没关），行号：%s' % fences[-6:])

    # 表格列数
    lines = md.split('\n')
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|[\s:\-|]+\|\s*$', lines[i + 1]):
            n = len(b3.split_row(lines[i])); j = i + 2
            while j < len(lines) and lines[j].strip().startswith('|'):
                k = len(b3.split_row(lines[j]))
                if k != n:
                    probs.append('第 %d 行表格列数 %d ≠ 表头 %d（单元格里的竖线要写成 \\|）' % (j + 1, k, n))
                j += 1
            i = j
        else:
            i += 1

    # mermaid 基本语法
    for m in re.finditer(r'```mermaid[^\n]*\n(.*?)\n```', md, flags=re.S):
        src = m.group(1)
        ln = md[:m.start()].count('\n') + 1
        if not re.match(r'^\s*flowchart\s+(TD|TB|LR)\b', src):
            probs.append('第 %d 行 mermaid：第一行必须是 flowchart TD 或 flowchart LR' % ln)
        for x in re.findall(r'\b\w+\s*[\[\{\(]([^"\]\}\)][^\]\}\)]*)[\]\}\)]', src):
            probs.append('第 %d 行 mermaid：节点标签要加双引号 id["…"]，发现：%s' % (ln, x[:30])); break
        nodes = set(re.findall(r'\b([A-Za-z_]\w*)\s*[\[\{\(]', src))
        if len(nodes) > 14:
            probs.append('第 %d 行 mermaid：节点 %d 个，超过 14 个，拆图或删节点' % (ln, len(nodes)))
        for lab in re.findall(r'"([^"]*)"', src):
            if len(lab) > 22:
                probs.append('第 %d 行 mermaid：标签太长（%d 字）「%s」' % (ln, len(lab), lab[:24])); break
        if re.search(r'classDef\s', src):
            probs.append('第 %d 行 mermaid：不要自己写 classDef，用 :::hl / :::warn' % ln)

    # 用渲染器跑一遍，收集渲染警告
    b3.WARN.clear()
    body, toc = b3.convert(md, where, {})
    probs += [w for w in b3.WARN if '跨书链接' not in w]
    figs = body.count('<figure')

    # 跨书链接：只在通用版已存在时核对标题
    xs = re.findall(r'\[\[([^\]]+)\]\]', md)
    if xs and os.path.isdir(gdir):
        titles = []
        for f in sorted(os.listdir(gdir)):
            if f.endswith('.md'):
                titles += [re.sub(r'[*`]', '', t).strip() for t in re.findall(r'^#{1,3}\s+(.+)$', open(os.path.join(gdir, f)).read(), flags=re.M)]
        for x in xs:
            q = re.sub(r'^(通用版|牙科医美版|牙科版)\s*', '', x).strip()
            nq = b3.norm(q)
            hit = any(nq and (nq in b3.norm(t) or b3.norm(t) in nq) for t in titles) or \
                  any(b3.lcs(nq, b3.norm(t)) >= max(4, len(nq) * 0.6) for t in titles)
            if not hit and titles:
                probs.append('[[%s]]：通用版目前没有匹配的小节标题（通用版可能还没写完；写通用版里真实的标题）' % x)

    chars = len(md)
    print('%s：%d 字，%d 张图，%d 个目录项' % (where, chars, figs, len(toc)))
    big = []
    cur, start = None, 0
    for m in re.finditer(r'^##\s+(.+)$', md, flags=re.M):
        if cur is not None and m.start() - start > 7000:
            big.append('%s（%d 字）' % (cur, m.start() - start))
        cur, start = m.group(1), m.start()
    if cur is not None and len(md) - start > 7000:
        big.append('%s（%d 字）' % (cur, len(md) - start))
    for b in big:
        probs.append('小节太长，考虑拆：' + b)
    if probs:
        print('⚠️ %d 个问题：' % len(probs))
        for p in probs:
            print('  -', p)
        sys.exit(1)
    print('OK')

main()
