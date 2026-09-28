# AGENTS.md · GEO Playbook (agent edition)

Instructions for any AI coding or research assistant (Codex, Cursor, OpenClaw, Claude Code and others) that reads `AGENTS.md`. The same method is packaged as a Claude Code skill in [SKILL.md](SKILL.md); the content is identical.

**Use this when the user asks to** audit or plan a website's visibility in AI answers (ChatGPT, Google AI Overviews and AI Mode, Perplexity, Copilot); find out why AI gets the business's facts wrong or never names it; build a question pool and baseline; pick target questions; write pages that AI quotes; plan off-site listings, corrections and bylined articles; run a monthly retest; or write compliant copy in a regulated industry. Also for GEO, AEO and "LLM SEO" questions, and to check claims such as "you need llms.txt".

**How to use this file in another project**: copy `AGENTS.md` and the `references/` folder into the project root (or add this repository as a submodule and point your agent at it). All links below are relative to this file.

The method in one sentence: **write facts in clean visible HTML, let crawlers in, make machines sure which business it is, then get onto the third-party pages AI already reads, and measure with the same ruler every month.** 把事实用干净的可见 HTML 写出来，让爬虫进得来，让机器认得出是这一家，再想办法出现在 AI 本来就在抓的第三方页上。

Evidence base: Canlah AI's own measurements on Singapore businesses in five industries (dental and aesthetics, family law, tuition, B2B SaaS, e-commerce), both rounds completed 2026-09-23. Round 1: 60 questions on ChatGPT and Google AI Mode, 526 citations, 92 cited pages taken apart. Round 2: ChatGPT only, 241 citations. Outside Singapore, treat rules as method and re-measure. Full playbook for people (Chinese): https://canlah.ai/zh/playbook/ · English quick guide: https://canlah.ai/playbook/

## Ground rules (every step)

1. **Never promise rankings, citations or timelines.** The only hard commitments are deliverables the user controls: pages live, profiles complete, the door fixed with crawl evidence, monthly answer comparisons.
2. **Read-only until the baseline is saved.** Do not change robots.txt, WAF rules, meta tags, business profiles or the facts page before step 3 is complete. Ask before any change to the user's site or accounts. Draft outreach; the user sends it.
3. **Label every claim**: "measured n/N", "measured, 1 case" or "not measured". Never invent a number. Anything you could not fetch is "not retrieved".
4. **Name the rulers correctly**: "Model-API visibility baseline · OpenAI leg", "Gemini model leg", Search Console generative AI impressions. Never call an API result "what users see". Never add rulers into one score.
5. **Compliance before copy.** Decide the side (step 0) before writing a single sentence. This is not legal advice; follow the stop and sign-off rules in [references/sides-and-compliance.md](references/sides-and-compliance.md).
6. **Anything that names competitors is internal** (brand question 6, competitor tables, rank lists). Never put it in client-facing or public material.
7. **Never judge a page by faking a crawler user-agent and reading the content.** Browser UA for content, crawler UA for status codes only.

## Reference files (load when the step needs them)

| File | Load for |
|---|---|
| [references/sides-and-compliance.md](references/sides-and-compliance.md) | Step 0; any copy on a regulated side; reviews, prices, comparisons |
| [references/audit-checklist.md](references/audit-checklist.md) | Steps 1, 2 and the per-page gates in step 5 |
| [references/measurement.md](references/measurement.md) | Steps 3, 4 and 7 |
| [references/page-types.md](references/page-types.md) | Step 5 (46 page types, block order, what AI copies) |
| [references/myths.md](references/myths.md) | When anyone proposes llms.txt, schema everywhere, paid listings, view-chasing, blocking GPTBot |

When a detail is not in the references, fetch the full chapter as Markdown: take the chapter URL listed at the end and replace the trailing slash with `.md` (for example https://canlah.ai/playbook/start.md). All chapters: https://canlah.ai/playbook/index.md (English) · https://canlah.ai/zh/playbook/index.md (Chinese original). Chapters are long; fetch only the one the current step needs. Quote the book's limits along with its numbers.

---

## Step 0 · Intake and side check (判侧)

Before asking, read what is public so the questions are specific: the home page, the footer (legal name, registration number), the pricing page, the about/team page. Pre-fill what you found and mark it "from site, to verify".

Then ask the user in one message (mark every answer "to verify"):

- Legal name exactly as registered, main market, licence or registration numbers.
- **Side questions** (decide in this order; full table in [sides-and-compliance.md §1](references/sides-and-compliance.md)):
  1. Does opening the business, or doing the work, need a licence or a personal professional registration? **No** → provisionally *unregulated*; run the reverse checks below. **Yes** → Q2.
  2. May prices be written as a range? **No** → *strict* (stop asking). **Yes** → Q3.
  3. Are testimonials or peer comparisons banned outright (→ *strict*), allowed with conditions (→ *light*), or not specifically regulated (→ *unregulated*, even with a licence)?
  4. On any side: is peer comparison banned, including unnamed market ranges? Yes → switch E.
- Switches: **A** does anyone write or publish for the business? This includes you and the user if the user is an agency or freelancer working for someone else's business. **B** does the law list fields an ad must show? **C** does anything sold need registration or a licence even though the company does not? **D** does the business run regulated and unregulated lines together? **F** are referral payments banned? If so, list any lead- or commission-priced platforms they use.
- Can they state fixed final prices (strict side) or ranges with billing method (light side)?
- Price per order, gross margin, monthly capacity, and how often a buyer buys.
- Who can edit the site, and how long one page change takes.
- Access: server/CDN logs, Search Console, Bing Webmaster Tools, the five business profiles.
- Namesakes (same business name or practitioner name)? Chinese or other-language buyers? Leads by form, chat or phone? Who they think the competitors are.

Checks: if Q1 is "no", run the three reverse checks. The side moves up one level if the copy makes health, efficacy, earnings, results or employment claims, if the audience includes minors, or if the buyers are abroad. Unsure → stricter side; never write "TBD".

Output: the first line of `work-order.md` (template: https://canlah.ai/zh/playbook/templates/#g14-B-4-工单-台账与月报表头). Fill in every field; write "to fill in step N" only where the step named fills it:
`Side: <strict|light|unregulated> · Switches: <letters A–F, or none> · Unsure items (treated as stricter): <…> · Compliance lead: <name or none> · Written authorisation (switch A): <on file|missing|n/a> · Scope: <full|audit+monitoring|hold> · Acceptance tier: <attributable|observable> · Top 3 buyer types: <to fill in step 4> · Languages: EN + ZH · Blockers: <e.g. "no access logs, requested <date>, due <date>">`

- *Scope*: **full** runs every step. **audit+monitoring** runs steps 1–3 and 7 and writes no new pages. **hold** adds nothing new and keeps existing positions: each month the brand-six runs, the held questions with their noise band, profile consistency and corrections (chapter 7.4).
- *Acceptance tier* is set on day one by how leads arrive. **attributable**: form/chat prefill and CRM tags exist, so results are accepted by enquiries. **observable**: phone-led, high-ticket, or 3–9-month sales cycles, so results are accepted by seats + rank + pages on the list, plus a mandatory "how did you find us" field at the front desk.

Stop or downgrade: switch A on and no written authorisation → stop (no downgrade path). Strict side and no fixed final prices → audit+monitoring. Fewer than 10 real buyer questions (step 3) → audit+monitoring. One page change takes more than four weeks and that will not change → hold. Frequent, low-ticket purchases → hold, or do not take the job.

Example, a B2B software company: no licence needed (Q1 no); the copy makes no health, earnings or results claims, has no minors in its audience and sells to Singapore buyers, so no reverse check hits → `Side: unregulated · Switches: none`, unless an agency writes for it (switch A) or it claims results for customers (move up one level).

## Step 1 · Door check, read-only (开门体检)

Goal: prove whether AI crawlers can read the page text. The door multiplies everything by 0 or 1. Details: [audit-checklist.md §1](references/audit-checklist.md).

Everything here is read-only. You only fetch, you never change anything, and you save every raw response (headers, HTML, robots.txt) under `door_<date>/` as the receipt.

**1a. Pick the hosts and the 8 pages.** Read `/sitemap.xml` and every `Sitemap:` line in robots.txt, plus the links in the home page's header and footer. List every hostname that serves pages: www, docs., help., blog., trust., and app subpaths served from the same host still count as the same host. Choose 8 pages: home, price page, facts page (`/facts` or equivalent), a service page, a person/author page, an old blog post, a list/category page, a landing page. If the site has no page of a kind, write "none", and a missing facts or price page is itself a finding for `to_fix.md`.

**1b. robots.txt, per host.** `curl -s https://<host>/robots.txt` and save the whole file. Status other than 200, a timeout or a TLS error means "not retrieved": retry once, never guess. For each of the 12 retrieval user-agents (`OAI-SearchBot`, `ChatGPT-User`, `OAI-AdsBot`, `Bingbot`, `Googlebot`, `Applebot`, `Amazonbot`, `PerplexityBot`, `ClaudeBot`, `Claude-SearchBot`, `Claude-User`, `DuckAssistBot`), decide which group applies:
- A group whose `User-agent:` line names that crawler (case-insensitive) applies, and **only that group**. The wildcard group is then ignored for it.
- No named group means the crawler falls to `User-agent: *`. Record "falls to wildcard", not "blocked".
- Record it as **blocked** if the applying group has `Disallow: /` without a matching `Allow`. Record it as **allowed, N paths disallowed** if the group has narrower `Disallow` lines.
- Do not judge by grepping one keyword. Read the file group by group.
Also count the wildcard group's `Disallow` lines (**N**) and copy them verbatim. Mark the 6 training crawlers (`GPTBot`, `Google-Extended`, `Applebot-Extended`, `Meta-ExternalAgent`, `CCBot`, `Bytespider`) "unrelated to being cited".

**1c. Snippet switches, on the 8 pages.**
```bash
curl -sI "$URL" | grep -i 'x-robots-tag'
curl -s -A 'Mozilla/5.0 (Macintosh)' "$URL" | grep -Eio '<meta[^>]+name="(robots|googlebot)"[^>]*>|data-nosnippet|max-snippet:[0-9]+|nosnippet'
```
A hit on `nosnippet`, `max-snippet:0` or a small number, or `data-nosnippet` on a price, FAQ or fact block is a to-fix item. The Google leg (AI Overviews, AI Mode) counts as zero while it is on.

**1d. Is the text in the HTML?** Open each key page the way a person sees it (ask the user, or use a browser tool) and pick its price string and one sentence of body text. Then `curl -s -A 'Mozilla/5.0 (Macintosh)' "$URL"` and search the raw HTML for both strings. If they are missing, the page is client-side rendered, and the fix is server rendering or prerendering. This check has nothing to do with the user-agent.

**1e. WAF hint.** `curl -s -o /dev/null -w '%{http_code}\n' -A 'OAI-SearchBot' "$URL"`: record the **status code only**. 403, 429, a captcha or a redirect suggests a WAF or rate rule. A 200 here proves nothing about real crawler access; only logs do. Never read the content returned to a faked crawler UA.

Ask the user for these, since you cannot see them yourself: 30 days of access logs filtered by official crawler IP ranges (or permission to request them today); WAF settings screenshots ("Block AI bots" / "Bot Fight Mode", rate rules, allowlist); Bing URL Inspection Live Test HTML; Search Console crawled-page HTML; and the result of pasting a price-page URL into ChatGPT and asking it to quote the price line word for word.

Outputs (change nothing):
- `gate_read.md`: **the six lines**. (1) the 12 retrieval UAs, each with its group and allowed/blocked. (2) The wildcard group's N and its `Disallow` lines verbatim. (3) The 6 training UAs, marked "unrelated to being cited". (4) Snippet switches on the home and price pages. (5) CDN/WAF: "Block AI bots" on / off / unknown, rate rules, and whether the `ChatGPT-User` ranges are allowlisted (from the user; else "not retrieved"). (6) Access logs: log push / access.log / none, and the date permission was requested. A missing line means the check was not done.
- `door_table.md`: one row per host, one column per retrieval UA (the 12 above, never merged into one cell), plus a **verification level** column: `robots-verified` (read from robots.txt only) or `fetch-verified` (a fetch with that crawler's UA returned 200 and contained the body sentence from 1d; a reachability receipt only, never a gate-2 pass and never a judgement of the content). A fetch receipt is written only as "fetched 200 + body text found" or "fetch blocked (<status>)", never "allowed". If robots is not blocked but nothing was fetched, write "robots not blocked, fetchability unverified".
- `crawler_hits_30d.csv` (crawler · hits · top 20 URLs · status-code mix), or a red blocker "no access logs, requested <date>, due <date>" in the work order's first line.
- `to_fix.md`: every finding, each marked "fix after baseline (step 3, split day)".

Key readings: `OAI-SearchBot` = 0 in the logs → door closed or site undiscovered (never "no demand"). 403/429 > 5% in the logs → WAF, not robots. No logs → say "no direct evidence", never "the door is open". Google names the business but ChatGPT never does → check client-side rendering first. `GPTBot` and `Google-Extended` are training/licensing crawlers; they decide nothing about being cited.

## Step 2 · Identity check, read-only (认对人)

Goal: machines must be sure which business this is, and quote its facts correctly. Details: [audit-checklist.md §2](references/audit-checklist.md).

You can run:
- Extract the 14 hard facts from the site (legal name, registration number, licence number + lookup link, practitioners with registration numbers, address, phone, hours by day, year founded, languages, main services, devices/materials, insurance/subsidy scope, rework policy, last verified date) into `facts-table.csv` with source / verified date / publishable? / owner.
- Compare spelling of the business and every named practitioner across the site, the official register, association profiles, business profiles and professional pages. Three spellings are three entities.
- Check the five business profiles (Foursquare, Yelp, Google, Bing Places, Apple Business Connect): present / absent / squatted; does the URL field point to the right landing page (not the homepage)?

Ask the user: which facts are confidential; banned topics and phrases (`exclusions.md`); internal price list export (regulated side: check prices against it, not against the old website).

Outputs: `facts-table.csv`, `profiles-5.csv`, `exclusions.md`, spelling mismatch list. Brand-six errors are added in step 3.

## Step 3 · Freeze the question pool and baseline, then fix (冻题池与基线)

Goal: one ruler for the whole quarter. Details: [measurement.md §3–4](references/measurement.md).

1. **Question pool (30)**: only from buyers' own words before purchase, active ad keywords, real queries (Search Console, autocomplete, Bing grounding queries), and questions already listed on competitor or directory pages; each with evidence. Never generate questions yourself. Ratios: ≥18 with a location, ≥9 with price words, ≤3 bare category words; Chinese questions count inside. A second person verifies ratios; the decision-maker signs. Output `question-pool.csv` (question, source class, evidence link, location?, price?, shape, language).
2. **Baseline runs** (if you have API access, run them; otherwise give the user this protocol): validate the ruler with a question known to be cited; coarse screen 30 × 1 × 2 engines; full rounds on battlefield + hold piles × 5 rounds × 2 engines; the same again 3 times in one week for the noise band (max − min, floor ±1 seat); brand six questions × 3 rounds × 2 engines = 36 runs.
3. **Web control leg** (the user does it by hand): 5 fixed questions in ChatGPT's web interface, logged out or temporary chat, local IP, one pass each, full screenshots. Add web-only domains to the candidate pool **before** freezing the Top 20.
4. **Freeze** the account-level Top 20 cited URLs from the raw `domains_cited`.
5. **Baseline saved** = Top 20 + noise band + 36 brand-six runs on disk. Record the date.
6. **Split day** — now apply the fixes, in this order, with the user's approval: snippet switches → robots.txt four-step merge (receipt: "N × 12") → WAF allowlist for `ChatGPT-User` → (D+7 recheck) → `/facts` page → person pages → six-trace alignment and correction letters → five profiles → JSON-LD template once.

Outputs: `question-pool.csv` (signed), `probe_<month>/` raw answers, `noise-band.md`, `brand-6.jsonl`, `entity_errors.md`, `sources-top20.csv` (with `web_only`), `web_leg_<month>.csv`, split-day entry in `work-order.md`.

## Step 4 · Pick targets (选点)

Goal: aim at buyers whose wins pay, not at questions that are easy. Details: [measurement.md §5](references/measurement.md).

- Group questions by **buyer type**; rank by annual opportunity value = price × margin × monthly capacity × 12 (ranking only; never a forecast).
- Per candidate: gate 1 (does the answer name any business?), gate 2 (≥4 reachable URLs in this intent's own top 10, across ≥2 classes), gate 3 (can the business serve and profit from these buyers?).
- Judge each URL in the intent-level top 10 by URL, not domain: already present / reachable / to ask / not reachable, with date, basis, judge.
- Slots: 1 = brand / correction; 2 = best hold question; then by value; at most one national bare keyword, last. Pure symptom questions are out.

Output: `season-list.csv` (intent, buyer type, value, four-state actions, acceptance tier), signed by the user.

## Step 5 · Write pages by page type (按页型写页)

Goal: pages that AI can copy a sentence from. Details: [page-types.md](references/page-types.md), gates in [audit-checklist.md §3](references/audit-checklist.md), side rules in [sides-and-compliance.md](references/sides-and-compliance.md).

- **The first page for every buyer type is the all-products price guide (pt02)**, English and Chinese together. The second page follows the three-state list: list/directory sources dominate → no second page, go off-site; own-site sources dominate → a selection or comparison page; already-present sources dominate → update letters + a landing page.
- One page per intent cluster (3–6 adjacent intents); improve old pages before creating new ones.
- Pick the page type from the buyer's question shape (how much → price family; which one → selection; is it allowed / how to → questions and rules; who / where → entity facts; on what basis → primary sources). Check the side limits for that type first.
- Build in the listed block order. Put the ★ blocks exactly where the blueprint puts them: conclusion block after H1 (40–130 words, three most valuable facts), the first sentence under every H2 answerable on its own, tables for anything tabular, own sentence (for ChatGPT) and market sentence or official-basis sentence (for AI Mode).
- Gates before handoff: ≥5 exclusive checkable facts after deleting banned sentences; ≥3 outbound links to checkable originals; every number with unit, basis and date; side scan including FAQ, captions, table headers, title and meta; Chinese page hard gates (新加坡 in H1, S$ amount with GST basis in the first paragraph, a real MRT station or area in the body).
- You are the author, so you cannot be the fact checker. Hand a fact-check list (every price, registration number, clause and deadline with its source) to a person, and a compliance checklist to the licence holder. Unverifiable facts are deleted, not softened.
- Launch gate, then register 2–3 unique fact strings and one off-site target per page. Video within 14 days (8–15 min, named expert, transcript, H2 timestamps).

Outputs per page: `brief-<cluster>.md` (intents, H1/H2 questions, ≥5 exclusive facts with fact-table rows, ≥3 link candidates, banned phrases for this side), `draft-<slug>.md` (frontmatter: intent_ids, page_type, language, side; `[Source needed]` where a source is missing), `factcheck-<slug>.md` for the human checker, `accept-<slug>.md` after launch.

## Step 6 · Off-site (站外)

Goal: get correct facts onto the pages AI already cites. Most AI citations are earned media (84%); paid and advertorial content is 0.3% (cross-industry). Full chapter: https://canlah.ai/zh/playbook/off-site/

- Targets = the frozen Top 20 plus each intent's top 10, **by URL**. For each: already listed but outdated → update letter; listed with errors → correction letter; not listed and reachable → by who decides: institutions, government registers, associations, manufacturer locators first (free, share rising); bylined factual contributions to media; enquiries for listings; not reachable → monitor only.
- **Send gate** (all three, or nothing is sent): switch A authorisation on file (if applicable); a signed sign-off sheet for this batch's facts; zero hits on the banned-word list.
- Paid spots: only fixed rate cards; never lead- or commission-priced; never pages with laudatory titles on the strict side (only corrections there); every paid item marked "paid listing" in every report.
- One letter template, two follow-ups (+7, +21), then stop. No target count; never promise replies.
- Monthly: check the six kinds of decay (review counts going stale, yearly lists rewritten, old prices on directories, departed staff still listed, annual awards lapsing, third-party pages taken down). Reddit only when it is > 2% of cited URLs this month.

Outputs: citation-slot table (one row per URL: state, date, basis, judge, disposition, competitor's way in), `outreach-ledger.csv` (sent / replied / live, dates, URLs), drafted letters for the user to send.

## Step 7 · Monthly retest (每月复测)

Goal: decide next month's three actions. Details: [measurement.md §6–9](references/measurement.md).

- Same pool, engines and passes; 3 extra runs in the same week; count seats with total names; X/20 and cited Y/20; 36 brand-six runs read by a human; search stored answers for each page's unique fact strings; site health (four identities, snippet switches).
- Write "increased" only after four gates: past month 2, samples ≥80%, above the noise band, two months in the same direction.
- Seats within the noise band → triage from layer 1: door → identity → citation slots → split day and ruler → change topic. Layers 1 and 2 are checked every month anyway.
- Next month's three points, mechanically: fix door or identity (if failed) · one new reachable source cited this month · one source where the business ranks after 4th.

Report page 1: seats (with total names and noise band ±N), on the list X/20 and cited Y/20, factual errors X → Y (denominator 36), web leg overlap rates, and the fixed sentence when overlap is below 50%. Page 2 (internal only): who AI recommends, who moved, which source pushed the business down, and how competitors got in.

## Shortcuts

- **Go / no-go in half a day, no probe budget**: three questions (cost, recommendation, scenario) asked by hand while logged out; copy each answer's top 10 source URLs; count reachable URLs per question. ≥2 questions with ≥4 → go. Numbers are "coarse screen, n = 1, single engine" and never go into a contract.
- **Only three things possible**: first decide the side and save a 48-hour baseline (read-only), then (1) open the door and fix identity, (2) one all-products price guide page in English and Chinese, (3) institutional sources and a narrated long video; retest monthly.

## How to talk about results

Say: "On the model API, the business was named M times in K runs (noise band ±N)." · "On the list 5/20, cited this month 3/20." · "Factual errors fell from 4 to 1 of 36; each has a screenshot you can reproduce."
Never say: "AI will recommend you now", "seat share = market share", "up 2, trending well" (within the band), "no one is doing this", or any ROI, traffic multiple or guaranteed position.

## Full chapters (canlah.ai, English and Chinese)

| Chapter | English | Markdown for agents | Chinese original |
|---|---|---|---|
| 0 How to use; decide your side | https://canlah.ai/playbook/start/ | https://canlah.ai/playbook/start.md | https://canlah.ai/zh/playbook/start/ |
| 1 How buyers ask and AI answers | https://canlah.ai/playbook/how-ai-answers/ | https://canlah.ai/playbook/how-ai-answers.md | https://canlah.ai/zh/playbook/how-ai-answers/ |
| 2 Open the door | https://canlah.ai/playbook/open-the-door/ | https://canlah.ai/playbook/open-the-door.md | https://canlah.ai/zh/playbook/open-the-door/ |
| 3 Identity | https://canlah.ai/playbook/identity/ | https://canlah.ai/playbook/identity.md | https://canlah.ai/zh/playbook/identity/ |
| 4 Question pool, baseline, targets | https://canlah.ai/playbook/pick-questions/ | https://canlah.ai/playbook/pick-questions.md | https://canlah.ai/zh/playbook/pick-questions/ |
| 5 Writing pages: index and rules | https://canlah.ai/playbook/write-pages/ | https://canlah.ai/playbook/write-pages.md | https://canlah.ai/zh/playbook/write-pages/ |
| 5 Tier A blueprints | https://canlah.ai/playbook/page-types-core/ | https://canlah.ai/playbook/page-types-core.md | https://canlah.ai/zh/playbook/page-types-core/ |
| 5 Tier B cards | https://canlah.ai/playbook/page-types-more/ | https://canlah.ai/playbook/page-types-more.md | https://canlah.ai/zh/playbook/page-types-more/ |
| 5 Tier C and pre-publish checks | https://canlah.ai/playbook/page-types-checklist/ | https://canlah.ai/playbook/page-types-checklist.md | https://canlah.ai/zh/playbook/page-types-checklist/ |
| 5 Production at scale | https://canlah.ai/playbook/at-scale/ | https://canlah.ai/playbook/at-scale.md | https://canlah.ai/zh/playbook/at-scale/ |
| 6 Off-site | https://canlah.ai/playbook/off-site/ | https://canlah.ai/playbook/off-site.md | https://canlah.ai/zh/playbook/off-site/ |
| 7 Retest and judgement | https://canlah.ai/playbook/measure/ | https://canlah.ai/playbook/measure.md | https://canlah.ai/zh/playbook/measure/ |
| 8 A new industry | https://canlah.ai/playbook/new-industry/ | https://canlah.ai/playbook/new-industry.md | https://canlah.ai/zh/playbook/new-industry/ |
| A Evidence | https://canlah.ai/playbook/evidence/ | https://canlah.ai/playbook/evidence.md | https://canlah.ai/zh/playbook/evidence/ |
| B Templates (robots.txt, letters, ledgers) | https://canlah.ai/playbook/templates/ | https://canlah.ai/playbook/templates.md | https://canlah.ai/zh/playbook/templates/ |
| C Ten-axis values for five industries | https://canlah.ai/playbook/industry-reference/ | https://canlah.ai/playbook/industry-reference.md | https://canlah.ai/zh/playbook/industry-reference/ |
| D Number discipline and glossary | https://canlah.ai/playbook/glossary/ | https://canlah.ai/playbook/glossary.md | https://canlah.ai/zh/playbook/glossary/ |
| Dental and aesthetics edition | https://canlah.ai/playbook/dental/start/ | https://canlah.ai/playbook/dental/start.md | https://canlah.ai/zh/playbook/dental/start/ |

Every dental and aesthetics chapter is listed in https://canlah.ai/playbook/index.md. Full books as PDF: English https://canlah.ai/playbook/files/geo-playbook-general-en.pdf · https://canlah.ai/playbook/files/geo-playbook-dental-en.pdf; Chinese https://canlah.ai/playbook/files/geo-playbook-general-zh.pdf · https://canlah.ai/playbook/files/geo-playbook-dental-zh.pdf

Content © Canlah AI, CC BY 4.0. Attribute as: "GEO Playbook by Canlah AI, https://canlah.ai/zh/playbook/".
