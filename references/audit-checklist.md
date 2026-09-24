# Audit checklist · 开门五道闸、认对人、每页三道闸

Condensed from GEO Playbook chapters 2, 3 and 5.4–5.31. Full text (Chinese): https://canlah.ai/zh/playbook/open-the-door/ · https://canlah.ai/zh/playbook/identity/

**Hard gate: until the baseline is saved, change nothing.** No door, profile or facts page is edited before the question pool, the account-level Top 20, the noise band and the 36 brand-six runs are on disk (see [measurement.md](measurement.md)). The first audit is read-only: get permissions, turn on logging, record the current state. The day the door is changed is the *split day*; every before/after comparison uses it.

Why: the door and identity are multipliers of 0 or 1. If crawlers cannot read the page, or AI credits another business, every page and outreach letter is multiplied by zero. Only the shelf (being on cited pages, and having your sentences quoted) adds up month by month. 门和人是乘 0/1 的开关。

---

## 1. Opening the door: five gates (开门五道闸)

Run all gates twice in the same order: on D1 read-only, and after the baseline is saved, to fix.

### Gate 0 · Access logs (the only direct evidence)
- [ ] Day 1, one email asks for three permissions at once: **domain verification** (Search Console, Bing Webmaster Tools), **robots.txt edit rights**, **access-log export**.
- [ ] Pull 30 days of raw logs (CDN log push or server `access.log`).
- [ ] Identify crawlers by **official IP ranges, never by user-agent string**: `openai.com/searchbot.json`, `openai.com/gptbot.json`, `openai.com/chatgpt-user.json`; Anthropic's and Perplexity's published ranges. Counts by UA mix in scanners and impostors.
- [ ] Output `crawler_hits_30d.csv`: crawler · hits in 30 days · top 20 URLs hit · status-code distribution.
- Readings (record as to-fix items, change nothing yet):
  - `OAI-SearchBot` hits = 0 → the door is closed or the site is undiscovered. Never write "wrong topic" or "no demand".
  - 403 + 429 > 5% → WAF or rate rules are blocking. robots.txt will not fix it.
  - All 200 but only the homepage → sitemap and internal links.
  - `ChatGPT-User` hits present → the live-fetch path works.
  - No logs → write "no direct evidence; first table in 30 days". Never say "the door is open".

### Gate 1a · Snippet switches (nosnippet 三兄弟), 10 minutes
Google documents `nosnippet`, `data-nosnippet`, `max-snippet` and `noindex` as the controls for Search, **including AI Overviews and AI Mode**. It is the one switch that zeroes the Google leg, and CMS templates and SEO plugins often turn it on.

- [ ] Check 8 pages: home, price page, `/facts`, and five templates (service, practitioner or author page, an old blog post, a list page, a landing page). Fetch HTML and response headers.
- [ ] Three places: `<meta name="robots|googlebot">` with `nosnippet` or `max-snippet:0` / small numbers; the `X-Robots-Tag` response header (only visible with `curl -I`); `data-nosnippet` attributes on key blocks (price tables, FAQ answers, fact blocks).
- Fix (after baseline): meta → `max-snippet:-1`; header → remove at CDN/server or set `max-snippet:-1`; attribute → delete. Grep all three again until empty.
- If any hit is not fixed within four weeks, the Google leg counts as zero for the quarter. It is re-enabled by redesigns and plugin updates, so check it every month.

```bash
for u in "$HOME_URL" "$PRICE_URL" "$FACTS_URL"; do
  curl -sI "$u" | grep -i 'x-robots-tag'
  curl -s -A 'Mozilla/5.0' "$u" | grep -Eio '(nosnippet|max-snippet:[0-9]+|data-nosnippet)'
done
```

### Gate 1b · robots.txt (six-line read, four-step merge)
Six lines to record on D1 (none may be skipped):

1. The 12 retrieval user-agents, each allowed or blocked: `OAI-SearchBot`, `ChatGPT-User`, `OAI-AdsBot`, `Bingbot`, `Googlebot`, `Applebot`, `Amazonbot`, `PerplexityBot`, `ClaudeBot`, `Claude-SearchBot`, `Claude-User`, `DuckAssistBot`.
2. The wildcard group: number of `Disallow` lines **N**, copied verbatim.
3. The 6 training user-agents (`GPTBot`, `Google-Extended`, `Applebot-Extended`, `Meta-ExternalAgent`, `CCBot`, `Bytespider`) — marked "unrelated to being cited". Allowing them is a content-licensing choice.
4. Snippet switches on home and price page (gate 1a).
5. CDN/WAF: "Block AI bots" / "Bot Fight Mode" on, off or absent; rate rules; ChatGPT-User IP ranges in the allowlist?
6. Access logs: log push / access.log / none, and the date permission was requested.

What blocking does: `OAI-SearchBot` blocked → the ChatGPT leg is zero all quarter. `Googlebot` blocked → AI Overviews, AI Mode and organic ranking go together. `Applebot` blocked → Siri, Spotlight, Apple Maps and Apple Intelligence go; do not claim the Apple Business profile until it is allowed. `Bingbot` blocked → Copilot goes and ChatGPT loses one of its retrieval sources.

Four common mistakes:
- Blocking `GPTBot` "to be safe" or thinking it removes you from ChatGPT: it is a training crawler; 88.2% of sites that block it are still cited (BuzzStream).
- Treating `Google-Extended` as the AI Overviews switch: Google says it "does not impact a site's inclusion in Google Search". AI Overviews depend on `Googlebot` + the snippet switches.
- Thinking a blocked `Applebot-Extended` cuts Apple: it only opts out of training.
- "AI crawlers ignore robots anyway": Anthropic's three bots follow robots.txt. `ChatGPT-User` and `Perplexity-User` are user-triggered and may not; their real switch is the WAF.

Merge in four steps (after baseline). **Never just append named groups at the end**: the most specific group wins and all others are ignored, so a new named group silently drops every wildcard `Disallow` (admin, cart, site search) for that crawler.
1. Copy the wildcard group's `Disallow` lines verbatim; count N.
2. Write 12 named retrieval groups, each `Allow: /`.
3. Copy the N lines into every named group: N × 12.
4. Training groups listed separately (if they `Allow: /`, they also get the N lines); `Sitemap:` lines at the very end.
- [ ] Receipt sentence, word for word: "Original wildcard Disallow lines = N, copied line by line into N × 12 places (12 named retrieval groups); training groups with Allow: / also copied." Without this sentence the gate has not passed.
- Check robots.txt **on the host where the page lives** (docs, help, blog and trust subdomains have their own), download the whole file and parse it by group, and keep a per-host × per-leg table (one row per host, one column per retrieval crawler, never merged into one cell). Unreachable robots (refused, timeout, TLS failure) → "not retrieved", never guessed.
- Which group applies: a group naming the crawler applies alone; a crawler with no named group falls to `User-agent: *` ("falls to wildcard", not "blocked"); blocked means the applying group has `Disallow: /`.
- The table carries a **verification level** column: `robots-verified` or `fetch-verified`. `fetch-verified` means a fetch with that crawler's UA returned 200 and contained the body sentence found with the browser UA; it is a reachability receipt, not a gate 2 pass. A fetch receipt is only "fetched 200 + body text found" or "fetch blocked (<status>)", never "allowed". Robots not blocked and nothing fetched → "robots not blocked, fetchability unverified". robots lifts only the protocol ban; client-side rendering and WAF or geo rules (403, captcha, redirect) are separate gates.
- Training crawlers (`GPTBot`, `Google-Extended`, `Applebot-Extended`, `Meta-ExternalAgent`, `CCBot`, `Bytespider`) do not go in this table.

### Gate 1c · WAF (the real switch for ChatGPT-User)
OpenAI: because these fetches are initiated by a user, "robots.txt rules may not apply".
- [ ] Screenshot the "Block AI bots" / "Bot Fight Mode" state.
- [ ] Move verified bots out of rate-limit rules; note the 429 share from gate 0.
- [ ] Allowlist the IP ranges in `openai.com/chatgpt-user.json` (rule name `allow-chatgpt-user`). For Perplexity-User, allowlist its published ranges.
- [ ] D+7: re-pull logs and look for `ChatGPT-User` hits.

### Gate 2 · Four identities (四身份实抓), read-only
Look at the same URL through four independent paths; keep four separate receipts.

| Identity | Where | Pass | Proves |
|---|---|---|---|
| a · the real crawler | gate 0 logs, filtered by official IP ranges | URL hit by `OAI-SearchBot` in 30 days **with 200** | the only direct evidence |
| b · Bing's HTML | Bing Webmaster Tools → URL Inspection → Live Test source | price number and body text found by string search | Bing/Copilot leg; closest free sample of a non-rendering crawler |
| c · Google's HTML | Search Console → URL Inspection → crawled page HTML | same | Google side only (Google renders); never conclusive alone |
| d · ChatGPT live path | paste the URL into ChatGPT: "Open this link and copy the line with the price, word for word" | quoted **verbatim** | the `ChatGPT-User` path works |

`curl` is a troubleshooting tool, not a fifth identity, and is read twice: (1) with a normal browser UA, to see whether body text and prices are in the HTML (client-side rendering has nothing to do with UA); (2) with the `OAI-SearchBot` UA, **status code only**, to spot a WAF. Mark both screenshots "troubleshooting only, not a pass criterion". Faking a crawler UA and reading the content misleads both ways.

Reading the differences: a hit with 200 → pass. a all zero → door closed or undiscovered. a 403/429 > 5% → WAF. No logs → if c passes and b fails → client-side rendering (open an SSR / prerender ticket; no new content pages this month); if b and d both pass → "pass, downgraded: no direct evidence, add a in 30 days"; b passes, d fails → WAF; other combinations → no conclusion. **Google has seats but ChatGPT has zero → check client-side rendering first, not topics.**

Main AI crawlers do not execute JavaScript; the exceptions are Gemini (Google infrastructure) and Applebot. Prices, core facts and body text must be in server-rendered HTML. Anything behind a login or quote wall does not exist for AI: publish a public summary page.

```bash
# (1) content check with a browser UA: body text and price must be in the raw HTML
curl -s -A 'Mozilla/5.0 (Macintosh)' "$URL" | grep -c 'S\$[0-9]'
# (2) status code only with the crawler UA (WAF check, not a pass criterion)
curl -s -o /dev/null -w '%{http_code}\n' -A 'OAI-SearchBot' "$URL"
```

### Gate 3 · Indexing paths and free first-party AI data
- [ ] D1: connect the Search Console generative AI report and Bing Webmaster Tools AI Performance; export and screenshot each. **Verify the site field**: a misconfigured tool silently reads another site and still returns OK, which is worse than not connecting it.
- [ ] Bing leg: `site:` check per page; submit missing pages via IndexNow (it feeds Bing and Yandex only; it is not a ChatGPT switch).
- [ ] ChatGPT leg: claim Foursquare (category chosen from the official category tree) and Yelp, correct business status; verify with identity d. Bing indexing is not evidence for the ChatGPT leg.
- Free first-party data comes before any paid probing.

### Gate 4 · JSON-LD, sealed once in half a day
Real-time fetches by the five major systems read no JSON-LD, and hidden Microdata/RDFa are ignored; one study found AI Overview citations fell 4.6% after pages added JSON-LD (the only significant effect). Schema is set once, not maintained per page.
- [ ] One template: Organization (or the industry subtype) + a Person per practitioner + `sameAs`.
- [ ] Only four things must be right: legal name matches `/facts` exactly; address and phone match the five business profiles exactly; each practitioner's registration number; the `sameAs` list (register lookup pages, association profiles, Google and Bing business pages, ORCID/Scholar, speaker pages, LinkedIn, Wikidata QID).
- [ ] A comment in the template: "indirect, Google leg only, low confidence".
- ✗ No FAQPage stacking for rich results; ✗ no `aggregateRating` self-ratings.

### Door acceptance (all ten, or the door is not open)
- [ ] Crawler hit table complete (or a red blocker with a due date)
- [ ] Snippet switches: three places empty, 8 screenshots
- [ ] robots.txt: 12 named retrieval groups, receipt sentence with N × 12
- [ ] `Sitemap:` at the end
- [ ] WAF rule `allow-chatgpt-user`, screenshot; `ChatGPT-User` hits after 7 days
- [ ] Four identities, four separate receipts; both `curl` reads screenshotted and marked
- [ ] Bing AI Performance and Search Console generative AI report connected
- [ ] JSON-LD template sealed
- [ ] Every launched page passed the launch gate (§3)
- [ ] The door triage is on the monthly schedule

Monthly door triage when seats have not moved: (1) real `OAI-SearchBot` hits and status codes, (2) snippet switches re-enabled?, (3) the four HTML copies identical, (4) Bing `site:` indexing, (5) ChatGPT quotes the price line verbatim from the pasted URL. Any failure is a door problem, not a topic problem: fix the same day, recheck in 7 days, no topic change and no new pages this month.

Full chapter: https://canlah.ai/zh/playbook/open-the-door/#g2-2-9-门层排查与本章验收

---

## 2. Identity: make machines sure it is this business (认对人)

Errors AI repeats (price, address, hours, registration number, practitioner names and credentials, whether the business has closed) are usually copied from outdated third-party pages. Fixing identity is often the fastest lever (observed, confidence 70%, never promised). The one hard number: **factual errors X → Y**.

Five fixed moves, in order (sameAs always last): unique spelling → `/facts` page → six-trace alignment → same-day corrections → sameAs.

### Two-hour checklist (after the baseline is saved)
| Time | Output | Do the full version if |
|---|---|---|
| 0–25 min | `entity_errors.md`: read the frozen 36 brand-six answers, list errors and negatives (no new probe run) | any factual error, mistaken identity or negative/excluded tendency → fix it the same day |
| 25–55 min | `facts-table.csv`: 14 rows, each with source / verified date / publishable? / owner | regulated side with public prices → check each price against the internal price list export, not the old website |
| 55–75 min | `profiles-5.csv`: five profiles present / absent / squatted; URL points to the canonical domain? | two domains, renamed, moved, or a profile URL pointing to the homepage |
| 75–95 min | re-check the gate 1 receipts | anything blocked, or "Block AI bots" on → back to the door; page work waits |
| 95–110 min | verify the reporting tools' site fields | wrong site field = not done |
| 110–120 min | `exclusions.md`: topics not mentioned, prices not public, banned phrases | switch A without written authorisation → no external letter at all |

Skip to a 30-minute version only if all four hold: single location and single practitioner; no namesake, no rename or move; zero factual errors and non-negative tendency at baseline; prices already in fixed form. Write the decision on the first line of the week's work order.

### The 14-row fact table (the single source of truth)
Legal name (exactly as registered, including case and suffix) · company registration number · licence or registration number + official lookup link · practitioners (name + registration number + lookup link) · address (one line + postcode, identical to the five profiles) · phone (identical) · opening hours (day by day, never "by appointment") · year founded · service languages · main services (no adjectives) · devices and materials (real brand and model; strict side: model only, no vendor link) · insurance and subsidy scope (definite sentences) · rework and replacement policy (period, times, what is included; no "free") · last verified date (YYYY-MM-DD).

- `/facts` page: own URL, in the sitemap, linked from the site footer; plain HTML `<table>` or `<dl>`, never an image, PDF or JS. Blueprint: [page-types.md](page-types.md) pt09.
- On a price change: `/facts`, the thick pages' price tables and the five profiles change the same day, and update letters go to third-party pages that list the old price.
- Test: fetch the source with a browser UA; price and registration strings are found; 100% match the fact table.

### Person pages and six-trace alignment
- One page per named practitioner at `/team/<name>`: on the regulated side this is the main line, because practitioners may state qualifications, scope, schedule and contact details. Still subject to the regulator's rules (true, accurate, verifiable, no exaggeration, no persuasive language, no comparison, no disparagement); never describe it as a back door around ad limits.
- Three spellings are three entities. Align name spelling, registration number, legal name and address across six traces: official register, association profile, business website team page, conference/speaker page, professional social profile, academic ID (if any). The official register is the source; fix it first.
- Send a correction for every mismatch the same day; follow up at +7 and +21.
- Namesake contamination: add one exclusive definition sentence to the top of `/facts` (product name + category noun + legal entity + location), and use it as the first sentence in all six traces.
- Staff leave: keep the page, mark "formerly", update all six places the same day; keep register/association/academic `sameAs`, delete any link to the new employer's page. There is no "301 for a byline".

### Five business profiles (an entry ticket, not a lever)
Claim in this order (by which engine benefits first): Foursquare → Yelp → Google Business Profile → Bing Places → Apple Business Connect (only once `Applebot` is allowed). The **URL field** is the only field with leverage: point it to the landing page for that buyer type, never the homepage. Every free-text box, Q&A, post and photo caption is advertising and follows the same word list. Monthly three-state check (about 20 min): present · URL correct · facts unchanged by third parties or the platform. Never tell a client that completing profiles makes ChatGPT recommend them.

### Wikidata (conditional) and Wikipedia (do not edit)
Create a Wikidata item only if one of these exists: independent press coverage, a journal byline, or an association announcement; attach ≥3 external references; re-check after 30 days that it was not nominated for deletion. Never edit Wikipedia body text to add the business or its links; self-citation is reverted and leaves a trace.

### Brand six questions (品牌六问, the only definition)
| # | Question | Tests | External use |
|---|---|---|---|
| 1 | `<legal name>` — what do they do? | identity | yes |
| 2 | Is `<legal name>` reliable / any good? | tendency | yes |
| 3 | Where is `<legal name>`, opening hours, phone? | basic facts | yes |
| 4 | How much does `<legal name>` charge for `<main service>`? | price errors (the most valuable) | yes |
| 5 | Does `<legal name>` have complaints / bad reviews / disputes? | negatives | yes |
| 6 | `<legal name>` vs `<competitor>`, which is better? | comparison | **no, internal only** (names a third party) |

6 questions × 3 rounds × 2 engines = **36 runs a month, frozen all quarter.** Chinese versions of Q1 and Q4 are a separate ruler (2 × 3 × 2 = 12, denominator 12, printed on its own line with "wrong-anchor" count). Log each answer on four dimensions, read by a human: identity (this business / namesake / merged / unknown), facts (each error mapped to a fact-table row), tendency (positive / neutral / negative / excluded), source (every URL under the answer).

Correction timeline: notify within 1 working day (screenshot + sampling spec) → fix the sources you control within 3 working days (`/facts`, profiles, site pages; before/after screenshots) and send a named correction letter to each third-party page with the error (point out the error, link to `/facts`, never mention rankings or promote) → follow up at +7 and +21 → re-ask the same question on the next monthly run. Whether a third party accepts is theirs to decide; never promise it.

Fix immediately (do not wait for the monthly report) when: a factual error appears in the brand six; mistaken identity or merged entity; negative or excluded tendency; a new third-party error in the monthly check; the client or a customer reports one. Wording changes, rank changes and seat fluctuations go into the monthly report.

Before/after screenshots: same question, engine, region setting and time of day; the caveat burned into the image ("single sample · single engine · directional, not acceptance evidence; the same question gives different answers at different times"); no causal wording; a "try it yourself" card with the exact question, engine and region steps. Never claim "I made the AI change its answer".

Full chapter: https://canlah.ai/zh/playbook/identity/

---

## 3. Every page: launch gate, three mechanical gates, content gates (每页三道闸)

### Three mechanical gates (any failure stops the next page)
1. **Ranking gate** — pages go live in order of annual opportunity value (see [measurement.md](measurement.md)). A change of order needs a written reason, and only two reasons count: legal or internal blockage; the three-state list moved this buyer type's effort off-site.
2. **Language gate** — English and Chinese pages are finished together, never saved up for the end of the quarter (saved-up pages become translations, not landing pages).
3. **Video gate** — within 14 days of launch, an 8–15 minute video narrated by the named author on camera: title = the page's main question + place + year; description = page URL on line one, full transcript, author page URL; timestamps per H2, worded exactly as the H2s. No AI voice-over, no slides instead of a person, no paid views, no jump cuts or music. Without it the page is marked "video missing" and the next page does not start.

### Content gates (before the page is written up)
- [ ] One intent cluster per page (3–6 adjacent intents); variants go into H2s of the same page; improve an old page before creating a new one (URL, H1 and paragraphs that rank stay; at most double the body).
- [ ] **Conclusion block**: after H1, before the first H2, 40–130 words, the page's three most valuable checkable facts (fixed tiered price; registration number with lookup link; process duration and number of visits), identical to the body sentences; no "this article will".
- [ ] **Density gate**: first delete every sentence that hits a ban, then count **≥5 exclusive checkable facts** that exist nowhere else and would change a buyer's choice. Fewer than 5 → go back and pick another intent cluster; never keep a banned sentence to make up the count.
- [ ] **Source gate**: ≥3 outbound links to checkable originals (rule text, register lookup, government fee or subsidy page; vendor spec pages except on the strict side).
- [ ] Every number: unit, threshold, basis; result numbers pass the six checks; the conclusion's numbers match the table.
- [ ] Three separate dates: price check date (as of <date>, reviewed every 30 days), regulation check date, `dateModified` (only for substantive edits, identical to the visible "updated" date).
- [ ] Chinese page hard gates: H1 contains 新加坡 (the country); the first paragraph has an S$ amount with GST included or excluded; the body names at least one real MRT station or area. H2s are rewritten from Chinese buyer questions, not translated.
- [ ] Compliance: side-by-side scan of the banned-word list (English and Chinese), including FAQ, captions, table headers, title and meta description; plus general red lines: traffic multiples, ROI, conversion lift, "guaranteed #1", "exclusive", "independent review", and leaking method details (probe settings, question lists).
- [ ] Non-author fact check: prices, registration numbers, clause text and statutory deadlines read back 100% word for word; everything else machine-scanned plus a 30% sample (any false item → recheck the whole page). If a fact cannot be verified, delete it.
- [ ] Licence-holder compliance sign-off. No exceptions, under any deadline.

### Launch gate (a page is "live" only when all pass)
- [ ] Same day: open in a private window with a hard refresh and see the new H1.
- [ ] Same day: four HTML copies (`OAI-SearchBot`, `Bingbot`, `Googlebot`, a browser) all contain the same body paragraph and price string. Serving machines a different version can be judged as manipulation.
- [ ] Same day: IndexNow ping receipt (Bing leg only).
- [ ] D+7: ask ChatGPT for one exclusive fact from the page, or paste the URL and have it quote the price line verbatim; screenshot. n = 1 is valid: it tests whether the page was read, not its rank.
- [ ] Register: intent cluster, buyer type, URL, launch date (= this page's split day), version, 2–3 exclusive fact strings for the page-level signal, and one off-site target ("which source should cite this page"), which must become a sent letter or "not reachable + reason" within 14 days.
- D30 / D60 / D90 comparisons use the same question pool, engines and number of passes.

Full references: https://canlah.ai/zh/playbook/open-the-door/#g2-2-8-每页上线闸 · https://canlah.ai/zh/playbook/write-pages/#g5-5-4-三十天写页顺序与三道机械闸 · https://canlah.ai/zh/playbook/write-pages/#g5-5-8-结论块-密度闸-出处闸 · https://canlah.ai/zh/playbook/page-types-checklist/#g8-5-31-交稿-每页五步-撒谎红线与自检
