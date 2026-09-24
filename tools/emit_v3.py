#!/usr/bin/env python3
"""v3_<keys>.json → geo-<keys>.html。用法：python3 emit_v3.py general | dental-general"""
import json, sys, re, os

S = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_build')
name = sys.argv[1] if len(sys.argv) > 1 else 'general'
books = json.load(open('%s/v3_%s.json' % (S, name)))
payload = json.dumps(books, ensure_ascii=False).replace('</', '<\\/')
TITLE = books[0]['full']
STORE = 'geo3-' + name

CSS = r'''
:root{
  --paper:#f4f3ef; --sheet:#fcfbf8; --sheet-2:#eceae4;
  --ink:#191d1b; --ink-2:#414b47; --muted:#75807b;
  --rule:#dcd9d1; --rule-2:#c6c2b8;
  --accent:#0c6252; --accent-soft:#e3efea; --accent-ink:#084a3e;
  --warn:#9a3f11; --warn-soft:#f7e9df;
  --serif:"Noto Serif SC",Songti SC,SimSun,Georgia,serif;
  --sans:"Noto Sans SC",-apple-system,BlinkMacSystemFont,"PingFang SC","Helvetica Neue",sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,"Noto Sans SC","PingFang SC","Hiragino Sans GB","Microsoft YaHei",monospace;
  --measure:42em;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#0e1211; --sheet:#151b19; --sheet-2:#1d2522;
  --ink:#e7eae6; --ink-2:#b2bdb8; --muted:#83908b;
  --rule:#293331; --rule-2:#38433f;
  --accent:#54bda4; --accent-soft:#12302a; --accent-ink:#7fd3bd;
  --warn:#df8a52; --warn-soft:#2f2018;
}}
:root[data-theme="dark"]{
  --paper:#0e1211; --sheet:#151b19; --sheet-2:#1d2522;
  --ink:#e7eae6; --ink-2:#b2bdb8; --muted:#83908b;
  --rule:#293331; --rule-2:#38433f;
  --accent:#54bda4; --accent-soft:#12302a; --accent-ink:#7fd3bd;
  --warn:#df8a52; --warn-soft:#2f2018;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:var(--sans);font-size:15.5px;line-height:1.85;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:var(--serif);margin:0;line-height:1.4;text-wrap:balance}
a{color:var(--accent)}
code{font-family:var(--mono);font-size:.86em;background:var(--sheet-2);
  padding:1px 5px;border-radius:2px;word-break:break-word}

.wrap{display:grid;grid-template-columns:260px minmax(0,1fr);min-height:100%}
@media (max-width:920px){.wrap{grid-template-columns:1fr}}
aside{border-right:1px solid var(--rule);background:var(--sheet);
  position:sticky;top:0;height:100vh;overflow-y:auto;padding:0 0 40px}
@media (max-width:920px){aside{position:static;height:auto;border-right:none;border-bottom:1px solid var(--rule)}}
.brand{padding:24px 20px 16px;border-bottom:1px solid var(--rule)}
.brand .kicker{font-family:var(--mono);font-size:10px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--muted);margin-bottom:9px}
.brand h1{font-size:22px;font-weight:700;letter-spacing:-.01em}
.brand .tag{font-size:12.5px;color:var(--muted);margin-top:7px;line-height:1.6}

.books{display:flex;gap:4px;padding:12px 14px;border-bottom:1px solid var(--rule)}
.books[hidden]{display:none}
.bk{flex:1;border:1px solid var(--rule-2);background:var(--paper);color:var(--ink-2);cursor:pointer;
  font-family:inherit;font-size:13px;padding:7px 8px;border-radius:3px;line-height:1.3}
.bk.on{background:var(--accent);border-color:var(--accent);color:var(--sheet);font-weight:500}

.dl{padding:12px 16px;border-bottom:1px solid var(--rule)}
.dl[hidden]{display:none}
.dlb{width:100%;border:1px solid var(--accent);background:none;color:var(--accent-ink);cursor:pointer;
  font-family:inherit;font-size:13px;padding:7px 10px;border-radius:3px}
.dlb:hover{background:var(--accent-soft)}
.dls{font-size:11.5px;color:var(--muted);margin-top:6px;line-height:1.5;min-height:0}
.dls:empty{display:none}

.searchbox{padding:12px 16px;border-bottom:1px solid var(--rule)}
#q{width:100%;font-family:var(--sans);font-size:13px;padding:8px 11px;
  border:1px solid var(--rule-2);border-radius:3px;background:var(--paper);color:var(--ink)}
#q::placeholder{color:var(--muted)}
#q:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:transparent}

nav{padding:12px 10px}
.chap{width:100%;text-align:left;border:none;background:none;cursor:pointer;
  font-family:inherit;color:var(--ink-2);padding:8px 12px;border-radius:3px;
  display:grid;grid-template-columns:44px 1fr;gap:8px;align-items:baseline;line-height:1.5}
.chap:hover{background:var(--sheet-2)}
.chap.on{background:var(--accent-soft);color:var(--accent-ink)}
.chap .i{font-family:var(--mono);font-size:10.5px;color:var(--muted);white-space:nowrap}
.chap.on .i{color:var(--accent)}
.chap .t{font-family:var(--serif);font-weight:500;font-size:14.5px}
.chap .s{grid-column:2;font-size:11.5px;color:var(--muted);margin-top:1px}
.subtoc{list-style:none;margin:2px 0 8px;padding:0 0 0 30px;display:none}
.subtoc.open{display:block}
.subtoc a{display:block;padding:4px 10px;font-size:12.5px;color:var(--muted);
  text-decoration:none;border-left:1px solid var(--rule);line-height:1.5}
.subtoc a:hover{color:var(--ink)}
.subtoc a.lv3{padding-left:22px;font-size:12px}
.subtoc a.here{color:var(--accent);border-left-color:var(--accent);font-weight:500}

main{padding:0 0 100px;min-width:0}
.sheet{max-width:var(--measure);margin:0 auto;padding:44px 20px 0}
@media (max-width:920px){.sheet{padding-top:28px}}
.chead{border-bottom:1px solid var(--rule);padding-bottom:20px;margin-bottom:28px}
.chead .n{font-family:var(--mono);font-size:11px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--accent);margin-bottom:10px}
.chead h2{font-size:clamp(26px,4.4vw,34px);font-weight:700;letter-spacing:-.015em}
.chead .s{margin-top:9px;color:var(--muted);font-size:13.5px}

article p{margin:0 0 16px}
article>.h2:first-child,article>.h1:first-child{border-top:none;margin-top:0;padding-top:0}
article .h1,article .h2{font-size:22px;font-weight:700;margin:46px 0 14px;
  padding-top:18px;border-top:1px solid var(--rule)}
article .h3{font-size:17.5px;font-weight:700;margin:32px 0 10px}
article .h4{font-size:15.5px;font-weight:700;margin:24px 0 8px;color:var(--ink-2)}
article ul,article ol{margin:0 0 16px;padding-left:1.5em}
article li{margin-bottom:7px}
article li ul{margin:6px 0 0}
article hr{border:none;border-top:1px solid var(--rule);margin:34px 0}
article blockquote{margin:20px 0;padding:14px 18px;border-left:3px solid var(--accent);
  background:var(--accent-soft);border-radius:0 3px 3px 0}
article blockquote.ex{border-left-color:var(--rule-2);background:var(--sheet)}
article blockquote.warn{border-left-color:var(--warn);background:var(--warn-soft)}
article blockquote p{margin:0 0 9px;font-size:14.5px}
article blockquote p:last-child{margin:0}
.code{background:var(--sheet-2);border:1px solid var(--rule);border-radius:3px;
  padding:14px 16px;overflow-x:auto;margin:18px 0;line-height:1.65}
.code code{background:none;padding:0;font-size:12.5px;white-space:pre}
.tw{overflow-x:auto;margin:20px 0;border:1px solid var(--rule);border-radius:3px;background:var(--sheet)}
table{border-collapse:collapse;width:100%;font-size:13.5px;min-width:520px}
th,td{text-align:left;padding:10px 13px;border-bottom:1px solid var(--rule);vertical-align:top;line-height:1.7}
thead th{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;color:var(--muted);
  font-weight:600;background:var(--sheet-2)}
tbody tr:last-child td{border-bottom:none}

.xref{display:inline-block;font-size:12.5px;line-height:1.5;padding:2px 10px;margin:0 2px;
  border:1px solid var(--accent);border-radius:12px;text-decoration:none;
  color:var(--accent-ink);background:var(--accent-soft)}
.xref:hover{background:var(--accent);color:var(--sheet)}
.xref.off{border-color:var(--rule-2);color:var(--muted);background:none}

/* ───── 图：公共 ───── */
.fig{margin:26px 0 30px}
.fig figcaption{font-size:13px;color:var(--ink-2);margin-top:10px;line-height:1.65;max-width:38em}

/* 施工图 */
.wf-page{border:1px solid var(--rule-2);border-radius:6px;background:var(--sheet);max-width:560px;overflow:hidden}
.wf-bar{height:22px;background:var(--sheet-2);border-bottom:1px solid var(--rule);
  display:flex;gap:5px;align-items:center;padding:0 10px}
.wf-bar span{width:7px;height:7px;border-radius:50%;background:var(--rule-2)}
.wf-body{padding:12px;display:grid;gap:6px}
.wf-row{display:flex;flex-wrap:wrap;gap:2px 10px;align-items:baseline;padding:7px 10px;
  border:1px solid var(--rule-2);border-radius:3px;background:var(--paper);font-size:13px;line-height:1.5}
.wf-row.lv1{margin-left:20px}
.wf-row.lv2{margin-left:40px}
.wf-k{flex:0 0 7.5em;font-weight:600}
.wf-v{flex:1 1 12em;color:var(--ink-2)}
.wf-row.m-opt{border-style:dashed;background:transparent}
.wf-row.m-opt .wf-k,.wf-row.m-opt .wf-v{color:var(--muted)}
.wf-row.m-no{border-style:dashed;border-color:var(--warn);background:transparent}
.wf-row.m-no .wf-k,.wf-row.m-no .wf-v{text-decoration:line-through;color:var(--muted)}
.wf-row.m-cite{background:var(--accent-soft);border-color:var(--accent);box-shadow:inset 3px 0 0 var(--accent)}
.tg{font-style:normal;font-size:10.5px;font-family:var(--mono);padding:1px 6px;border-radius:2px;
  white-space:nowrap;margin-left:auto;line-height:1.6}
.tg.t-cite{background:var(--accent);color:var(--sheet)}
.tg.t-law{border:1px solid var(--warn);color:var(--warn)}
.tg.t-no{color:var(--warn)}
.legend{display:flex;gap:6px 14px;flex-wrap:wrap;margin-top:8px;font-size:11.5px;color:var(--muted)}
.lg::before{content:"";display:inline-block;width:14px;height:10px;border:1px solid var(--rule-2);
  margin-right:5px;vertical-align:-1px;border-radius:2px;background:var(--paper)}
.lg.m-opt::before{border-style:dashed;background:none}
.lg.m-cite::before{background:var(--accent-soft);border-color:var(--accent)}
.lg.m-law::before{border-color:var(--warn)}
.lg.m-no::before{border-color:var(--warn);border-style:dashed;background:none}

/* 横条 */
.bar-list{display:grid;gap:9px;max-width:620px}
.bar-row{display:grid;grid-template-columns:minmax(120px,38%) 1fr 4.5em;gap:3px 12px;align-items:center;font-size:13px;line-height:1.45}
.bt{height:12px;background:var(--sheet-2);border-radius:2px;overflow:hidden}
.bf{display:block;height:100%;background:var(--accent);border-radius:2px}
.bv{font-family:var(--mono);font-size:12px;text-align:right;font-variant-numeric:tabular-nums}
.bn{grid-column:2/-1;font-size:11.5px;color:var(--muted)}
.bn:empty{display:none}
.bar-g{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;color:var(--muted);margin-top:8px}
@media (max-width:560px){.bar-row{grid-template-columns:1fr 4em}.bl{grid-column:1/-1}.bn{grid-column:1/-1}}

/* 步骤 */
.st{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(128px,1fr));gap:0 4px}
.st li{position:relative;padding:14px 12px 10px 0;border-top:2px solid var(--accent);margin:0}
.st li::before{content:"";position:absolute;top:-6px;left:0;width:10px;height:10px;border-radius:50%;
  background:var(--accent);box-shadow:0 0 0 3px var(--paper)}
.st-when{display:block;font-family:var(--mono);font-size:11px;color:var(--accent);margin-top:4px}
.st-t{display:block;font-weight:700;font-family:var(--serif);font-size:15px;line-height:1.45}
.st-d{display:block;font-size:12.5px;color:var(--ink-2);line-height:1.6;margin-top:3px}

/* 左右对照 */
.sp{border:1px solid var(--rule);border-radius:4px;overflow:hidden;background:var(--sheet);max-width:640px}
.sp-h,.sp-r{display:grid;grid-template-columns:1fr 22px 1fr}
.split:not(.arrow) .sp-h,.split:not(.arrow) .sp-r{grid-template-columns:1fr 1px 1fr}
.split:not(.arrow) .sp-x{visibility:hidden}
.sp-h span{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;color:var(--muted);
  padding:9px 12px;background:var(--sheet-2)}
.split.arrow .sp-h span:first-child{color:var(--warn)}
.split.arrow .sp-h span:last-child{color:var(--accent)}
.sp-r>span{padding:9px 12px;border-top:1px solid var(--rule);font-size:13.5px;line-height:1.6}
.sp-r .sp-x{padding:9px 0;color:var(--accent);text-align:center}
.split.arrow .sp-l{color:var(--ink-2)}
.split:not(.arrow) .sp-rt{border-left:1px solid var(--rule)}

/* mermaid */
.mmd-out{overflow-x:auto;background:var(--sheet);border:1px solid var(--rule);border-radius:4px;
  padding:18px 14px;text-align:center;min-height:60px}
.mmd-out svg{height:auto;display:block;margin:0 auto}
.mmd-out .code{text-align:left;margin:0}

.pager{max-width:var(--measure);margin:54px auto 0;padding:22px 20px 0;
  border-top:1px solid var(--rule);display:flex;gap:12px;justify-content:space-between}
.pbtn{flex:1;max-width:48%;border:1px solid var(--rule-2);background:var(--sheet);border-radius:3px;
  padding:13px 16px;cursor:pointer;font-family:inherit;text-align:left;color:var(--ink)}
.pbtn:hover{border-color:var(--accent)}
.pbtn[hidden]{display:none}
.pbtn .d{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.12em;color:var(--muted);margin-bottom:5px}
.pbtn .t{font-family:var(--serif);font-weight:600;font-size:14.5px}
.pbtn.next{text-align:right;margin-left:auto}

#results{max-width:var(--measure);margin:0 auto;padding:30px 20px}
.rhit{display:block;width:100%;text-align:left;border:none;border-bottom:1px solid var(--rule);
  background:none;cursor:pointer;font-family:inherit;padding:14px 4px;color:var(--ink)}
.rhit:hover{background:var(--sheet)}
.rhit .w{display:block;font-family:var(--mono);font-size:10.5px;color:var(--accent);margin-bottom:5px}
.rhit .t{display:block;font-family:var(--serif);font-weight:600;font-size:15px;margin-bottom:4px}
.rhit .x{display:block;font-size:12.5px;color:var(--muted);line-height:1.6}
.rhit mark{background:var(--accent-soft);color:var(--accent-ink);padding:0 2px;border-radius:2px}
.rnone{color:var(--muted);font-size:14px;padding:20px 4px}
#results h3{font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:var(--muted);font-weight:600;margin-bottom:6px}

@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
'''

JS = r'''
(function(){
  var BK = JSON.parse(document.getElementById('data').textContent);
  var nav = document.getElementById('nav'), body = document.getElementById('body');
  var reader = document.getElementById('reader'), results = document.getElementById('results');
  var q = document.getElementById('q'), books = document.getElementById('books');
  var bk = 0, cur = 0, io = null, seq = 0, showSeq = 0;
  var STORE = '@@STORE@@';
  function save(k,v){ try{ localStorage.setItem(STORE+k,v);}catch(e){} }
  function load(k){ try{ return localStorage.getItem(STORE+k);}catch(e){ return null; } }
  function esc(s){ return s.replace(/[&<>]/g, function(m){ return {'&':'&amp;','<':'&lt;','>':'&gt;'}[m]; }); }
  function tok(n){ return getComputedStyle(document.documentElement).getPropertyValue(n).trim(); }

  // 书切换
  if (BK.length > 1){
    books.hidden = false;
    BK.forEach(function(b, ix){
      var x = document.createElement('button');
      x.className = 'bk'; x.type = 'button'; x.textContent = b.name;
      x.addEventListener('click', function(){ show(ix, 0); });
      books.appendChild(x);
    });
  }

  function buildNav(){
    nav.innerHTML = '';
    BK[bk].chapters.forEach(function(c, ix){
      var b = document.createElement('button');
      b.className = 'chap'; b.type = 'button'; b.dataset.ix = ix;
      b.innerHTML = '<span class="i"></span><span class="t"></span><span class="s"></span>';
      b.querySelector('.i').textContent = c.label.replace('第 ','').replace(' 章','').replace('附录 ','附');
      b.querySelector('.t').textContent = c.title;
      b.querySelector('.s').textContent = c.sub || '';
      b.addEventListener('click', function(){ show(bk, ix); });
      nav.appendChild(b);
      var ul = document.createElement('ul'); ul.className = 'subtoc'; ul.dataset.ix = ix;
      c.toc.forEach(function(t){
        var li = document.createElement('li'), a = document.createElement('a');
        a.href = '#' + t[2]; a.textContent = t[1]; if (t[0] >= 3) a.className = 'lv3';
        a.addEventListener('click', function(ev){
          ev.preventDefault(); var el = document.getElementById(t[2]);
          if (el) el.scrollIntoView({block:'start'});
        });
        li.appendChild(a); ul.appendChild(li);
      });
      nav.appendChild(ul);
    });
    Array.prototype.forEach.call(books.querySelectorAll('.bk'), function(x, ix){ x.classList.toggle('on', ix === bk); });
  }

  function spy(){
    if (io) io.disconnect();
    var tocEl = nav.querySelector('.subtoc[data-ix="'+cur+'"]'); if (!tocEl) return;
    var links = {};
    Array.prototype.forEach.call(tocEl.querySelectorAll('a'), function(a){ links[a.getAttribute('href').slice(1)] = a; });
    var heads = body.querySelectorAll('h1[id],h2[id],h3[id]');
    if (!heads.length || !('IntersectionObserver' in window)) return;
    io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (!e.isIntersecting) return;
        Array.prototype.forEach.call(tocEl.querySelectorAll('a'), function(a){ a.classList.remove('here'); });
        var a = links[e.target.id]; if (a) a.classList.add('here');
      });
    }, {rootMargin:'-12% 0px -72% 0px'});
    Array.prototype.forEach.call(heads, function(h){ io.observe(h); });
  }

  // mermaid：自己渲染，颜色取当前主题的 token
  function mmdInit(){
    if (!window.mermaid) return false;
    try {
      window.mermaid.initialize({startOnLoad:false, securityLevel:'strict', theme:'base',
        fontFamily: tok('--sans'),
        themeVariables:{ primaryColor: tok('--sheet'), primaryBorderColor: tok('--rule-2'),
          primaryTextColor: tok('--ink'), lineColor: tok('--muted'), textColor: tok('--ink-2'),
          secondaryColor: tok('--sheet-2'), tertiaryColor: tok('--paper'),
          edgeLabelBackground: tok('--paper'), fontSize:'14px' },
        flowchart:{ htmlLabels:true, curve:'basis', padding:8, nodeSpacing:30, rankSpacing:38, wrappingWidth:118 }});
      return true;
    } catch(e){ return false; }
  }
  function drawDiagrams(root){
    var figs = root.querySelectorAll('figure.mmd');
    if (!figs.length) return Promise.resolve();
    var ok = mmdInit();
    var defs = '\n  classDef hl fill:' + tok('--accent-soft') + ',stroke:' + tok('--accent') + ',color:' + tok('--accent-ink') + ',stroke-width:1.5px;'
             + '\n  classDef warn fill:' + tok('--warn-soft') + ',stroke:' + tok('--warn') + ',color:' + tok('--warn') + ';';
    return Array.prototype.reduce.call(figs, function(p, f){
      return p.then(function(){
        var src = f.querySelector('.mmd-src').textContent, out = f.querySelector('.mmd-out');
        // 菱形判断节点会随标签变得很大，改画六边形（仍然读作判断，面积约一半）
        src = src.replace(/(\b[A-Za-z_]\w*)\{"([^"{}]*)"\}/g, '$1{{"$2"}}');
        if (!ok){ out.innerHTML = '<pre class="code"><code>' + esc(src) + '</code></pre>'; f.dataset.err = 'nolib'; return; }
        function fit(){
          // 宽图缩到栏宽会让字小到看不清：LR 缩得太狠就改成 TD 重画；最小只缩到 85%，再宽就横向滚动
          var svg = out.querySelector('svg'); if (!svg) return;
          var vb = svg.viewBox && svg.viewBox.baseVal, nat = vb && vb.width ? vb.width : svg.getBoundingClientRect().width;
          var room = out.clientWidth - 28;
          svg.style.maxWidth = 'none'; svg.style.width = Math.min(nat, Math.max(room, nat * 0.85)) + 'px'; svg.style.height = 'auto';
          return nat / Math.max(room, 1);
        }
        return window.mermaid.render('geo-m' + (++seq), src + defs).then(function(r){
          out.innerHTML = r.svg; f.dataset.ok = '1';
          var ratio = fit();
          if (ratio > 1.25 && /^\s*flowchart\s+LR/.test(src)) {
            var td = src.replace(/^(\s*flowchart\s+)LR/, '$1TD');
            return window.mermaid.render('geo-m' + (++seq), td + defs).then(function(r2){
              out.innerHTML = r2.svg; f.dataset.flip = 'TD'; fit();
            });
          }
        }).catch(function(e){
          out.innerHTML = '<pre class="code"><code>' + esc(src) + '</code></pre>';
          f.dataset.err = (e && e.message ? e.message : String(e)).slice(0, 200);
          if (window.console) console.warn('[geo-mmd]', f.dataset.err);
        });
      });
    }, Promise.resolve());
  }
  function redraw(){ drawDiagrams(body); }
  if (window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    if (mq.addEventListener) mq.addEventListener('change', redraw);
  }
  new MutationObserver(redraw).observe(document.documentElement, {attributes:true, attributeFilter:['data-theme']});


  // 下载整本书为一个 .md（viewer 会弹确认；不能用就不显示按钮）
  var dlBox = document.getElementById('dl'), dlBtn = document.getElementById('dlb'), dlSt = document.getElementById('dls');
  var dlApi = null;
  function bookMd(b){
    var head = '# ' + b.full + '\n\n> Canlah · 2026-09-23 · ' + b.tag + '\n';
    return head + b.chapters.map(function(c){ return '\n\n' + c.md; }).join('') + '\n';
  }
  function dlLabel(){ dlBtn.textContent = '下载' + BK[bk].name + '（.md）'; dlSt.textContent = ''; }
  if (window.claude && typeof window.claude.use === 'function') {
    window.claude.use('downloads').then(function(d){
      if (!d) return;
      dlApi = d; dlBox.hidden = false; dlLabel();
    }).catch(function(){});
  }
  dlBtn.addEventListener('click', function(){
    if (!dlApi) return;
    var b = BK[bk];
    dlSt.textContent = '';
    dlApi.save({filename: 'GEO-Playbook-' + b.name + '-2026-09-23.md', data: bookMd(b)}).then(function(){
      dlSt.textContent = '已保存';
    }).catch(function(e){
      var c = e && e.code;
      if (c === 'declined') return;
      if (c === 'rate_limited') { dlSt.textContent = '上一个保存窗口还开着，关掉后再点一次。'; return; }
      dlSt.textContent = '这里没法保存文件。'; if (c === 'unavailable' || c === 'not_granted') dlBox.hidden = true;
    });
  });

  function show(b, ix, anchor){
    var bookChanged = b !== bk || !nav.children.length;
    bk = b; cur = ix;
    if (bookChanged) { buildNav(); if (dlApi) dlLabel(); }
    var c = BK[bk].chapters[ix];
    document.getElementById('cn').textContent = BK[bk].name + ' · ' + c.label;
    document.getElementById('ct').textContent = c.title;
    document.getElementById('cs').textContent = c.sub || '';
    document.getElementById('btag').textContent = BK[bk].tag;
    body.innerHTML = c.html;
    Array.prototype.forEach.call(nav.querySelectorAll('.chap'), function(x){ x.classList.toggle('on', +x.dataset.ix === ix); });
    Array.prototype.forEach.call(nav.querySelectorAll('.subtoc'), function(u){ u.classList.toggle('open', +u.dataset.ix === ix); });
    var chs = BK[bk].chapters, p = document.getElementById('prev'), nx = document.getElementById('next');
    p.hidden = ix === 0; nx.hidden = ix === chs.length - 1;
    if (!p.hidden) p.querySelector('.t').textContent = chs[ix-1].title;
    if (!nx.hidden) nx.querySelector('.t').textContent = chs[ix+1].title;
    results.hidden = true; reader.hidden = false;
    save('bk', String(bk)); save('ch', String(ix));
    var el = anchor && document.getElementById(anchor);
    if (el) el.scrollIntoView({block:'start', behavior:'instant'}); else window.scrollTo(0,0);
    var mine = ++showSeq;
    // 图是异步画的，画完会把下面的内容往下推；画完后再对一次锚点
    drawDiagrams(body).then(function(){
      if (el && mine === showSeq) el.scrollIntoView({block:'start', behavior:'instant'});
    });
    spy();
  }

  body.addEventListener('click', function(ev){
    var a = ev.target.closest ? ev.target.closest('a.xref[data-xbook]') : null;
    if (!a) return;
    ev.preventDefault();
    var b = -1;
    BK.forEach(function(x, ix){ if (x.key === a.dataset.xbook) b = ix; });
    if (b < 0) return;
    show(b, +a.dataset.xch || 0, a.dataset.xid);
  });
  document.getElementById('prev').addEventListener('click', function(){ if (cur > 0) show(bk, cur-1); });
  document.getElementById('next').addEventListener('click', function(){ if (cur < BK[bk].chapters.length-1) show(bk, cur+1); });

  // 搜索：两本书一起搜
  var flat = [];
  BK.forEach(function(b, bi){
    b.chapters.forEach(function(c, ci){
      var d = document.createElement('div'); d.innerHTML = c.html;
      Array.prototype.forEach.call(d.querySelectorAll('.mmd-src'), function(x){ x.remove(); });
      var nodes = d.querySelectorAll('h1[id],h2[id],h3[id]');
      for (var i = 0; i < nodes.length; i++){
        var txt = '', n = nodes[i].nextSibling;
        while (n && !(n.nodeType === 1 && /^H[1-3]$/.test(n.tagName))){ txt += (n.textContent || '') + ' '; n = n.nextSibling; }
        flat.push({bi:bi, ci:ci, id:nodes[i].id, title:nodes[i].textContent.trim(), text:txt.replace(/\s+/g,' ')});
      }
    });
  });
  function search(term){
    term = term.trim();
    if (term.length < 2){ results.hidden = true; reader.hidden = false; return; }
    var t = term.toLowerCase(), hits = [];
    for (var i = 0; i < flat.length && hits.length < 60; i++){
      var s = flat[i], hay = (s.title + ' ' + s.text).toLowerCase(), p = hay.indexOf(t);
      if (p < 0) continue;
      var raw = s.title + ' ' + s.text, from = Math.max(0, p - 45);
      hits.push({s:s, snip:(from > 0 ? '…' : '') + raw.substr(from, 150) + '…'});
    }
    var h = '<h3>' + hits.length + ' 处命中' + (hits.length >= 60 ? '（只显示前 60 处）' : '') + '</h3>';
    if (!hits.length) h += '<p class="rnone">没找到「' + esc(term) + '」。换个词试试。</p>';
    var re = new RegExp(term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'ig');
    hits.forEach(function(x){
      var ch = BK[x.s.bi].chapters[x.s.ci];
      h += '<button class="rhit" type="button" data-bi="' + x.s.bi + '" data-ci="' + x.s.ci + '" data-id="' + x.s.id + '">'
        + '<span class="w">' + esc(BK[x.s.bi].name + ' · ' + ch.label + ' · ' + ch.title) + '</span>'
        + '<span class="t">' + esc(x.s.title) + '</span>'
        + '<span class="x">' + esc(x.snip).replace(re, function(m){ return '<mark>' + m + '</mark>'; }) + '</span></button>';
    });
    results.innerHTML = h; results.hidden = false; reader.hidden = true;
    Array.prototype.forEach.call(results.querySelectorAll('.rhit'), function(b){
      b.addEventListener('click', function(){ q.value = ''; show(+b.dataset.bi, +b.dataset.ci, b.dataset.id); });
    });
  }
  var timer;
  q.addEventListener('input', function(){ clearTimeout(timer); timer = setTimeout(function(){ search(q.value); }, 160); });
  q.addEventListener('keydown', function(e){ if (e.key === 'Escape'){ q.value = ''; search(''); } });

  var sb = parseInt(load('bk'), 10), sc = parseInt(load('ch'), 10);
  if (!(sb >= 0 && sb < BK.length)) sb = 0;
  if (!(sc >= 0 && sc < BK[sb].chapters.length)) sc = 0;
  show(sb, sc);
})();
'''

HTML = '''<title>@@TITLE@@</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700&family=Noto+Sans+SC:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>@@CSS@@</style>
<div class="wrap">
  <aside>
    <div class="brand">
      <div class="kicker">Canlah · 2026-09-23</div>
      <h1>GEO Playbook</h1>
      <p class="tag" id="btag"></p>
    </div>
    <div class="books" id="books" hidden></div>
    <div class="dl" id="dl" hidden><button class="dlb" id="dlb" type="button">下载这本书（.md）</button><div class="dls" id="dls" role="status"></div></div>
    <div class="searchbox"><input id="q" type="search" placeholder="搜全书…" autocomplete="off" aria-label="搜索全书"></div>
    <nav id="nav" aria-label="章节"></nav>
  </aside>
  <main>
    <div id="results" hidden></div>
    <div id="reader">
      <div class="sheet">
        <div class="chead"><div class="n" id="cn"></div><h2 id="ct"></h2><div class="s" id="cs"></div></div>
        <article id="body"></article>
      </div>
      <div class="pager">
        <button class="pbtn prev" id="prev" type="button" hidden><span class="d">上一章</span><span class="t"></span></button>
        <button class="pbtn next" id="next" type="button" hidden><span class="d">下一章</span><span class="t"></span></button>
      </div>
    </div>
  </main>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/11.15.0/mermaid.min.js"></script>
<script type="application/json" id="data">@@DATA@@</script>
<script>@@JS@@</script>
'''
out = HTML.replace('@@TITLE@@', TITLE).replace('@@CSS@@', CSS).replace('@@JS@@', JS.replace('@@STORE@@', STORE)).replace('@@DATA@@', payload)
path = '%s/geo-%s.html' % (S, name)
open(path, 'w').write(out)
print('已生成', path, len(out), '字符')
