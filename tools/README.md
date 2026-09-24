# Build tools · 构建工具

These scripts build the GEO Playbook from its Markdown source into the website pages, the quick-guide slides (PDF / PPTX) and the site data files. They are published so the build is inspectable and reusable. **The book source itself (the `general/` and `dental/` chapter files) is not in this repository**: the full text lives only on the website, https://canlah.ai/zh/playbook/ .

这些脚本把《GEO Playbook》的 Markdown 书稿构建成官网页面、轻量版幻灯片（PDF / PPTX）和站点数据。公开出来是为了让构建过程可查、可复用。**书稿本身（`general/`、`dental/` 各章）不在本仓库**，完整正文只放官网。

License: MIT (see `../LICENSE-CODE`). The book content is CC BY 4.0 (see `../LICENSE`).

## Expected layout · 目录约定

The scripts treat the parent of `tools/` as the book root. Override it with the `GEO_V3` environment variable.

```
<book root>/
├── general/        # general edition, one .md per chapter (g0.md … gD.md)
├── dental/         # dental & aesthetics edition (d0.md … dB.md)
├── guide/          # quick guide source: en.md, zh.md
├── tools/          # these scripts
├── _build/         # output: single-file HTML, JSON, PDF, PPTX
└── _site/          # output: static chapter HTML, manifest.json, geo-book.css, downloads/
```

Note: the quick-guide source (`guide/en.md`, `guide/zh.md`) is not in this repository either. `build_guide.py` expects it under `<book root>/guide/`, with a `[QR]` line where the QR page goes.

## Scripts · 脚本

| Script | What it does |
|---|---|
| `lint_v3.py <chapter.md>` | Checks one chapter: diagram fences, `@include` targets, cross-book links, table column counts |
| `build_v3.py general` / `build_v3.py dental general` | Chapters → one JSON + single-file HTML. Diagram fences supported: `wireframe`, `mermaid`, `bars`, `steps`, `split`. With `GEO_PUBLIC=1`, anything between `<!-- internal -->` and `<!-- /internal -->` is removed and internal-only files are skipped |
| `emit_v3.py general` / `emit_v3.py dental-general` | JSON → reader app HTML (search, chapter nav, light/dark) |
| `build_guide.py en` / `build_guide.py zh` | `guide/<lang>.md` → 16:9 slides as HTML, PDF and PPTX, plus the JSON used by the website's quick-guide page |
| `emit_site.py` | Runs the public builds, pre-renders every mermaid diagram to inline SVG in a headless browser (so crawlers that do not execute JavaScript still see the diagrams), rewrites cross-chapter links to real site URLs, writes `_site/manifest.json`, `geo-book.css` (scoped under `.geo-book`) and the downloads, then runs a leak check |

```bash
cd tools
python3 lint_v3.py ../general/g5-0.md
python3 build_v3.py general && python3 emit_v3.py general
python3 build_v3.py dental general && python3 emit_v3.py dental-general
python3 build_guide.py en     # needs: pip install playwright python-pptx qrcode pillow && playwright install chromium
python3 emit_site.py          # needs: playwright (same as above)
```

## Leak check · 泄漏检查

`emit_site.py` fails loudly (prints a warning) if a public page contains a local file path, a scratch directory name, or an unstripped `<!-- internal` marker. To add your own banned words (for example names that must not appear in public material), put them one per line in `tools/leak-words.txt` (keep that file out of version control) or pass them comma-separated in `GEO_LEAK_WORDS`.

`emit_site.py` 发现公开页里有本机路径、临时目录名或没剔掉的 `<!-- internal` 标记就报警。要加自己的禁用词（例如公开材料里不许出现的名字），每行一个写进 `tools/leak-words.txt`（不要提交进版本库），或用逗号分隔写进环境变量 `GEO_LEAK_WORDS`。
