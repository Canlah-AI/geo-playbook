#!/usr/bin/env python3
"""公开版 → 官网用的静态素材（_v3/_site/）。
- 每章一份静态 HTML（爬虫不执行 JS 也读得到正文）
- mermaid 在本地用浏览器预渲染成内联 SVG（官网深色主题配色）
- 跨章链接改成真实网址 /zh/playbook/<slug>/#锚点
- 书内容专用样式 geo-book.css（全部限定在 .geo-book 下，不影响官网其他页面）
- 轻量版网页数据 guide-zh.json / guide-en.json、下载文件
用法：.venv/bin/python emit_site.py
"""
import os, re, sys, json, html, shutil, hashlib, subprocess, asyncio

HERE = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.dirname(HERE)
BUILD = os.path.join(V3, '_build')
SITE = os.path.join(V3, '_site')
PY = sys.executable

SLUGS = {
    'general': {'g0.md': 'start', 'g1.md': 'how-ai-answers', 'g2.md': 'open-the-door', 'g3.md': 'identity',
                'g4.md': 'pick-questions', 'g5-0.md': 'write-pages', 'g5-A.md': 'page-types-core',
                'g5-B.md': 'page-types-more', 'g5-C.md': 'page-types-checklist', 'g5-D.md': 'at-scale',
                'g6.md': 'off-site', 'g7.md': 'measure', 'g8.md': 'new-industry', 'gA.md': 'evidence',
                'gB.md': 'templates', 'gC.md': 'industry-reference', 'gD.md': 'glossary'},
    'dental': {'d0.md': 'start', 'd1.md': 'rules', 'd2.md': 'week-one', 'd3.md': 'identity',
               'd4.md': 'pick-questions', 'd5-0.md': 'write-pages', 'd5-A.md': 'price-pages',
               'd5-B.md': 'fact-pages', 'd5-C.md': 'trust-pages', 'd6.md': 'off-site', 'd7.md': 'measure',
               'dA.md': 'statutes', 'dB.md': 'templates'},
}
BASE = {'general': '/zh/playbook/', 'dental': '/zh/playbook/dental/'}
NAME = {'general': '通用版', 'dental': '牙科医美版'}

# 官网 marketing-theme 的深色 token
TOK = {'--paper': '#10141b', '--sheet': '#181e27', '--sheet-2': '#202935', '--ink': '#f1f2ed', '--ink-2': '#c5ccda',
       '--muted': '#a7b0bd', '--rule': '#303947', '--rule-2': '#3d4757', '--accent': '#b5bffa',
       '--accent-soft': '#252c4d', '--accent-ink': '#d3d8fd', '--warn': '#f4b780', '--warn-soft': '#30251e'}

def run_public_builds():
    env = dict(os.environ, GEO_PUBLIC='1')
    for args in (['general'], ['dental', 'general']):
        subprocess.run([PY, os.path.join(HERE, 'build_v3.py')] + args, env=env, check=True, stdout=subprocess.DEVNULL)
    for lang in ('zh', 'en'):
        if not os.path.exists(os.path.join(BUILD, 'guide-%s.json' % lang)):
            subprocess.run([PY, os.path.join(HERE, 'build_guide.py'), lang], check=True)
    return (json.load(open(os.path.join(BUILD, 'v3_general_public.json')))[0],
            json.load(open(os.path.join(BUILD, 'v3_dental-general_public.json')))[0])

def fix_xrefs(h, book_chapters):
    def rep(m):
        anchor, book, ch = m.group(1), m.group(2), int(m.group(3))
        chs = book_chapters.get(book)
        if not chs or ch >= len(chs):
            return m.group(0)
        slug = SLUGS[book][chs[ch]['file']]
        return '<a class="xref" href="%s%s/#%s">' % (BASE[book], slug, anchor)
    return re.sub(r'<a class="xref" href="#([^"]+)" data-xbook="(\w+)" data-xch="(\d+)" data-xid="[^"]*">', rep, h)

MMD_RE = re.compile(r'<pre class="mmd-src" hidden>(.*?)</pre><div class="mmd-out"></div>', re.S)

async def render_mermaid(srcs):
    from playwright.async_api import async_playwright
    out = {}
    page_html = ('<!doctype html><html><body style="background:%s">'
                 '<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/11.15.0/mermaid.min.js"></script></body></html>') % TOK['--paper']
    async with async_playwright() as pw:
        br = await pw.chromium.launch()
        pg = await br.new_page(viewport={'width': 1200, 'height': 900})
        await pg.set_content(page_html, wait_until='networkidle')
        await pg.evaluate("""(t) => mermaid.initialize({startOnLoad:false, securityLevel:'strict', theme:'base',
            fontFamily:'"DM Sans","Noto Sans SC","PingFang SC",sans-serif',
            themeVariables:{primaryColor:t['--sheet'], primaryBorderColor:t['--rule-2'], primaryTextColor:t['--ink'],
              lineColor:t['--muted'], textColor:t['--ink-2'], secondaryColor:t['--sheet-2'], tertiaryColor:t['--paper'],
              edgeLabelBackground:t['--paper'], fontSize:'15px'},
            flowchart:{htmlLabels:true, curve:'basis', padding:8, nodeSpacing:30, rankSpacing:38, wrappingWidth:118}})""", TOK)
        defs = ('\n  classDef hl fill:%s,stroke:%s,color:%s,stroke-width:1.5px;\n  classDef warn fill:%s,stroke:%s,color:%s;'
                % (TOK['--accent-soft'], TOK['--accent'], TOK['--accent-ink'], TOK['--warn-soft'], TOK['--warn'], TOK['--warn']))
        for k, src in srcs.items():
            s = re.sub(r'(\b[A-Za-z_]\w*)\{"([^"{}]*)"\}', r'\1{{"\2"}}', src)
            gid = 'gb' + k[:10]
            try:
                svg = await pg.evaluate('([id,s]) => mermaid.render(id, s).then(r => r.svg)', [gid, s + defs])
                vb = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"', svg)
                w = float(vb.group(1)) if vb else 0
                if w > 820 and re.match(r'^\s*flowchart\s+LR', s):   # 太宽的横向图改竖排，免得缩到看不清
                    svg = await pg.evaluate('([id,s]) => mermaid.render(id, s).then(r => r.svg)',
                                            [gid + 't', re.sub(r'^(\s*flowchart\s+)LR', r'\1TD', s) + defs])
                out[k] = svg
            except Exception as e:
                out[k] = None
                print('⚠️ mermaid 渲染失败：', src[:60].replace('\n', ' '), '|', str(e)[:120])
        await br.close()
    return out

def scope_css(css):
    """把书的 CSS 限定到 .geo-book 下：:root token 换成 .geo-book，其余选择器加前缀；跳过侧栏 / 翻页 / 搜索等阅读器外壳。"""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    skip = re.compile(r'^(\s*)(\*|html|body|\.wrap|aside|\.brand|\.books|\.bk|\.searchbox|#q|nav|\.chap|\.subtoc|main|\.sheet|\.chead|\.pager|\.pbtn|#results|\.rhit|\.rnone|\.dl|\.dlb|\.dls|:focus-visible)\b')
    out = []
    def prefix_block(block):
        res = []
        for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', block):
            sels, body = m.group(1).strip(), m.group(2)
            if sels.startswith(':root') or '[data-theme' in sels:
                continue
            keep = [s.strip() for s in sels.split(',') if s.strip() and not skip.match(s.strip())]
            if not keep:
                continue
            keep = ['.geo-book ' + re.sub(r'^article\s*', '', s) if s.startswith('article') else '.geo-book ' + s for s in keep]
            res.append('%s{%s}' % (','.join(keep), body.strip()))
        return '\n'.join(res)
    # @media 块单独处理（只保留非 prefers-color-scheme 的）
    pos = 0
    for m in re.finditer(r'@media([^{]+)\{((?:[^{}]*\{[^{}]*\})*)\s*\}', css):
        out.append(prefix_block(css[pos:m.start()]))
        cond = m.group(1).strip()
        if 'prefers-color-scheme' not in cond:
            inner = prefix_block(m.group(2))
            if inner:
                out.append('@media %s{%s}' % (cond, inner))
        pos = m.end()
    out.append(prefix_block(css[pos:]))
    tokens = '.geo-book{%s;--serif:"DM Sans","Noto Sans SC","PingFang SC",sans-serif;--sans:"DM Sans","Noto Sans SC","PingFang SC",sans-serif;' \
             '--mono:"DM Mono",ui-monospace,Menlo,"Noto Sans SC","PingFang SC",monospace;color:var(--ink);line-height:1.85}' % \
             ';'.join('%s:%s' % kv for kv in TOK.items())
    extra = ('.geo-book .mmd-out{overflow-x:auto;background:var(--sheet);border:1px solid var(--rule);border-radius:4px;padding:16px 12px;text-align:center}'
             '.geo-book .mmd-out svg{height:auto;max-width:100%}'
             '.geo-book .h1,.geo-book .h2{scroll-margin-top:96px}.geo-book .h3{scroll-margin-top:96px}')
    return tokens + '\n' + '\n'.join(x for x in out if x) + '\n' + extra + '\n'

def main():
    general, dental = run_public_builds()
    books = {'general': general, 'dental': dental}
    book_chapters = {k: b['chapters'] for k, b in books.items()}
    guides = {l: json.load(open(os.path.join(BUILD, 'guide-%s.json' % l))) for l in ('zh', 'en')}

    # 收集所有 mermaid 源
    srcs = {}
    def collect(h):
        for m in MMD_RE.finditer(h):
            s = html.unescape(m.group(1))
            srcs[hashlib.sha1(s.encode()).hexdigest()] = s
    for b in books.values():
        for c in b['chapters']:
            collect(c['html'])
    for g in guides.values():
        for p in g:
            collect(p['fig'])
    print('预渲染 %d 张流程图…' % len(srcs))
    svgs = asyncio.run(render_mermaid(srcs))

    def inline(h):
        def rep(m):
            k = hashlib.sha1(html.unescape(m.group(1)).encode()).hexdigest()
            svg = svgs.get(k)
            if not svg:
                return '<pre class="code"><code>%s</code></pre>' % m.group(1)
            return '<div class="mmd-out">%s</div>' % svg
        return MMD_RE.sub(rep, h)

    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE)
    manifest = {'generated': 'emit_site.py', 'books': [], 'guide': {}, 'downloads': []}
    for key, b in books.items():
        os.makedirs(os.path.join(SITE, key))
        chs = []
        for i, c in enumerate(b['chapters']):
            slug = SLUGS[key][c['file']]
            body = inline(fix_xrefs(c['html'], book_chapters))
            open(os.path.join(SITE, key, slug + '.html'), 'w').write(body)
            plain = re.sub(r'<[^>]+>', ' ', body); plain = re.sub(r'\s+', ' ', html.unescape(plain)).strip()
            chs.append({'slug': slug, 'label': c['label'], 'title': c['title'], 'sub': c.get('sub', ''),
                        'toc': [{'level': t[0], 'title': t[1], 'id': t[2]} for t in c['toc'] if t[0] == 2],
                        'figures': c['figs'], 'chars': c['chars'], 'html': '%s/%s.html' % (key, slug),
                        'description': plain[:150]})
        manifest['books'].append({'key': key, 'name': NAME[key], 'full': b['full'], 'tag': b['tag'],
                                  'base': BASE[key], 'chapters': chs})
    for lang, g in guides.items():
        pages = [{'title': p['title'], 'fig': inline(p['fig']), 'body': p['body'], 'full': p['full'], 'qr': p['qr']} for p in g]
        # full 字段 → 完整版对应小节的真实链接
        idx = {}
        for c in manifest['books'][0]['chapters']:
            for t in c['toc']:
                num = re.match(r'^\s*([\dA-Z]+\.[\dA-Z]+)', t['title'])
                if num:
                    idx[num.group(1)] = '%s%s/#%s' % (BASE['general'], c['slug'], t['id'])
        for p in pages:
            num = re.match(r'^\s*([\dA-Z]+\.[\dA-Z]+)', p['full'] or '')
            p['fullHref'] = idx.get(num.group(1)) if num else None
            p['fullNum'] = num.group(1) if num else None
        json.dump(pages, open(os.path.join(SITE, 'guide-%s.json' % lang), 'w'), ensure_ascii=False, indent=1)
        manifest['guide'][lang] = 'guide-%s.json' % lang
    open(os.path.join(SITE, 'geo-book.css'), 'w').write(
        scope_css(re.search(r"CSS = r'''(.*?)'''", open(os.path.join(HERE, 'emit_v3.py')).read(), re.S).group(1)))
    dl = os.path.join(SITE, 'downloads'); os.makedirs(dl)
    for f, name in (('GEO-Playbook-轻量版-2026.pdf', 'geo-playbook-quick-guide-zh.pdf'),
                    ('GEO-Playbook-轻量版-2026.pptx', 'geo-playbook-quick-guide-zh.pptx'),
                    ('GEO-Playbook-Quick-Guide-2026.pdf', 'geo-playbook-quick-guide-en.pdf'),
                    ('GEO-Playbook-Quick-Guide-2026.pptx', 'geo-playbook-quick-guide-en.pptx')):
        src = os.path.join(BUILD, f)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(dl, name)); manifest['downloads'].append({'file': 'downloads/' + name, 'bytes': os.path.getsize(src)})
    # 全书 markdown（公开版）也给下载
    for key, b in books.items():
        name = 'geo-playbook-%s-zh.md' % key
        md = '# %s\n\n> Canlah AI · CC BY 4.0 · https://canlah.ai%s\n' % (b['full'], BASE[key]) + ''.join('\n\n' + c['md'] for c in b['chapters']) + '\n'
        open(os.path.join(dl, name), 'w').write(md); manifest['downloads'].append({'file': 'downloads/' + name, 'bytes': len(md.encode())})
    json.dump(manifest, open(os.path.join(SITE, 'manifest.json'), 'w'), ensure_ascii=False, indent=1)
    # 泄漏检查：本机路径、内部标记，外加 GEO_LEAK_WORDS（逗号分隔）或 tools/leak-words.txt（每行一个，不入库）里的词
    words = [w for w in os.environ.get('GEO_LEAK_WORDS', '').split(',') if w.strip()]
    wf = os.path.join(HERE, 'leak-words.txt')
    if os.path.exists(wf):
        words += [l.strip() for l in open(wf) if l.strip() and not l.startswith('#')]
    pats = [re.compile(r'/(?:Users|home)/[^/\s]+/'), re.compile(r'~/[A-Za-z]'), re.compile(r'scratchpad'),
            re.compile(r'<!--\s*internal')] + [re.compile(re.escape(w.strip()), re.I) for w in words]
    pages = [open(os.path.join(SITE, k['key'], c['slug'] + '.html')).read() for k in manifest['books'] for c in k['chapters']]
    leaks = [p.pattern for p in pats if any(p.search(h) for h in pages)]
    print('通用版 %d 章、牙科版 %d 章 → %s' % (len(general['chapters']), len(dental['chapters']), SITE))
    print('流程图：%d 张，失败 %d 张' % (len(svgs), sum(1 for v in svgs.values() if not v)))
    print('公开版泄漏检查：', '通过' if not leaks else '⚠️ 发现 ' + ', '.join(leaks))

main()
