# Page types · 46 种被引页型

Condensed from GEO Playbook chapter 5 (5.1, 5.11–5.30, B.5). Each entry: the buyer intent it answers, which AI engine mainly cites it, the side limits, and the block order from top to bottom, with the blocks AI most often copies marked. Full blueprints with diagrams and examples (Chinese) are linked on every entry. Index: https://canlah.ai/zh/playbook/write-pages/#g5-5-1-页型总图-46-种-六个家族-三档证据-三侧开放

## How to read this file

**Evidence tier** — **A**: round 1, measured on both ChatGPT and Google AI Mode (9 types). **B**: round 2, measured on ChatGPT only; AI Mode was not run because the probe quota ran out, so "not measured on AI Mode" does not mean "AI Mode does not cite it" (33 types). **C**: seen only in an external teardown, not measured by us (4 types, pt43–pt46). Lengths are English word counts of the cited pages we saw; they are a reference, not a target. Length is set by page type: write until the job is done, then stop.

**Where the count comes from**: 9 (round 1) + 33 (round 2) + 5 from an external teardown − 1 merged duplicate = 46. Two pages are the same type only if all three hold: the triggering questions belong to one family; the quoted sentence sits in the same place and form; one blueprint can produce both. The number grows as more kinds of question are tested.

**Side limits** use four values: **build** (may self-build) · **adapt** (build after rewriting) · **cite** (only quote it downstream or fill in your own row) · **stop** (do not do). Unregulated businesses may build every type unless noted. "E→" is what changes when switch E (peer comparison banned) is on. Rules: [sides-and-compliance.md](sides-and-compliance.md).

**Block marks**: `[req]` required · `[opt]` optional · `★` the block AI most often copies · `⚖` side rules apply to this block · `✗` never do this. Blueprints marked *not measured* carry no ★.

**Two sentence types on every page** (5.6): an *own sentence* for ChatGPT (subject is the business; exact price or spec, unit, defining condition, tax basis) and a *market sentence* for AI Mode (a range, 3–4 drivers, source and date: "<scope> generally ranges from $X to $Y, depending on A, B, C"). Strictly regulated sites and switch E replace the market sentence with an official-basis sentence.

**Rules that hold for every type** (5.7): the first sentence of every paragraph stands alone; core facts in the first 30% of the page; tables wherever facts fit a table, with column headers in the buyer's comparison words; title carries the year if the content changes by year (not on official pricing pages); H1 is a statement, the first H2 is the main question, other H2s are statements with the verdict in the heading, questions go in FAQ H3s; FAQ restates the body, it is rarely the quoted source; numbers are exact with unit, basis and date; prices, results and specs are in the initial HTML (not JS, images or IP-based variants).

---

## Price family · 价格类 (8)

### pt01 · Single-service price page 单项目价格页
- **Intent**: the buyer has chosen a service and asks what it costs. One URL per service, same template.
- **Cited by**: tier A, mainly ChatGPT · 62–1,609 words.
- **Sides**: strict build (fixed final price only) · light build (ranges need scope and exclusions).
- **Blocks**:
  1. H1 — statement with year `[req]`
  2. Byline / date line — named reviewer + month/year, or "Rate card reviewed <month year>" `[opt]`
  3. Own-price sentence — 1–3 sentences, 40–130 words, number first `[req] ★ ⚖`
  4. Price table — right after: tier + defining condition + price + inclusions `[req] ★ ⚖`
  5. H2 tier criteria — first sentence gives the basis, one number per tier `[opt]`
  6. Included / extra table — Item / Fee / Notes `[opt]`
  7. H2 subsidies and payment — standalone fact section, separate from the price table `[opt]`
  8. H2 alternatives — first sentence states both own prices; a market sentence may go here `[opt]`
  9. FAQ — restate the billing rules in full sentences `[opt]`
  10. Links to related price pages `[opt]`
- **Common mistake**: price only in an image, booking widget or JS toggle. Ctrl+F the price in the page source before publishing.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-core/#g6-5-11-单项目价格页-pt01

### pt02 · Price guide page 价格指南页 (always the first page)
- **Intent**: "how much does <category> cost in <city>". Every product the business sells in one table.
- **Cited by**: tier A, both engines, AI Mode more · 900–2,000 words. Price questions trigger AI Overviews most often; locally cited price guides are mostly written by the providers themselves.
- **Sides**: strict adapt (no peer ranges; official benchmark in its own section) · light build (market range only as a sourced standalone section; E→ no peer range, use official-basis and procedure-variable sentences).
- **Blocks**:
  1. title — `<Category> Cost in Singapore (<year>): <price hook>` `[req]`
  2. H1 — statement with year; the Chinese version names the country `[req]`
  3. Byline / date line `[opt]`
  4. Conclusion block — 40–130 words: own sentence + market sentence `[req] ★ ⚖`
  5. Data basis line — one line above the table: sample, source or check date `[opt]`
  6. H2 main price question — "How Much Does <Category> Cost?" `[req]`
     - first sentence: "At <Brand>, <category> costs S$X (incl. GST)" `[req] ⚖`
     - price grid table: <type> / Cost / Suitable for, one number per cell `[req] ★ ⚖`
  7. Official public benchmark — own section with table number and update date; on the strict side no own price inside it `[opt] ⚖`
  8. H2 factors that affect the price — first sentence is the market sentence; 3–5 factors, each a numbered H3 `[opt] ⚖`
  9. H2 subsidies, insurance and tax — standalone; government figures with table number and date `[opt]`
  10. H2 included and not included — 4–8 items `[opt]`
  11. FAQ — 5–12 questions, 40–60 words each `[opt]`
  12. Related price pages + one CTA `[opt]`
- **Hard specs**: all products in one table; H1 carries the year and is refreshed each quarter (update `dateModified`); English and Chinese versions finished together; at least five checkable facts found nowhere else.
- **Common mistake**: the summary only warms up, or its numbers differ from the table. When the top cards and the table disagree, AI uses the table.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-core/#g6-5-12-价格指南页-一-为什么第一页永远是它-pt02 · https://canlah.ai/zh/playbook/page-types-core/#g6-5-13-价格指南页-二-施工图-列头-句子-pt02

### pt03 · Official pricing page /pricing 官方定价页
- **Intent**: "how much is <product>", plans and tiers of a product with public list prices.
- **Cited by**: tier A, mainly ChatGPT (27/31 citations) · 1,691–8,265 words.
- **Sides**: strict stop → pt01 · light adapt (with switch B: a course/product price page, names verbatim from the official approval; E→ stop, use pt01).
- **Blocks**:
  1. H1 — noun phrase, no year `[req]`
  2. Billing toggle — annual / monthly, both prices in the HTML `[req]`
  3. Row of price cards — right under H1: plan + price + unit + who it is for + key capability `[req] ★`
  4. Free tier limits and minimums — free tier cap, minimum seats on paid tiers `[req]`
  5. Tax and currency footnote — "prices exclude tax"; billing country sets the currency `[req] ★`
  6. Enterprise card — the four no-public-price sentences under the button (not measured) `[opt]`
  7. Add-ons table — Add-on / Price / Unit `[opt]`
  8. Feature comparison table — Feature / <tier 1> / <tier 2> `[opt]`
  9. Market sentence — your own product's range and drivers, never competitor prices `[opt]`
  10. FAQ — billing rules as full sentences `[opt]`
- **Common mistake**: only a slogan and "Contact sales" under H1; price cards appear only after a click or JS.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-core/#g6-5-14-官方定价页-pt03

### pt17 · Subsidy and limit rules page 补贴与限额规则页
- **Intent**: "how do I claim X", "how much do I pay after the subsidy".
- **Cited by**: tier B, ChatGPT · about 1,600 words.
- **Sides**: official version is cite-only on every side · own version: strict adapt (subsidy only as a standalone fact section, never beside your price) · light build.
- **Blocks**:
  1. H1 — full scheme name with abbreviation `[req]`
  2. Summary + update date — update date on the first screen, not the footer `[req]`
  3. Three or four H2 questions — what it is / benefits / who is eligible / how to use `[req]`
  4. Item-by-item limit table — one row per item + cap amount `[req] ★`
  5. Old and new tables side by side — when limits change `[opt]`
  6. Eligibility table — which group can use which tier `[req]`
  7. Numbered claim steps — download → fill → submit `[opt]`
  8. Own three-column table — item / cap / you pay (not on the strict side) `[opt] ⚖`
- **Common mistake**: building a subsidy calculator. Give the number AI cannot compute: your actual price after your own coding.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-21-1-补贴与限额规则页-pt17

### pt27 · Parameter and rate basis page 参数口径页
- **Intent**: "how much will I pay in my situation", "X calculator", "monthly cost". Used as a calculation input, not for price comparison.
- **Cited by**: tier B, ChatGPT · 150–503 words.
- **Sides**: strict adapt (fixed final tax-inclusive values, no ranges) · light build.
- **Blocks**:
  1. title — the question itself, or category + region `[req]`
  2. Basis sentence — who sets the rate, how often it changes `[req]`
  3. Current value, paired — pre-tax and tax-inclusive in one sentence `[req] ★`
  4. Period table — parameter / current value / effective period `[req]`
  5. Current value sentence — what it is now and since when `[req] ★`
  6. Formula and worked example — three-column example (not measured) `[opt]`
  7. H2 units — unit and average usage `[opt]`
  8. Everything in static HTML — numbers remain with JS off `[req]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-21-2-参数口径页-pt27

### pt37 · Category list page 品类列表页
- **Intent**: the "which brands are there, from how much to how much" part of complete-guide questions.
- **Cited by**: tier B, ChatGPT · about 885 words.
- **Sides**: strict stop → own service catalogue · light adapt (own catalogue, names as registered; E→ stop).
- **Blocks**:
  1. title — category synonyms + audience + site name `[req]`
  2. H1 — a selling line is fine; it is not quoted `[opt]`
  3. Product count + price endpoints — "N products", lowest and highest price `[req] ★`
  4. Brand wall — each brand name as a text item `[req] ★`
  5. Type filters — each type name as a text item `[req]`
  6. Bottom description — one or two H2s, not a quote source `[opt]`
  7. ✗ count, prices and brands only inside JS facets
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-21-3-品类列表页-pt37

### pt38 · Calculator page 计算器页
- **Intent**: "how do I calculate my X", "which tier does <score> get", "X calculator".
- **Cited by**: tier B, ChatGPT · 2,500–3,000 words.
- **Sides**: strict adapt (process estimate only, output is never a price promise) · light build (E→ "subject to formal engagement", no peer prices).
- **Blocks**:
  1. title = H1 — tool name + year + what it computes + site name `[req]`
  2. Tiered conclusion on the first screen — one sentence with numbers: tier A → X, tier B → Y `[req] ★ ⚖`
  3. Calculator widget — JS; cited 0 times, do not invest `[opt]`
  4. Static lookup table — every result pre-computed `[req] ★`
  5. FAQ — 5 questions restating the method `[opt]`
  6. Method sentence — how it adds up, what the range is `[req]`
- **Test**: with JS off, a tiered conclusion sentence and a static table remain.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-21-4-计算器页-pt38

### pt42 · Time-limited promotion page 限时促销页
- **Intent**: when answering "is this business any good", AI looks for its current actual prices.
- **Cited by**: tier B, ChatGPT · length not captured (page blocked).
- **Sides**: strict stop (explicit) → pt01 · light build (with switch B, full validity period and conditions).
- **Blocks** (only three things verified):
  1. One URL per promotion — numbered, one page each `[req]`
  2. Fixed nett price + scope — one sentence: bundle content, price, participating outlets `[req] ⚖`
  3. Under a news section — URL path checkable `[req]`
  4. title, H1 and other blocks — not captured; do not guess `[opt]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-21-5-限时促销页-pt42

---

## Selection and reputation family · 选择与口碑类 (8)

### pt04 · Comparison page (A vs B) 对比页
- **Intent**: "A or B", "X vs Y", "X alternatives". Organise by scenario, not by candidate.
- **Cited by**: tier A, AI Mode (ChatGPT only 3/20) · about 1,200 words (brand-written) / 4,000 (media).
- **Sides**: strict adapt (compare options, not institutions) · light adapt (options and delivery formats, not institutions; E→ procedures only, explicit). Unregulated: must include competitors, same basis, sourced, check date.
- **Blocks**:
  1. title / H1 — title is a question, H1 a statement, both with year `[req]`
  2. Comparison basis line — check date + versions or plans compared `[req]`
  3. Conclusion block — 60–120 words, or a verdict-by-scenario table `[req] ★ ⚖`
  4. H2 main question — first sentence is a conditional verdict, followed by a scenario table `[req] ★`
  5. H2 criteria — numbered H3s, each first sentence states the tipping threshold `[opt]`
  6. Master comparison table — in the first 25%, one checkable value per cell `[req] ⚖`
  7. H2 per criterion × N — winner in the heading, first sentence repeats it with a number `[opt]`
  8. H2 price comparison — same tier, currency and billing period `[opt]`
  9. H2 when the other option fits better — at least 2 concrete scenarios, each with a public fact about the other `[req]`
  10. H2 skip it if… `[opt]`
  11. Sources and dates — source + check date for every data point `[req]`
  12. FAQ — H3 questions, first sentence answers `[opt]`
  13. Links to related comparisons — 3–5 `[opt]`
- **Common mistake**: background first and the verdict in the middle, so only the middle sentence is quoted. On regulated sides, comparing institutions instead of options is a violation, not a layout issue.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-core/#g6-5-15-对比页-pt04

### pt05 · List page (Best X for Y) 榜单页
- **Intent**: "best X for Y", "top X in <city>".
- **Cited by**: tier A, AI Mode (ChatGPT about 6/29) · 2,100–9,000 words. For "which one is best" questions, neither engine cited list pages that a business wrote about itself; the main lever for those questions is off-site.
- **Sides**: strict stop (ranking is comparison) · light stop (conservative line; written reasons from the client can relax it; E→ stop) · unregulated build, with disclosure if you rank yourself first.
- **Blocks**:
  1. title / H1 — year; method or check date in title or first screen `[req]`
  2. Author, date, check date line — all three `[req]`
  3. Conclusion paragraph — before any H2, names the top pick and budget pick `[req] ★`
  4. First H2 + summary table — repeats the verdict, table in the first 20% `[req]`
  5. Table of contents `[opt]`
  6. Methodology — How we tested / How we picked `[req]`
  7. Interest disclosure — mandatory if you rank yourself first `[req] ⚖`
  8. One H2 per entry — "<Name>: Best for <scenario>" `[req] ★`
  9. How to choose — criteria H2, links to official standards `[opt]`
  10. What changed since last time — 3–6 items `[opt]`
  11. Data sources — source and date for every price and spec `[opt]`
  12. FAQ — restate the top verdict `[opt]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-core/#g6-5-16-榜单页-pt05

### pt24 · Third-party single-business review 第三方单机构测评页
- **Intent**: "is <business> good", "<model> review", "is it worth it". Specs come from the product page; subjective pros and cons only from this type.
- **Cited by**: tier B, ChatGPT · 1,200–5,000 words.
- **Sides**: strict stop · light stop (both conservative line) · unregulated build.
- **Blocks**:
  1. Byline + update date `[req]`
  2. Cost summary table — <tier> / estimated monthly fee, in the first 25% `[req] ★`
  3. Pros — one sentence each, 4–8 `[req]`
  4. Cons — one sentence each, the negatives the official site will not write `[req] ★`
  5. Comparison table — feature / competitor / this option `[opt]`
  6. Short conversational H2s — each carries one quotable judgement `[opt]`
  7. Verdict paragraph — strong and weak scenarios `[req]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-22-1-第三方测评页-pt24

### pt25 · Sentiment, forum and news pages 舆情·论坛·新闻报道页 (defensive)
- **Intent**: the negative side of "is this business good". You cannot build it, but it caps what your own pages can do.
- **Cited by**: tier B, ChatGPT · length varies.
- **Sides**: no side may self-build. Only add facts; never respond with comparisons or counter-testimonials.
- **What AI reads** (observed): news H1 is an event sentence (party + business + amount); Reddit H1 is the original question; forum threads carry page numbers in the URL; each post = username + timestamp + text + reply count; AI reads deep into later thread pages, not only page one.
- **Common mistake**: paying for brand-polish content. None of it reached an answer; checkable numbers and forum quotes did.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-22-2-舆情-论坛-新闻报道页-pt25

### pt28 · Review aggregate page 评价聚合页
- **Intent**: "is <business> good", "<brand> reviews". Explains the half of "which is best" citations you do not control; can be generated per branch.
- **Cited by**: tier B, ChatGPT · 800–2,200 words.
- **Sides**: strict stop (ratings are testimonials, explicit) · light adapt (testimonials with name, relationship, year; E→ stop).
- **Blocks**:
  1. Rating widget on the first screen — score + N reviews + category, no preamble `[req] ★`
  2. Sub-score table `[opt]`
  3. Business facts — phone, email, address `[req]`
  4. Opening hours table — day + hours + status `[req]`
  5. FAQ restating the score `[opt]`
  6. Paginated review stream — name, date, stars, text `[opt]`
  7. schema — AggregateRating + LocalBusiness, matching the visible values `[req]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-22-3-评价聚合页-pt28

### pt29 · Self-built reputation and credentials page 自建口碑与资质页
- **Intent**: "is <business> good". The only type you can build yourself for review-style questions.
- **Cited by**: tier B, ChatGPT · 2,300–75,000 words.
- **Sides**: strict stop (testimonials, stars, explicit) · light adapt (testimonials with name, relationship, year; E→ provable expertise, years in practice, third-party list years only).
- **Blocks**:
  1. Third-party media quote — one line + source `[opt]`
  2. Rating H2 — rating + denominator, its own H2 `[req] ★`
  3. Award lines — one award per line, consecutive years and each year listed `[req] ★`
  4. Per-person H3 — individual recognition `[opt]`
  5. Quantified claim with denominator — one sentence on the first screen `[req]`
- **Common mistake**: 150 testimonials. AI copies one or two quantified lines ("M of N + year + basis"); without that line the page scores zero.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-22-4-自建口碑与资质页-pt29

### pt41 · Verdict-first page 结论先行页
- **Intent**: "<model> review, is it worth it in <region>": value plus price and where to buy.
- **Cited by**: tier B, ChatGPT · about 2,436 words.
- **Sides**: strict stop (a verdict is a comparison, conservative line) · light adapt (scenario table only, no "best" or "best value"; E→ stop, but "boundary conditions in their own section" can be borrowed).
- **Blocks**:
  1. Dek — key numbers fixed, right under H1 `[req] ★`
  2. Primary sources referenced — sources first `[req]`
  3. The verdict — its own section `[req]`
  4. Key reasoning `[req]`
  5. Supporting facts — fact table `[req]`
  6. How to apply this `[opt]`
  7. What this actually means `[opt]`
  8. When this does NOT apply — own section; AI takes the limits along with the verdict `[req] ⚖`
  9. Closing: FAQ / key takeaways / disclaimer `[opt]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-22-5-结论先行页-pt41

### pt43 · Buyer's selection framework 买家选型框架页 (tier C)
- **Intent**: "how to choose a <provider type>". The strict side's only legal route onto the list shelf: criteria, no ranking, no names.
- **Cited by**: tier C, not measured (inferred to lean AI Mode) · 2,100–3,700 words in the teardown.
- **Sides**: strict adapt (delete the provider matrix and provider cards; keep dimensions, limits of diagnosis, RFP questions) · light build (E→ same as strict).
- **Blocks** (*not measured*):
  1. title — "How to Choose a <provider type> for <scope>" `[req]`
  2. Quick answer — 2–3 sentences, then a disclosure `[req]`
  3. H2 What does <thing> measure? — one strong sentence + 5–6 bold labels `[opt]`
  4. H2 What a useful <thing> should show — numbered 5–7, one sentence each `[opt]`
  5. H2 Research snapshot — what the status quo misses `[opt]`
  6. H2 Evaluation dimensions — five "label:" paragraphs, no bullets `[req]`
  7. H2 Provider comparison matrix — Provider / dimension 1 / dimension 2 / Best for `[opt] ⚖`
     - one card per provider, limits written as buyer tasks `[opt] ⚖`
  8. H2 How to interpret common results `[opt]`
  9. H2 How to run a defensible baseline — 5–10 imperative steps `[opt]`
  10. H2 What a free diagnosis cannot prove — 100–160 words `[req]`
  11. H2 Questions to put in the RFP — 8 full questions ending in "?" `[req]`
  12. H2 Final recommendation — when to switch from X to Y, 2 paragraphs `[opt]`
  13. FAQ + method and sources — 5–6 questions; at most 2 mention your own brand; one says "always confirm current scope with the vendor directly" `[req]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-checklist/#g8-pt43-买家选型框架页

---

## Questions and rules family · 问题与规则类 (12)

### pt06 · One question, one page 一问一页
- **Intent**: single questions with a definite answer: can I, must I, what is the cap, how long, who qualifies.
- **Cited by**: tier A; government versions mainly ChatGPT (20/23); business-written versions seen only in AI Mode, small sample · 40–1,500 words.
- **Sides**: strict build (general information, no case-by-case judgement; personal-safety symptom questions go to pt08) · light build (E→ no peer ranges in cost questions).
- **Blocks**:
  1. H1 — the buyer's question, word for word `[req]`
  2. Answer paragraph — first sentence Yes/No or a number, conditions in sentences 2–3, 40–90 words `[req] ★ ⚖`
  3. Boundary sentence — what cannot be decided online, and who decides `[opt]`
  4. Source line — source + check date `[req] ⚖`
  5. Own-fact paragraph — subheading "At <business>", 1–2 sentences of own facts `[opt]`
  6. Byline and date `[opt]`
  7. Related questions — 3–4, each on its own URL `[opt]`
- **Common mistake**: ten questions on one page, or an answer that starts "it depends".
- **Full spec**: https://canlah.ai/zh/playbook/page-types-core/#g6-5-17-一问一页-pt06

### pt07 · Eligibility and process page 资格流程页
- **Intent**: what conditions, how many visits, how long, how to apply, what to bring.
- **Cited by**: tier A, mainly ChatGPT (official versions 21/29) · 900–2,500 words.
- **Sides**: strict build (general conditions only; durations are process time, not outcome promises) · light build (quote statutory deadlines verbatim).
- **Blocks**:
  1. H1 — task-style statement `[req]`
  2. Byline and date — named reviewer for personal-safety topics; otherwise Last updated `[opt]`
  3. Conclusion block — five-cell spec strip + own sentence + market sentence `[req] ⚖`
  4. H2 main question — first sentence answers in ≤35 words `[req] ★`
     - step table: Step / Result, each row with time and number of visits `[req] ★`
  5. H2 conditions — numbered H3s, or a fact × explanation × when-it-applies table `[req]`
  6. H2 what to bring — 3–8 items `[opt]`
  7. H2 itemised fees — Item or service / Fees `[req]`
  8. H2 what cannot be decided online — 40–80 words `[opt] ⚖`
  9. H2 branches after assessment — four-column branch table; price cells hold a final price or "set after assessment" `[opt]`
  10. H2 risks and exceptions — general, never a personal diagnosis `[opt] ⚖`
  11. H2 alternatives — Option / When / Time / Price `[opt]`
  12. H2 who makes the final call — who and when, ≤50 words `[opt]`
  13. FAQ — H3 questions, 40–60 words each `[opt]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-core/#g6-5-18-资格流程页-pt07

### pt08 · Remedy and second-opinion page 补救与二次评估页
- **Intent**: "it went wrong, what now", "who do I complain to", "I want a second opinion". Pick one of two skeletons; never merge them.
- **Cited by**: tier A, both engines · 900–1,600 words.
- **Sides**: strict build (safety order must not move; no rescue rates, no blame, no before/after) · light build (E→ never criticise or assess the previous provider, explicit). The subject is the buyer's situation, never another provider's conduct.
- **Blocks — personal-safety type** (order fixed):
  1. H1 + byline — H1 states the situation; author and reviewer + date `[req]`
  2. What to do now — first-screen box: one definition + 3–4 actions `[req] ★`
  3. Red-flag table — If you notice / Do this / How soon, three levels `[req] ★ ⚖`
  4. Do not judge this yourself — 3–5 items `[req]`
  5. Assessment process — Step / What happens / Time + bring-list `[req]`
  6. Possible paths — conditional branch table; the first mention of "cause" is here `[req] ⚖`
  7. Itemised fees — assessment at a final price; treatment "confirmed in writing after assessment" `[req]`
  8. Complaint and regulator channels — only where there is harm or dissatisfaction `[opt]`
  9. Author bio + references — ≤100 words each `[req]`
  10. FAQ — 3–6 H3 questions `[opt]`
- **Blocks — rights-deadline type** (*not measured*): H1 + practitioner byline → urgent deadline table (Deadline / What it applies to / Source) → what we can and cannot take on → conflict check before any case details → documents to bring → scope of the second opinion (Covered / Not covered) → fee table (Service / Fee / Includes / Excludes) → no interference with the current engagement → FAQ.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-core/#g6-5-19-补救与二次评估页-pt08

### pt10 · Regulatory obligations and penalties page 监管义务与罚则页
- **Intent**: "is X legal", "what are the rules", "do I need to register", "what happens if I don't".
- **Cited by**: tier B, ChatGPT; the largest tier-B sample · 366–3,650 words.
- **Sides**: cite only on every side. Write a downstream summary: verbatim quote + link to the original + check date; schedule it as a trust page, not a traffic page.
- **Blocks** (as seen on cited source pages):
  1. H1 — the obligation as a noun phrase or a judgement, no year `[req]`
  2. Date line — Last updated inside the first screen, not the footer `[req]`
  3. Obligation sentence — directly under H1, 35–90 words: from <date> / who / must do what `[req] ★`
  4. Numbered requirement table — Number / Item description `[opt] ★`
  5. Penalty lines — one line per party: jail term + fine cap `[req]`
  6. H2s split by reader role, not by clause number `[opt]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-23-1-监管义务与罚则页-pt10

### pt12 · Definition page 定义词条页
- **Intent**: "what is X", "why do X", "how is X calculated"; reused as a fact source in checklists and guides. Generic consumer terms are in the model already: without a local variable (local law, standard number, local price), do not spend on this type.
- **Cited by**: tier B, ChatGPT · 200–2,875 words.
- **Sides**: strict build (named reviewer + date on personal-safety topics) · light build (cite clause numbers, no success rates).
- **Blocks**:
  1. Reviewer line — named reviewer + date, above the summary `[opt] ⚖`
  2. Summary — 100–150 words in fixed order: what it is / when it is needed / recovery time `[req]`
  3. One-sentence definition, twice — under H1 and again, identical, under the first H2 `[req]`
  4. Every H3 is a buyer question — What is / How painful / How long… `[req]`
  5. First sentence under each H3 is a conditional — "If <condition>, then <conclusion>" `[req] ★`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-23-2-定义词条页-pt12

### pt13 · Step-by-step procedure page 办事步骤页
- **Intent**: "how do I do X, step by step", "which documents do I submit".
- **Cited by**: tier B, ChatGPT · 650–2,600 words. Every quoted sentence came from a table cell; narrative paragraphs were never quoted.
- **Sides**: build on every side (own version: "how it works with us"; strict: subsidy steps in their own section).
- **Blocks**:
  1. H1 — starts with a verb + the track `[req]`
  2. Deliverable sentence — what this page gives you `[req]`
  3. Step table — Step / Result, deadlines inside the cells `[req] ★`
  4. Form table — document name / form number and source `[req] ★`
  5. Official fee table — Item or service / Fees `[req]`
  6. Channel H3s — online / in person `[opt]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-24-1-办事步骤页-pt13

### pt14 · Preparation and bring-list page 准备与携带清单页
- **Intent**: "what do I prepare before X", "what should I bring", "X checklist". Unstable: the same question can return zero or several citations; worth doing, do not expect it every time.
- **Cited by**: tier B, ChatGPT · 200–860 words.
- **Sides**: build on every side (strict: no "painless" or "quick recovery").
- **Blocks**:
  1. Timing sentence — at the top: when to start preparing `[req] ★`
  2. Document group — institution-specific names in full `[req]`
  3. Fasting or escort items — their own lines, never inside a paragraph `[req] ⚖`
  4. Reverse list — "we provide / you don't need to bring", two columns `[req] ★`
  5. Grouping — by role first, then by time, then a one-page checkbox list `[req]`
- **Common mistake**: listing only what to bring. "What we already provide" is the half competitors cannot copy.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-24-2-准备与携带清单页-pt14

### pt16 · Schedule and deadline page 日程与截止日期页
- **Intent**: "when does registration open", "which days is the window", "am I still in time".
- **Cited by**: tier B, ChatGPT · 650–700 words.
- **Sides**: build on every side (booking windows written as process time; dates tied to the registered course or product name).
- **Blocks**:
  1. H1 — process name, no year `[req]`
  2. First-screen sentence — who can apply + this year's opening dates `[req] ★`
  3. Four fixed H2s — Criteria → Procedure → Schedule → Enquiries `[req]`
  4. Two-column date table — Period / Actions: apply, shortlist, results `[req] ★`
  5. ✗ eligibility reasoning on this page
- **Common mistake**: dates in the H1 and a new URL every year, which resets the page's history.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-25-1-日程与截止日期页-pt16

### pt22 · Collected FAQ page 集合式 FAQ 页
- **Intent**: definition + risk combined; long-tail follow-ups to procedures and rules. Unlike pt06, many questions on one page, each answer quoted separately.
- **Cited by**: tier B, ChatGPT · 613–1,370 words.
- **Sides**: build (strict: general information only, side-effect wording aligned with official documents, no "free consultation"; E→ no peer comparison in answers).
- **Blocks**:
  1. Alternating questions and answers — no body paragraphs, no intro `[req]`
  2. Questions in the buyer's words — each standalone `[req]`
  3. Answers of 40–80 words — the first sentence is the conclusion `[req] ★`
  4. One-sentence answers with thresholds — quoted even when far down the page `[req] ★`
  5. Footnote numbers on key claims `[opt]`
  6. schema — FAQPage `[opt]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-25-2-集合式-FAQ-页-pt22

### pt26 · Policy hub page 政策专题 hub 页
- **Intent**: "complete guide to X", "all the rules on X". AI tends to follow the hub's in-page anchor order when structuring its answer.
- **Cited by**: tier B, ChatGPT · 441–6,653 words.
- **Sides**: build (strict: process and official wording only, no peer comparisons).
- **Blocks**:
  1. First-screen question anchors — a list of in-page anchors, not a summary `[req]`
  2. H2s match the anchors one to one, in order `[req]`
  3. Phased timeline table — Implementation Date / Who it applies to `[req] ★`
  4. Subsidy or transaction tables — 3–5 rows each `[opt]`
  5. Glossary — one term + one-sentence definition per row `[req] ★`
  6. Update date + schema — Last updated + FAQPage `[req]`
- **Common mistake**: splitting one topic into ten blog posts. Build one hub.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-25-3-政策专题-hub-页-pt26

### pt34 · Change notice / old-vs-new page 变更公告页
- **Intent**: after AI finds a price or rule, it checks whether it still applies. This page stops AI quoting old prices and old rules.
- **Cited by**: tier B, ChatGPT · 1,700–2,400 words.
- **Sides**: build (strict: rules and effective dates only, no price increases, original prices or discounts; subsidy changes in their own section).
- **Blocks**:
  1. Effective date in the title — commercial version starts "Important:" + date `[req]`
  2. Scope statement — which part changed `[req]`
  3. Timeline table — Date / What Happens, 3–8 rows `[req] ★`
  4. Old-vs-new sentence — old practice and new practice in one sentence `[req] ★`
  5. Transition rules — their own H2 with the number of days `[req]`
- **Common mistake**: quietly editing the number on the old page. Each price change gets a notice page, and the old page links to it from the top.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-25-4-变更公告页-pt34

### pt40 · Misconception page 误解纠正页
- **Intent**: questions that hide a popular false premise ("everyone thinks you can, but you can't"). Exempt from the first-30% rule: each entry carries its own context and can be quoted from anywhere on the page.
- **Cited by**: tier B, ChatGPT · up to 7,500 words.
- **Sides**: build (each fact sentence matches the legal text and cites it; never framed as a dig at peers).
- **Blocks**:
  1. H1 — an opposing short phrase `[req]`
  2. A single H2 — the only H2 on the page `[req]`
  3. Entries × N — collapsible, three fixed parts `[req]`
     - the popular claim, in the buyer's first-person words `[req]`
     - a one-word verdict ("Incorrect!") on its own line `[req]`
     - the fact sentence + footnote: party + amount + effective date `[req] ★`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-25-5-误解纠正页-pt40

---

## Entity and product facts family · 实体与产品事实类 (8)

### pt09 · Entity anchor pages 实体锚点页 (organisation facts, person, product detail)
- **Intent**: "who is this", "where is it", "what exactly is this product". Three sub-types.
- **Cited by**: tier A; organisation pages mainly ChatGPT; product detail pages ChatGPT only · organisation pages vary, PDP 400–1,500 words. Organisation fact pages were cited with no conclusion block, date or byline before the first H2: this type runs on numbers.
- **Sides**: build on every side; strict: no testimonials, stars or before/after (explicit); E→ no relative position against peers.
- **Blocks — organisation facts page `/facts`**:
  1. title / H1 — legal name + bare facts, zero adjectives (e.g. "<Legal name> · Company facts") `[req]`
  2. Credential sentence — licence, registration number, year: 2–4 numbers `[req]`
  3. Hard fact cards — 3–5 KPI cards, each with definition, denominator and period underneath `[req] ★`
  4. 14-row field table — one field per row, no narrative in values `[req] ★`
     - practitioners: name + registration number + official lookup link, one per row `[req]`
  5. Price block — per side: fixed price, or range + billing method `[req] ⚖`
  6. Location and hours — day by day, never "by appointment" `[req]`
  7. Reviews — none on the regulated side `[opt] ⚖`
  8. FAQ — 3–6 questions restating the body `[opt]`
  9. ✗ self-ratings, reposted reviews, comparison images `⚖`
  10. Footer — last verified date + owner `[req]`
  11. schema — one site-wide template, not per page `[req]`
- **Blocks — person page `/team/<name>`** (*not measured*): H1 unique legal spelling + registered title → registration strip (number, register and status, start date, official lookup link) → compliance line (regulated side only, dated) → qualifications table (degree, institution, year; practice start year) → third-party grading (not on the strict side for vendor-granted tiers) → scope and services with fixed prices `⚖` → external anchors (association profile, academic ID, speaker page, professional profile, Wikidata QID if it exists) → bylined content list → update date.
- **Blocks — product detail page**:
  1. H1 — full product name + key spec `[req]`
  2. Buy box on the first screen — actual price / original / discount / stock / delivery, matching the feed, structured data and checkout `[req] ★ ⚖`
  3. Feature H3s — numbers in the headings `[req]`
  4. Spec table — Specification / Value, HTML table, never an image `[req] ★`
  5. Warranty — own section: years, who is responsible, local service centre `[req]`
  6. Returns / trial `[opt]`
  7. FAQ — 3–5 H3 questions `[opt]`
- **Full spec**: https://canlah.ai/zh/playbook/identity/#g3-3-2-事实表与机构事实页 · https://canlah.ai/zh/playbook/identity/#g3-3-3-个人实体页与六处痕迹对齐 · https://canlah.ai/zh/playbook/page-types-core/#g6-5-20-实体锚点页-三个子型与商品详情页-pt09

### pt11 · Store / branch page 门店页
- **Intent**: "X near <MRT station / area>", "is X open on Sunday". When a place name or "visit" appears in the question, this type takes almost all citations. One location, one URL.
- **Cited by**: tier B, ChatGPT · 60–1,500 words.
- **Sides**: build on every side; the safest type on the strict side (address, hours, phone, registration fields, zero adjectives).
- **Blocks**:
  1. title — service + place first, brand after `[req]`
  2. H1 — service + place, or "Welcome to <store>" `[req]`
  3. Full address line — building, number, unit, postcode on one line; conditions on the same line `[req] ★`
  4. Opening hours by day — 4–7 plain-text lines, Sunday on its own line `[req] ★`
  5. Phone and messaging — one channel per line `[req]`
  6. H2 how to get here — MRT station name in the H2; walking minutes, shuttle, parking `[req]`
  7. Nearby landmarks — one or two `[opt]`
  8. Staff at this branch — one line each: qualification, start year, location, registration number `[opt] ⚖`
  9. LocalBusiness schema — matches visible values exactly `[opt]`
  10. ✗ hours or address rendered by JS
- **Test**: `curl` the page and `grep` the unit number and "Sun".
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-26-1-门店页-pt11

### pt21 · Vendor legal terms page 厂商法律条款页
- **Intent**: "can the data be stored overseas", "are you compliant": questions that need the country in writing.
- **Cited by**: tier B, ChatGPT · 1,500–9,800 words.
- **Sides**: strict adapt (equivalent: data handling and confidentiality policy page) · light adapt (same).
- **Blocks**:
  1. title / H1 — full name of the terms, no marketing words `[req]`
  2. TOC, FAQ, dates, author — not needed for this type `[opt]`
  3. Definitions clause — lists the countries or jurisdictions covered `[req] ★`
  4. Sections per jurisdiction — section title = jurisdiction name `[req]`
  5. Commitment sentences — compliance commitments naming the country `[req] ★`
  6. Numbered clauses `[req]`
  7. ✗ "applicable laws" without naming the country
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-27-2-厂商法律条款页-pt21

### pt30 · Verification and lookup page 核验与查询入口页
- **Intent**: the closing step of guide answers: "how do I check this <practitioner> is qualified", "where do I find certified X". Cited because it is the one actionable step in the answer. Put that step on your own page.
- **Cited by**: tier B, ChatGPT · 267–716 words.
- **Sides**: build on every side (registration numbers + official lookup links only; strict links to government only, never to a vendor locator).
- **Blocks**:
  1. H1 — the body's name, or "Find a <category> <role>" `[req]`
  2. Legal authority sentence — established under which law, regulating whom `[req] ★`
  3. Two action buttons — search the register, practitioner login `[req]`
  4. Search box — the first H2 `[req]`
  5. Four explanatory H2s — apply, registered practitioners, dated notices, FAQ `[opt]`
  6. URL with a search-type parameter `[opt]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-26-2-核验与查询入口页-pt30

### pt31 · Help centre / how-to page 帮助中心与操作页
- **Intent**: "how do I set up B in A", "how do A and B connect". Help pages beat product pages because facts are short sentences, not marketing.
- **Cited by**: tier B, ChatGPT · 660–2,500 words.
- **Sides**: strict adapt (equivalent: operations page: how to book, reschedule, get results; process only, no effects) · light build.
- **Blocks**:
  1. Line above H1 — update date + scope `[req]`
  2. H1 — task name starting with a verb `[req]`
  3. First paragraph — the objects and direction involved, no warm-up `[req] ★`
  4. H2 step names — or Step 1…4 first `[req]`
  5. Limitations list — "does not support / does not sync" as its own paragraph `[req] ★`
  6. Exact menu path text `[opt]`
  7. ✗ hiding what is not supported
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-27-3-帮助中心与操作页-pt31

### pt33 · Third-party directory listing 第三方目录收录页
- **Intent**: the fallback for location questions when AI cannot find an official branch page. You cannot build it: publish a pt11 page per location and correct every directory entry to match word for word.
- **Cited by**: tier B, ChatGPT · 128–800 words.
- **Sides**: cite only on every side; the self-supplied blurb still follows price and ad rules (no "From", discounts or "best" on strict and E).
- **What AI reads**: title (English name + local-language name + category and place) → H1 with branch suffix → one blurb ending with payment methods and subsidies `⚖` → H2 opening hours (seven lines, ★; the line that gets challenged when it conflicts with the official site) → H2 address and contact.
- **Common mistake**: directory hours from three years ago that differ from the official site; the directory entry is down-weighted on the spot.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-26-3-第三方目录收录页-pt33

### pt35 · Integration / marketplace listing 集成与对接 listing 页
- **Intent**: "can A integrate with B", "does A have a connector". B2B only.
- **Cited by**: tier B, ChatGPT · length varies (JS-rendered).
- **Sides**: strict adapt (equivalent: "which institutions and payment methods we work with"; name them, do not link) · light adapt (same).
- **Blocks**:
  1. title / H1 — one integration per URL `[req]`
  2. ✗ a logo wall with no fields
  3. Certification badge — AI uses it for yes/no answers `[req]`
  4. Builder — first-party or third-party `[opt]`
  5. Objects list — name each synced object, not "core data" `[req]`
  6. Direction — one-way or two-way, in the same sentence `[req]`
  7. Prerequisites — required plan or credentials `[req]`
  8. Not supported — state what it does not do `[req]`
  9. Sync timing — frequency, full or incremental (not measured) `[opt]`
  10. Plain-text fallback page — the same fields on a help page that `curl` can read `[req]`
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-27-4-集成与对接-listing-页-pt35

### pt39 · Trust centre / compliance proof page 资质与合规证明页
- **Intent**: B2B due diligence: "is X compliant", "how secure is X".
- **Cited by**: tier B, ChatGPT · 3,600–8,650 words.
- **Sides**: strict build (harder version: licence and credential wall) · light build (practising certificates and insurance wall).
- **Blocks**:
  1. title — own subdomain optional `[opt]`
  2. H1 — "<Brand> Trust Center" `[req]`
  3. Counter strip — number of documents, FAQs, certificates in one line `[req]`
  4. Certificate / licence wall — name + issuer + validity, machine-readable list `[req] ★`
  5. Latest check date sentence — the exact date of the most recent report or check `[req] ★`
  6. Q&A directory — grouped by topic with counts `[req]`
  7. Reports themselves — may sit behind login or NDA `[opt]`
  8. ✗ a marketing article with adjectives instead of a certificate wall
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-27-1-资质与合规证明页-pt39

---

## Primary sources family · 源头类 (7)

These are mostly pages you cannot write in place of the official source. What you can do: write downstream pages that quote verbatim, with clause anchors and a check date, and get your own row filled in.

### pt15 · Statute text page 法条原文页
- **Intent**: the "on what basis" part of rule questions; AI wants a URL that points to a clause.
- **Cited by**: tier B, ChatGPT · 2,500–3,300 words.
- **Sides**: cite only (own summaries of statutes were never cited in our data).
- **What AI reads**: title "Part <n> – <name>" or full statute name → optional full TOC → H2 = numbered section title (the title is the rule name) → numbered subsections (1)(2)(a)(b), each a complete rule (★) → a stable anchor per section (★) → list of commencement dates. ✗ Your paraphrase without clause number and link.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-28-1-法条原文页-pt15

### pt18 · Regulator guidance PDF 监管机构指引 PDF
- **Intent**: rule and complete-guide questions in English and Chinese; dominant for Chinese regulation questions. PDFs are not down-weighted here; they are the first-choice source when they have a question-style table of contents.
- **Cited by**: tier B, ChatGPT · 20–62 pages.
- **Sides**: build (you may publish your own compliance long-form PDF; prices inside still follow the final-price rule; with switch B, full fee elements).
- **Blocks**:
  1. Cover — full title + version + revision date `[req]`
  2. Question-style TOC — each line a buyer question + page number `[req] ★`
  3. Numbered paragraphs — each can be cited precisely `[req]`
  4. Definition and effective date in the first 3% — one sentence `[req] ★`
  5. ✗ a TOC of noun phrases
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-28-2-监管机构指引-PDF-pt18

### pt19 · Statistics source page 统计源头页
- **Intent**: "what percentage of people X", "average X", "how many use X". Includes first-party data reports.
- **Cited by**: tier B, ChatGPT · 300–2,540 words.
- **Sides**: strict adapt (six checks, then the compliance lead; no success rates) · light build (no success rates).
- **Blocks**:
  1. Method paragraph — sampling + sample size + basis + change from the last edition `[req]`
  2. Structure labels — OBJECTIVES etc., or numbered charts `[req]`
  3. Population qualifier right after every percentage `[req]`
  4. Restated key numbers in the conclusion `[req] ★`
  5. Chart titles with year and basis; value labels on bars `[req] ★`
  6. Sentence above each table stating its numbers `[req]`
  7. Scope-negation sentence — excludes A, does not cover B, survey year C `[req]`
  8. Named author and unit `[opt]`
  9. ✗ numbers without survey name + year + sample size
- **Note**: writing "there is no official figure" can itself be quoted as the answer. A yearly dataset page (clean HTML table + CSV, basis and dates per row) is the one move that makes third parties come to cite you.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-29-1-统计源头页-pt19

### pt20 · Register / approved list page 名录与准入名单页
- **Intent**: "which providers are accredited", or location questions that need many names at once.
- **Cited by**: tier B, ChatGPT · 13–66-row tables.
- **Sides**: cite only. Get into every official and platform register you can, and fill your row completely.
- **What AI reads**: title / H1 "<body> + <list name> + Listing" (no year, no "best") → two first-screen sentences: what the list means; listing is not endorsement (★) → long table, one row per provider, all fields filled (★) → tiers as H2s (vendor registers) → tier explanation → footer update date → the self-supplied blurb, written as fee and credential facts `⚖`. ✗ Empty fields in your row.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-29-2-名录与准入名单页-pt20

### pt23 · Official replies and speech records 官方答复与讲话记录页
- **Intent**: when no official document gives a number or rule, AI falls back to what an official said on record.
- **Cited by**: tier B, ChatGPT · 1,700–5,700 words.
- **Sides**: cite only (a restatement page: verbatim quote + link + date; never imply the official endorses you).
- **What AI reads**: title (title and name + occasion + year) → date + category line → no H2s: sections + numbered paragraphs, each with its own subject (★) → self-contained number sentences with numerator, denominator, percentage and time window (★) → transcript variants split per exchange.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-28-3-官方答复与讲话记录页-pt23

### pt32 · Device and product regulatory documents 器械与产品监管文件页
- **Intent**: definition questions about side effects, indications, where a product may be used. For efficacy and side effects, AI trusts regulator wording, not seller claims.
- **Cited by**: tier B, ChatGPT · 30–1,008 words.
- **Sides**: cite only. Your own side-effect paragraph must match the regulator's wording line by line (link government sources; name vendor documents by file name and version).
- **What AI reads**: three carriers (instructions landing page + PDF; regulator explainer with one H2 in four blocks; approval document listing indications) → side-effect wording (★, copied almost verbatim) → indications listed one by one (★). ✗ Your own softer wording.
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-28-4-器械与产品监管文件页-pt32

### pt36 · Case-law page 判例页
- **Intent**: the "how courts actually decide" step in guides and estimates.
- **Cited by**: tier B, ChatGPT · 689–16,152 words.
- **Sides**: strict stop (equivalent: pt32) · light: industry edition decides (only where case law exists; summaries, not win records, no win rates).
- **Blocks** (summary version):
  1. H1 — case name + topic + year + court + number `[req]`
  2. Holding sentence under H1 — standalone: what rule the case set; the subject is the court `[req] ★`
  3. Judgment date `[req]`
  4. Two H3s — Facts / Court's Decision `[req]`
  5. Outcome block (full version) — the court's orders `[opt]`
  6. Subsequent treatment sentence (full version) — still cited by N judgments, any negative treatment `[opt] ★`
  7. Citation graph (full version) — Cited by / Authorities cited `[opt]`
  8. Stable anchor per paragraph `[opt]`
  9. ✗ the full judgment with no holding sentence
- **Full spec**: https://canlah.ai/zh/playbook/page-types-more/#g7-5-28-5-判例页-pt36

---

## Commentary family · 解读与观点类 (3, all tier C)

All three are *not measured*; specs come from an external teardown, and schedule them after tiers A and B. Validate pt43, pt44 and pt45 first; pt46 last. Index and scheduling: https://canlah.ai/zh/playbook/page-types-checklist/#g8-其余三型-各一行 · Blueprints: https://canlah.ai/zh/playbook/templates/#g14-B-5-未验证页型的施工图-供行业版引用

### pt44 · Concept pillar page 概念支柱页
- **Intent**: "what is the difference between X and Y" (two concepts, long form). Titles with "which is better / which to buy" belong to pt04; one concept belongs to pt12, which is measured, so build pt12 first. One keyword, one page.
- **Sides**: strict build (options and formats only, not institutions; named reviewer) · light build (no success rates, no peer comparison).
- **Blocks** (*not measured*): title "{NEW} vs {OLD}: difference + outcome noun" → one-line axiom (complementary, not substitutes) → H2 why AI does not recommend you (200–280 words, 4–5 buyer questions inline) → H2 the difference in 30 seconds (+ table) → H2 why it matters now → H2 what is OLD / what is NEW → H2 core differences (+ table) → H2 why you still need NEW if you have OLD (3 pattern subheads) → H2 most common problems in real projects (evidence) → H2 four common problems → H2 each engine prioritises differently (+ table) → H2 will it replace / how they combine / which first (3 case subheads) → H2 summary → FAQ 8–11 (no bold, links, bullets or brand names in answers).

### pt45 · News and policy explainer 新闻与政策解读页
- **Intent**: a new rule or event. Citations for rule questions land almost entirely on the official page; the only way in is to restate the rule verbatim, date it, link the original, and add one sentence on what it means for this industry. What gets quoted: who / from which date / must do what / penalty. Opinions were never quoted.
- **Sides**: strict adapt (official numbers in their own section; never use a new rule to solicit) · light build.
- **Blocks** (*not measured*): assertive title with the event → untitled lead of 3–5 sentences (date and event → bet → headline number → negative-first lesson) → H2 key findings (4–5, third parties first, last one self-limiting) → H2 what happened (past tense, no adjectives) → H2 why the mechanism matters (one study per paragraph, sourced) → H2 our evidence (table) → H2 what the audience should do (5–6 bullets, no product names, no soliciting `⚖`) → H2 our position (optional) → H2 method and limits → FAQ of exactly 3 sceptical questions, each answer starting with a negative.
- **Example sentence** (not measured): "From <effective date>, <new rule> requires <who> to <do what>; for <a group in this industry>, the direct effect is <one sentence>."

### pt46 · Market observation page 市场观察页
- **Intent**: commentary on a market shift. Weakest evidence, with counter-evidence: the teardown subject's own articles of this kind were internal-link dead ends.
- **Sides**: strict stop · light stop (where it barely works, write it as pt45). Without first-party data, do not write or schedule it; a service provider's own blog may use it as brand material, not as a cited page.
- **Blocks** (*not measured*): declarative title with a structural claim → lead of 90–160 words (fact → evidence → audience constraint → correction) → H2 key findings (exactly 4) → H2 argument one / two → H2 our first-hand view (at 40–55% of the page `⚖`) → H2 framework table → H2 who is affected → H2 what buyers should test (no product names) → H2 our position (the only sales section, third or fourth from last, no links `⚖`) → H2 method and limits → FAQ of exactly 3 → references 2–4.

---

## Before publishing any page (5.31)

Five steps, each blocking the next: brief (≥5 exclusive facts or change the intent cluster) → draft (write `[Source needed]`, never invent) → fact check by someone other than the author → compliance sign-off by the licence holder → launch acceptance. Checks: see [audit-checklist.md](audit-checklist.md) §3. Full checklist: https://canlah.ai/zh/playbook/page-types-checklist/#g8-5-31-交稿-每页五步-撒谎红线与自检
