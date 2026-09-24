#!/usr/bin/env python3
"""v3 手册构建：_v3/<book>/*.md → 单文件 HTML（可多本书同页切换）。
支持图：wireframe / mermaid / bars / steps / split；行业版 @include <id>、[[通用版 …]] 跨书链接。
用法：python3 build_v3.py general            → geo-general.html
      python3 build_v3.py dental general    → geo-dental.html（牙科版 + 通用版同页）
"""
import re, os, sys, json, html

# 书稿根目录：默认是 tools/ 的上一级（其下有 general/、dental/、guide/）；也可用环境变量 GEO_V3 指定
V3 = os.environ.get('GEO_V3') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(V3, '_build')
BOOKS = {
    'general': {'name': '通用版', 'full': 'GEO Playbook · 通用版',
                'tag': '任何行业照着做，把自己在 AI 答案里的位置做上去。'},
    'dental':  {'name': '牙科医美版', 'full': 'GEO Playbook · 牙科医美',
                'tag': '新加坡牙科、医美诊所照着干活的那本。'},
}
WARN = []
# 公开版：GEO_PUBLIC=1 时剔除 <!-- internal --> … <!-- /internal --> 包起来的内容，并整份跳过内部文件
PUBLIC = os.environ.get('GEO_PUBLIC') == '1'
PUBLIC_EXCLUDE = {'dental/dC.md'}

def strip_internal(md):
    if not PUBLIC:  # 内部版：内容保留，只去掉标记本身
        return re.sub(r'[ \t]*<!--\s*/?internal\s*-->[ \t]*\n?', '', md)
    md = re.sub(r'[ \t]*<!--\s*internal\s*-->.*?<!--\s*/internal\s*-->[ \t]*\n?', '', md, flags=re.S)
    return md

def esc(s):
    return html.escape(s, quote=False)

def attr(s):
    return html.escape(s, quote=True)

def inline(s):
    codes = []
    def stash(m):
        codes.append(m.group(1))
        return '\x00%d\x00' % (len(codes) - 1)
    s = re.sub(r'`([^`]+)`', stash, s)
    s = s.replace('<br>', '\x01').replace('<br/>', '\x01').replace('<br />', '\x01')
    s = esc(s)
    s = s.replace('\x01', '<br>')
    s = re.sub(r'\[\[([^\]]+)\]\]', lambda m: xref(m.group(1)), s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)',
               r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'~~([^~]+)~~', r'<del>\1</del>', s)
    return re.sub(r'\x00(\d+)\x00', lambda m: '<code>%s</code>' % esc(codes[int(m.group(1))]), s)

# ───── 跨书链接 ─────
XINDEX = []   # (book, chapter_ix, anchor, plain_title)

def norm(t):
    return re.sub(r'[\s·・:：\-—（）()「」【】\[\]/、,，.。0-9A-Za-z§]+', '', t)

def xref(label):
    lab = label.strip()
    m = re.match(r'^(通用版|牙科医美版|牙科版)\s*(.*)$', lab)
    book = 'general'
    target = lab
    if m:
        book = 'general' if m.group(1) == '通用版' else 'dental'
        target = m.group(2).strip()
    return '<a class="xref" href="#" data-xbook="%s" data-xq="%s">→ %s</a>' % (
        attr(book), attr(target), esc(lab))

def resolve_xrefs(books_out):
    """把 data-xq 解析成具体章与锚点；解析不到的记警告，保留为不跳转的标签。"""
    def best(book, q):
        nq = norm(q)
        numq = re.findall(r'\d+(?:\.\d+)?', q)
        cands = [x for x in XINDEX if x[0] == book]
        # 1) 小节号精确命中（如 5.2）
        if numq:
            for x in cands:
                if re.match(r'^\s*' + re.escape(numq[0]) + r'(\s|·|$)', x[3]):
                    if not norm(q.replace(numq[0], '')) or norm(q.replace(numq[0], ''))[:4] in norm(x[3]):
                        return x
        # 2) 标题包含
        for x in cands:
            nx = norm(x[3])
            if nq and (nq in nx or nx in nq):
                return x
        # 3) 最长公共子串
        bestx, bl = None, 0
        for x in cands:
            nx = norm(x[3])
            l = lcs(nq, nx)
            if l > bl:
                bestx, bl = x, l
        return bestx if bl >= max(4, len(nq) * 0.6) else None

    def fix(m):
        book, q, label = html.unescape(m.group(1)), html.unescape(m.group(2)), m.group(3)
        if book not in books_out:          # 单独发通用版时，指向行业版的链接降级为文字
            return '<span class="xref off">%s</span>' % label
        x = best(book, q)
        if not x:
            WARN.append('跨书链接解析不到：[[%s %s]]' % (BOOKS[book]['name'], q))
            return '<span class="xref off">%s</span>' % label
        return '<a class="xref" href="#%s" data-xbook="%s" data-xch="%d" data-xid="%s">%s</a>' % (
            attr(x[2]), attr(book), x[1], attr(x[2]), label)
    pat = re.compile(r'<a class="xref" href="#" data-xbook="([^"]*)" data-xq="([^"]*)">(.*?)</a>')
    for b in books_out.values():
        for c in b['chapters']:
            c['html'] = pat.sub(fix, c['html'])

def lcs(a, b):
    if not a or not b:
        return 0
    prev = [0] * (len(b) + 1); best = 0
    for ca in a:
        cur = [0]
        for j, cb in enumerate(b):
            v = prev[j] + 1 if ca == cb else 0
            cur.append(v); best = max(best, v)
        prev = cur
    return best

# ───── 图 ─────
def cells(line, sep='|'):
    return [c.strip() for c in line.split(sep)]

def fig(cls, inner, cap, fid=None):
    idattr = ' data-fig="%s"' % attr(fid) if fid else ''
    capx = '<figcaption>%s</figcaption>' % inline(cap) if cap else ''
    return '<figure class="fig %s"%s>%s%s</figure>' % (cls, idattr, inner, capx)

MARKS = {'必': ('m-req', '必需'), '选': ('m-opt', '可选'), '禁': ('m-no', '不要做'),
         '抄': ('m-cite', 'AI 常抄这里'), '规': ('m-law', '合规敏感')}
MARKS_EN_LABEL = {'必': 'Required', '选': 'Optional', '禁': "Don't", '抄': 'AI quotes this', '规': 'Regulated'}
MARK_ALIAS = {'req': '必', 'opt': '选', 'no': '禁', 'cite': '抄', 'law': '规'}
LABEL_LANG = 'zh'

def mark_label(m):
    return MARKS_EN_LABEL[m] if LABEL_LANG == 'en' else MARKS[m][1]

def r_wireframe(lines, cap, fid, where):
    rows, used = [], set()
    for ln in lines:
        if not ln.strip():
            continue
        depth = (len(ln) - len(ln.lstrip(' '))) // 2
        cs = cells(ln.strip())
        k = cs[0] if cs else ''
        v = cs[1] if len(cs) > 1 else ''
        ms = [m.strip() for m in re.split(r'[,，、\s]+', cs[2])] if len(cs) > 2 else []
        cls = ['wf-row', 'lv%d' % min(depth, 2)]
        tags = []
        for m in ms:
            if not m:
                continue
            m = MARK_ALIAS.get(m.lower(), m)
            if m not in MARKS:
                WARN.append('%s wireframe 未知标记「%s」' % (where, m)); continue
            cls.append(MARKS[m][0]); used.add(m)
            if m in ('抄', '规', '禁'):
                tags.append('<i class="tg %s">%s</i>' % (MARKS[m][0].replace('m-', 't-'), mark_label(m)))
        if len(cs) > 3:
            WARN.append('%s wireframe 一行超过 3 列（说明里有竖线？）：%s' % (where, ln.strip()[:60]))
        rows.append('<div class="%s"><span class="wf-k">%s</span><span class="wf-v">%s</span>%s</div>' % (
            ' '.join(cls), inline(k), inline(v), ''.join(tags)))
    legend = ''.join('<span class="lg %s">%s</span>' % (MARKS[m][0], mark_label(m))
                     for m in ['必', '选', '抄', '规', '禁'] if m in used)
    inner = ('<div class="wf-page"><div class="wf-bar"><span></span><span></span><span></span></div>'
             '<div class="wf-body">%s</div></div><div class="legend">%s</div>') % (''.join(rows), legend)
    return fig('wf', inner, cap, fid)

def r_bars(lines, cap, fid, where):
    unit, mx, items = '', None, []
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        m = re.match(r'^unit\s*[:：]\s*(.*)$', s)
        if m:
            unit = m.group(1).strip(); continue
        m = re.match(r'^max\s*[:：]\s*([\d.]+)$', s)
        if m:
            mx = float(m.group(1)); continue
        if s.startswith('#'):
            items.append(('g', s.lstrip('#').strip())); continue
        cs = cells(s)
        try:
            val = float(cs[1].replace(',', ''))
        except (IndexError, ValueError):
            WARN.append('%s bars 数值解析失败：%s' % (where, s[:60])); continue
        items.append(('b', cs[0], val, cs[2] if len(cs) > 2 else ''))
    top = mx or max([x[2] for x in items if x[0] == 'b'] or [1]) or 1
    out = []
    for x in items:
        if x[0] == 'g':
            out.append('<div class="bar-g">%s</div>' % inline(x[1])); continue
        _, lab, val, note = x
        w = max(0.0, min(100.0, val / top * 100))
        vs = ('%g' % val) + unit
        out.append('<div class="bar-row"><span class="bl">%s</span><span class="bt"><span class="bf%s" style="width:%.1f%%"></span></span>'
                   '<span class="bv">%s</span><span class="bn">%s</span></div>' % (
                       inline(lab), ' zero' if val == 0 else '', w, esc(vs), inline(note)))
    return fig('bars', '<div class="bar-list">%s</div>' % ''.join(out), cap, fid)

def r_steps(lines, cap, fid, where):
    out = []
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        cs = cells(s) + ['', '']
        out.append('<li><span class="st-when">%s</span><span class="st-t">%s</span><span class="st-d">%s</span></li>' % (
            inline(cs[0]), inline(cs[1]), inline(cs[2])))
    if len(out) > 9:
        WARN.append('%s steps 超过 8 步（%d）' % (where, len(out)))
    return fig('steps', '<ol class="st">%s</ol>' % ''.join(out), cap, fid)

def r_split(lines, cap, fid, where):
    rows = [cells(l.strip(), '||') for l in lines if l.strip()]
    if not rows:
        return ''
    head = rows[0] + ['']
    arrow = bool(re.search(r'禁|不要|不能|旧|错|别|原来', head[0]))
    cls = 'split arrow' if arrow else 'split'
    h = '<div class="sp-h"><span>%s</span><span></span><span>%s</span></div>' % (inline(head[0]), inline(head[1]))
    body = ''.join('<div class="sp-r"><span class="sp-l">%s</span><span class="sp-x" aria-hidden="true">→</span><span class="sp-rt">%s</span></div>' % (
        inline(r[0]), inline(r[1] if len(r) > 1 else '')) for r in rows[1:])
    return fig(cls, '<div class="sp">%s%s</div>' % (h, body), cap, fid)

def r_mermaid(lines, cap, fid, where):
    src = '\n'.join(lines).strip('\n')
    if not re.match(r'^\s*(flowchart|graph)\s+(TD|TB|LR|RL|BT)', src):
        WARN.append('%s mermaid 不是 flowchart TD/LR 开头' % where)
    return fig('mmd', '<pre class="mmd-src" hidden>%s</pre><div class="mmd-out"></div>' % esc(src), cap, fid)

RENDER = {'wireframe': r_wireframe, 'bars': r_bars, 'steps': r_steps, 'split': r_split, 'mermaid': r_mermaid}

def parse_info(info):
    """```<type> [id=xx] 图：caption"""
    info = info.strip()
    typ = info.split()[0] if info else ''
    rest = info[len(typ):].strip()
    fid = None
    m = re.match(r'^id=([\w\-]+)\s*', rest)
    if m:
        fid = m.group(1); rest = rest[m.end():]
    cap = re.sub(r'^图[:：]\s*', '图：', rest.strip()) if rest.strip() else ''
    return typ, fid, cap

# ───── @include ─────
FIGS = {}

def collect_figs(md, where):
    lines = md.split('\n'); i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith('```'):
            typ, fid, _ = parse_info(lines[i].lstrip()[3:])
            j = i + 1
            while j < len(lines) and not lines[j].lstrip().startswith('```'):
                j += 1
            if fid:
                if fid in FIGS:
                    WARN.append('图 id 重复：%s（%s 与 %s）' % (fid, FIGS[fid][1], where))
                FIGS[fid] = ('\n'.join(lines[i:j + 1]), where)
            i = j + 1
        else:
            i += 1

def expand_includes(md, where):
    def rep(m):
        fid = m.group(1)
        if fid not in FIGS:
            WARN.append('%s @include %s：通用版里没有这张图' % (where, fid))
            return '> ⚠️ 缺图 %s' % fid
        return FIGS[fid][0]
    return re.sub(r'^\s*@include\s+([\w\-]+)\s*$', rep, md, flags=re.M)

# ───── markdown ─────
def split_row(line):
    line = line.strip()
    if line.startswith('|'): line = line[1:]
    if line.endswith('|'): line = line[:-1]
    return [c.strip() for c in re.split(r'(?<!\\)\|', line)]

def convert(md, where, seen):
    lines = md.split('\n')
    out, toc = [], []
    i, n = 0, len(lines)

    def anchor(t):
        a = re.sub(r'[^\w\u4e00-\u9fff]+', '-', t).strip('-')[:60] or 'sec'
        seen[a] = seen.get(a, 0) + 1
        return a if seen[a] == 1 else '%s-%d' % (a, seen[a])

    while i < n:
        ln = lines[i]
        if ln.lstrip().startswith('```'):
            info = ln.lstrip()[3:]
            typ, fid, cap = parse_info(info)
            i += 1; buf = []
            while i < n and not lines[i].lstrip().startswith('```'):
                buf.append(lines[i]); i += 1
            i += 1
            if typ in RENDER:
                if not cap:
                    WARN.append('%s %s 图缺「图：」说明' % (where, typ))
                out.append(RENDER[typ](buf, cap, fid, where))
            else:
                out.append('<pre class="code"%s><code>%s</code></pre>' % (
                    ' data-lang="%s"' % attr(typ) if typ else '', esc('\n'.join(buf))))
            continue
        m = re.match(r'^(#{1,5})\s+(.*)$', ln)
        if m:
            lv = min(len(m.group(1)), 4); raw = m.group(2).strip()
            plain = re.sub(r'[*`]', '', raw)
            a = anchor(plain)
            if lv <= 3:
                toc.append((lv, plain, a))
            out.append('<h%d id="%s" class="h%d">%s</h%d>' % (lv, a, lv, inline(raw), lv))
            i += 1; continue
        if re.match(r'^\s*(-{3,}|\*{3,}|_{3,})\s*$', ln):
            out.append('<hr>'); i += 1; continue
        if ln.strip().startswith('|') and i + 1 < n and re.match(r'^\s*\|[\s:\-|]+\|\s*$', lines[i + 1]):
            head = split_row(ln); i += 2; rows = []
            while i < n and lines[i].strip().startswith('|'):
                rows.append(split_row(lines[i])); i += 1
            t = ['<div class="tw"><table><thead><tr>']
            t += ['<th>%s</th>' % inline(c.replace('\\|', '|')) for c in head]
            t.append('</tr></thead><tbody>')
            for r in rows:
                r = (r + [''] * len(head))[:len(head)]
                t.append('<tr>' + ''.join('<td>%s</td>' % inline(c.replace('\\|', '|')) for c in r) + '</tr>')
            t.append('</tbody></table></div>')
            out.append(''.join(t)); continue
        if ln.lstrip().startswith('>'):
            buf = []
            while i < n and (lines[i].lstrip().startswith('>') or
                             (buf and lines[i].strip() and not re.match(r'^\s*[|#\-*\d`]', lines[i]))):
                buf.append(re.sub(r'^\s*>\s?', '', lines[i])); i += 1
            inner, sub = convert('\n'.join(buf), where, seen)
            toc += sub
            first = buf[0].strip() if buf else ''
            kind = ' class="ex"' if re.match(r'^\*\*(举例|例)', first) else (
                ' class="warn"' if re.match(r'^\*\*(⚠️|注意|红线|别)', first) else '')
            out.append('<blockquote%s>%s</blockquote>' % (kind, inner)); continue
        m = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.*)$', ln)
        if m:
            ordered = bool(re.match(r'\d+\.', m.group(2)))
            tag = 'ol' if ordered else 'ul'
            items, base = [], len(m.group(1))
            while i < n:
                mm = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.*)$', lines[i])
                if not mm or len(mm.group(1)) < base:
                    if lines[i].strip() and not re.match(r'^\s*([-*+]|\d+\.)\s', lines[i]) \
                       and items and len(lines[i]) - len(lines[i].lstrip()) > base:
                        items[-1] += ' ' + lines[i].strip(); i += 1; continue
                    break
                if len(mm.group(1)) > base and items:
                    items[-1] += '\x02' + mm.group(3); i += 1; continue
                items.append(mm.group(3)); i += 1
            def li(x):
                parts = x.split('\x02')
                sub = ''.join('<li>%s</li>' % inline(p) for p in parts[1:])
                return '<li>%s%s</li>' % (inline(parts[0]), '<ul>%s</ul>' % sub if sub else '')
            out.append('<%s>%s</%s>' % (tag, ''.join(li(x) for x in items), tag)); continue
        if not ln.strip():
            i += 1; continue
        if re.match(r'^\s*@include\s', ln):
            i += 1; continue
        buf = [ln]; i += 1
        while i < n and lines[i].strip() and not re.match(r'^\s*(#{1,5}\s|[-*+]\s|\d+\.\s|\||>|```|-{3,})', lines[i]):
            buf.append(lines[i]); i += 1
        out.append('<p>%s</p>' % inline(' '.join(x.strip() for x in buf)))
    return '\n'.join(out), toc

def _stem(fn):
    m = re.match(r'^[a-z]+(\d+|[A-Z])(?:-([0-9A-Z]))?$', os.path.splitext(fn)[0])
    return (m.group(1), m.group(2) or '') if m else (None, '')

def chapter_label(fn, book):
    n, part = _stem(fn)
    if n is None:
        return os.path.splitext(fn)[0]
    return ('第 %d 章' % int(n)) if n.isdigit() else ('附录 ' + n)

def order_key(fn):
    n, part = _stem(fn)
    if n is None:
        return (2, 0, fn)
    return (0, int(n), part) if n.isdigit() else (1, 0, n + part)

def load_book(key):
    d = os.path.join(V3, key)
    files = sorted([f for f in os.listdir(d) if re.match(r'^[a-z]+(\d+|[A-Z])(-[0-9A-Z])?\.md$', f)], key=order_key)
    out = []
    for f in files:
        if PUBLIC and (key + '/' + f) in PUBLIC_EXCLUDE:
            continue
        out.append((f, strip_internal(open(os.path.join(d, f)).read())))
    return out

def build(keys):
    # 通用版总是先收图，供行业版 include
    if 'general' in keys or any(k != 'general' for k in keys):
        for fn, md in load_book('general'):
            collect_figs(md, 'general/' + fn)
    books_out = {}
    for key in keys:
        chs = []
        for ix, (fn, md) in enumerate(load_book(key)):
            where = key + '/' + fn
            if key != 'general':
                md = expand_includes(md, where)
            raw_md = md
            title, sub = fn, ''
            m = re.search(r'^#\s+(.+)$', md, flags=re.M)
            if m:
                title = re.sub(r'^(第\s*\d+\s*章|附录\s*[A-Z])\s*[·・:：]?\s*', '', m.group(1).strip())
                title = re.sub(r'^附录\s*[·・:：]\s*', '', title)
                md = md[:m.start()] + md[m.end():]
            ms = re.search(r'<!--\s*sub:\s*(.*?)\s*-->', md)
            if ms:
                sub = ms.group(1); md = md.replace(ms.group(0), '')
            seen = {}
            body, toc = convert(md, where, seen)
            # 锚点加书与章前缀，防止两本书冲突
            pre = '%s%d-' % (key[0], ix)
            body = re.sub(r' id="([^"]+)"', lambda mm: ' id="%s%s"' % (pre, mm.group(1)), body)
            toc = [(lv, t, pre + a) for lv, t, a in toc]
            for lv, t, a in toc:
                XINDEX.append((key, ix, a, t))
            XINDEX.append((key, ix, pre + 'top', title))
            chs.append({'file': fn, 'label': chapter_label(fn, key), 'title': title, 'sub': sub,
                        'html': body, 'toc': toc, 'chars': len(md), 'figs': body.count('<figure'),
                        'md': re.sub(r'<!--\s*sub:.*?-->\n?', '', raw_md).strip()})
        books_out[key] = {'key': key, 'name': BOOKS[key]['name'], 'full': BOOKS[key]['full'],
                          'tag': BOOKS[key]['tag'], 'chapters': chs}
    resolve_xrefs(books_out)
    return books_out

if __name__ == '__main__':
    keys = sys.argv[1:] or ['general']
    books = build(keys)
    for k in keys:
        b = books[k]
        print('%s：%d 章，%d 字，%d 张图' % (b['name'], len(b['chapters']),
              sum(c['chars'] for c in b['chapters']), sum(c['figs'] for c in b['chapters'])))
        for c in b['chapters']:
            print('   %-6s %-22s %7d 字 %3d 图' % (c['label'], c['title'][:22], c['chars'], c['figs']))
    if WARN:
        print('\n⚠️ %d 条警告：' % len(WARN))
        for w in WARN:
            print('  -', w)
    name = '-'.join(keys) + ('_public' if PUBLIC else '')
    json.dump([books[k] for k in keys], open(os.path.join(OUT, 'v3_%s.json' % name), 'w'), ensure_ascii=False)
    print('→', os.path.join(OUT, 'v3_%s.json' % name))
