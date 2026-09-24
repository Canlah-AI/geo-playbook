# Measurement · 三个数、噪声带、每月流程

Condensed from GEO Playbook chapters 1.2–1.3, 4 and 7. Full text (Chinese): https://canlah.ai/zh/playbook/pick-questions/ · https://canlah.ai/zh/playbook/measure/

Principle: **a number without a noise band is not a number** (没有噪声带的数字不是数字). The monthly result is not "effective / not effective" but **the next three things to do**, plus three numbers that do not depend on AI randomness.

## 1. Name the rulers correctly

| System | Ruler | Report name (use exactly) |
|---|---|---|
| OpenAI model API | seat count on the frozen question pool | "Model-API visibility baseline · OpenAI leg" |
| Gemini model API | same | "Gemini model leg" |
| AI Overviews and AI Mode | Search Console generative AI report impressions only | — |
| ChatGPT web interface | web control leg, calibration only, never acceptance | — |

- Never call an API reading "what users see in ChatGPT" or "real user visibility". API and web citations differ systematically (not noise; more runs do not remove it). If you only have API evidence, say "on the model API".
- **Gemini API ≠ AI Overviews ≠ AI Mode.** Different retrieval, answer generation and source pools. Do not use one to accept another.
- Never add the rulers together or merge them into one visibility score: when they are summed, one getting worse is hidden by another.
- Probe models are pinned and do not follow whatever model you use day to day. The OpenAI leg calls the official API directly (a proxy measures something else). The Gemini leg may use a proxy pool, but must pin an exact model (floating aliases can fail and empty the month). Change models only by decision, and on all legs at once; a model change is a ruler change.

## 2. The three numbers (三个数)

| Number | How to count | Win criterion | Print with it |
|---|---|---|---|
| **Seats** 席位数 | Times the business is named in this month's N answers on the frozen pool; also record total names in each answer and each competitor's seats | Increase above your own measured noise band, same direction two months running | Total names and seat share; seats scale linearly with the number of passes, so never compare across different pass counts |
| **On the list and cited, X/20** 在册且被引 | Of the 20 third-party pages AI cites most on this pool (frozen at baseline), how many show the business **and** were cited this month; open each and screenshot. Report two lines: on the list X/20; on the list and cited this month Y/20 | Baseline is usually 0–2; +1 a month; ≥ +3 in 90 days | On the list ≠ cited. If "on the list" rises and "cited" does not for two months, you are investing in containers that are not cited: next month, only target sources cited this month |
| **Factual errors** 事实错误条数 | Brand six questions (6 × 3 rounds × 2 engines = 36 runs/month), read by a human; every wrong address, price, status or credential, with screenshot | Down to 0, each fix with before/after screenshots | The hardest number: errors are copied from source pages, so fixing the source moves both engines. **If you watch one number, watch this one** |

Plus: Search Console generative AI impressions (impressions only, no names or positions; already inside total impressions, never add them; blanks exported as 0 must be flagged).

Seats can be split (answer shelf vs shopping shelf, each with its own noise band); denominators can be split by line of business when their named sets barely overlap; factual errors can be split into own-source vs third-party. Definitions never change.

## 3. Question pool: 30 questions, frozen for the quarter (题池)

The pool is the ruler. Pool quality caps project results.

- **Read free data first** (half a day): Search Console generative AI report, Bing AI Performance (cited pages, grounding queries, citation share), and buyers' exact words before their last 15 purchases (from front desk or CRM; if none are recorded, make the fields "How did you find us?" and "What did you most want to ask?" mandatory now).
- **Only four sources, each with evidence** (link or screenshot): **A** buyers' own words before purchase · **B** keywords in active ads · **C** real platform queries (Search Console queries, Google autocomplete, related questions, Bing grounding queries) · **D** questions already listed on competitor comparison pages, directories and list pages. **Never let AI invent questions**; AI-written questions poison the ruler itself. Anything without evidence goes to a reserve pool (topic ideas only). Fewer than 10 A-type questions → downgrade to audit plus monitoring.
- **Ratios are fixed** (a baseline that breaks them is void):

| Line | Count of 30 | Rule |
|---|---|---|
| With a location (e.g. "in Singapore", "near <area>") | 18 | at least 60% |
| With price or cost words | 9 | at least 30% |
| Bare category words | 3 | at most 10%, control only |

  Bare words can fake a zero: asking only "divorce lawyer", AI Mode listed no firms in 10 cities; adding "near me" restored 38/38 (PRWeb, overseas sample).
- By question shape, in parallel: which one / best (10) · how much (8) · A vs B (6) · scenario, including second opinions (4) · brand direct (2).
- Chinese buyers → Chinese questions are a main line, all with a location; they count inside the location and price numerators, not as extra. When ratios cannot be met, cut bare words first, never Chinese questions. A minority language whose results all point to another country is the wrong target: swap it for a Chinese question.
- A non-author counts the ratios and signs "ratios verified · date · name"; the decision-maker reads every question aloud, edits on the spot and signs. **Changing a question is changing the ruler.**

## 4. Baseline: coarse screen, full rounds, noise band, web control leg

1. **Validate the ruler**: run a question that is known to be cited; if the probe cannot catch it, stop. Lock region and language; never give the AI your own URL.
2. **Coarse screen**: 30 questions × 1 round × 2 engines = 60 runs. **Dead pile**: neither engine names any business (only general advice) → out; a second person re-reads before it is final; up to 3 may be lifted back. Say "no business named in the coarse screen (n = 2)", never "zero visibility". **Battlefield pile**: businesses named, you are not. **Hold pile**: you are named.
3. **Full rounds**: battlefield + hold × 5 rounds × 2 engines.
4. **Noise band**: same questions, engines and passes, re-run **3 times in the same week**. Noise band = max − min of the three seat counts, **floor ±1 seat** (even if all three match). From month three, the baseline band is the median of three months, never the maximum (a maximum only ratchets up and makes any improvement impossible to declare). If the band widens two months running, add passes and start a new baseline.
5. **Brand six** in the same week: 36 runs. The only source of the factual-error baseline; no quick runs.
6. **Web control leg, before freezing the Top 20**: 5 fixed questions from the pool (≥2 "which one / near me", ≥1 price, the rest from the battlefield pile), typed by hand into ChatGPT's web interface, logged out or in a temporary chat, personalisation and memory off, from an IP in the target market, 1 pass each, no re-runs, full screenshots including the sources area, transcribed into `web_leg_<month>.csv`. Domains that appear only on the web leg are **forced into the candidate pool**.
7. **Freeze the account-level Top 20**: from the raw `domains_cited` of the full rounds (not a version with your own site or generic domains removed), merged with the web-only domains, ranked by URL-level citation count; mark `web_only=Y`. A second person spot-reads 3 pages. This is the X/20 denominator and the off-site target list for the quarter.
8. **Sign the control agreement**: same-site pages not to touch, three competitors, which number is primary, when to stop.

**Baseline saved = account-level Top 20 + noise band + 36 brand-six runs, all on disk.** Only then may the door, profiles and facts pages change.

Record for every answer: who is named, whether you are, position; total names in that answer; source types (official site, directory, list page, review site, map, forum, government, media; listicles counted separately); whether review counts or stars appear in the answer (recommendation vs non-recommendation questions on separate lines); Reddit share; valid vs failed samples (failed removed from the denominator and listed); URL-level vs answer-level counts; tendency (negative or excluded → fix today). Write counts as "asked K times, named M times", never small per-question fractions.

**Two different "present"**: *listed as a source* (the page appears under the answer; measured by X/20; fix: get onto the page) vs *written into the answer* (AI writes your name or number in the text; measured by seats; fix: rewrite the sentences, adding pages does not help). Never merge them.

Two overlap rates from the web leg (5 questions only, union as denominator): named-set overlap and source-domain overlap. If either is below 50%, print this sentence unchanged: "This month the two paths diverge (named overlap X%, source overlap Y%). The seat changes below were measured on the model API and are not extrapolated to what real users see on the web." Never use the web leg to claim "visible" or to count seats.

## 5. Choosing targets (选点)

- **Annual opportunity value** = price per order × gross margin × monthly capacity cap × 12, from the business's own books; for ranking only, never shown as a revenue forecast or multiplied by seats. Capacity is a hard cap.
- **Three gates per candidate**: (1) does the answer name any business at all (not "are we named")? (2) are there **≥4 reachable URLs** in this intent's own top 10? (3) can the business serve and profit from the buyers it brings?
- **Four states per URL** in the intent-level top 10 (by URL, not domain): *already present* · *reachable* (accepts listing, submission, claim, nomination or correction, with a provable entry point) · *to ask* (send one enquiry; no reply in 7 days → not reachable; must be cleared before baseline) · *not reachable* (government registers, Wikipedia body, competitor domains, platform-edited pages, closed ratings). Log state / date / basis / judge; an empty basis counts as "to ask".
- A URL is **reachable enough** only if all four hold: present or reachable; allowed on this side; has an email or public entry; free or with a published rate card. The intent continues only with **≥4 such URLs across at least two classes** (2 classes × 2 each); otherwise it is dropped for the quarter (after one retry from a different angle: turn a policy question into an execution question).
- Quarter slots: slot 1 brand / correction; slot 2 the highest-value hold question; then by annual opportunity value; national bare keyword at most one, last. Pure symptom questions are out (AI cites public health sites and encyclopaedias).
- Two denominators, never mixed: **account-level Top 20** (all intents, frozen, used only for X/20) vs **intent-level top 10** (per intent, used for gate 2, the abstain line and triage).

Go / no-go in half a day with no probe budget: three questions (cost, recommendation, scenario), asked by hand while logged out; copy each answer's top 10 source URLs (three lists, never merged); count reachable URLs per list. ≥2 questions with ≥4 → go; exactly 1 → start with one buyer type; 0 → retry from another angle, then stop or downgrade. Label every number "coarse screen, n = 1, single engine, <date>, not for external use".

## 6. Every month (每月十步, about 12.5 hours)

1. First-party data: Bing AI Performance + Search Console (0.5 h)
2. Retest: same pool, engines, passes (2 h)
3. Noise band: 3 more runs in the same week (1.5 h)
4. Count seats: names, positions, total names + page-level signal (1.5 h)
5. List check: open the frozen Top 20; X/20 and cited this month; tag five binary features per URL (price table / side-by-side comparison / author with credentials / visible update date / FAQ); features on ≥60% become mandatory specs for next month's pages (1.5 h)
6–8. Profile consistency, 36 brand-six runs read by a human, site health (four identities, snippet switches, canonical, index status) (2.5 h)
9. **Triage** (below) → next month's three points (1 h)
10. Monthly report on a fixed date (2 h)

The web control leg (40 min) runs on its own day at the start of the month.

**Page-level signal** (the only page-level causal signal): at launch, register 2–3 fact strings unique to that page (e.g. an exact price like `S$6,800`); each month, string-search the stored answer texts. Found = that page was read and trusted. n = 1 is valid.

**Four gates before writing "increased"**: months 1–2 → list side by side only ("noise band baseline not yet stable, K/3 months recorded"); any leg below 80% of planned samples → "instrument incomplete", no comparison; increase within the noise band → "within normal variation, cannot be determined"; above the band but only one month → "above the band this month, to be confirmed"; above the band two months in the same direction → "increased".

## 7. Not-moved triage (没动分诊)

**Trigger (the only one): the month's seat increase is within the noise band.** Whether X/20 rose is irrelevant; a trigger must never contain a variable you control. Start at layer 1, never skip. Layers 1 and 2 are checked every month regardless, because their failures are silent.

| Layer | Check | Verdict and action |
|---|---|---|
| 1 · Door | logs (real `OAI-SearchBot` hits, status), snippet switches, four HTML copies identical, Bing `site:`, ChatGPT quotes the price line, Foursquare/Yelp status | Any failure = door problem: fix today, recheck in 7 days, no topic change, no new pages |
| 2 · Identity | brand six read by a human: right business? names, address, registration, prices right? namesakes? negatives? | Wrong → all page work is void until fixed; fix six controlled sources, send corrections; tag each error as third-party page vs business profile |
| 3 · Citation slots | intent-level top 10 against the target table | entry gone → shelf changed, go after the new source first · basis missing → fill it in, recompute · fewer than 2 reachable → wrong target, drop this intent |
| 4 · Split day and ruler | page live < 2 weeks; URL changed; bare-word questions; engine/model/passes changed; band wider; web overlap < 50%; a leg < 80% samples | Any hit → recompute or mark "instrument defect", this month does not count; the defect excuse cannot be used two months running |
| 5 · Change topic | layers 1–4 all pass and still no movement | Change the battlefield, not the wording |

Never write "no demand" without passing layers 1–4. Two months stuck on the same layer is an execution problem.

**Next month's three points**, assigned mechanically, stop at three: point 1 = fix door or identity (if layer 1 or 2 failed; no new content pages that month) · point 2 = one new reachable source cited this month where you are absent (highest citation count; competitor entry ≠ platform-edited) · point 3 = one source where you are listed but ranked after 4th (update letter). If still short: professional services → thicken the educational page for the weakest billing intent; consumer services → profile and fact fields (strict side: never a review task); then price-page expansion; then the Chinese page or a long video.

**Reddit**: each month, Reddit URLs ÷ all cited URLs. > 2% → one Reddit task this month; ≤ 2% → record only; > 2% two months running → add to the regular rhythm. One month's swing is never a long-term rule.

## 8. Changing the ruler (量具纪律)

| Change | Consequence | Allowed |
|---|---|---|
| Engine, model (including minor version), questions, pool, ratios | new ruler | start a new baseline, marked "not comparable with the previous one" |
| Number of passes | seats scale linearly | new baseline; old and new never added or drawn on one chart |
| The 5 web-leg questions | new calibration | not within a quarter |
| Brand six composition or rounds | factual errors not comparable | frozen all quarter |

Re-freeze the Top 20 in the month when **≥6 of its URLs show a visible update date later than the freeze date**; start a new segment and never draw old and new X/20 as one line. For shelves with predictable rewrite windows (e.g. sales seasons), either measure outside the window or keep separate noise bands for normal and window phases, and write the phase on the baseline file's first line.

## 9. Words that are never used (四句不许说)

| Never say | Say instead |
|---|---|
| "We're on the list, so AI will recommend us" | On the list X/20, of which cited this month Y/20 |
| "Seat share 1.29% = market share 1.29%" | Asked K times, named X times, noise band ±N |
| "Up 2 seats, heading the right way" (within the band) | Within normal variation, cannot be determined |
| A combined "visibility score" | Each ruler on its own line with its limitations |

At the 90-day settlement, also never: "another three months and it will rise", "the industry average is six months", "the data is trending up" (when seats are within the band and X/20 did not rise). No rankings or citations are ever promised; the deliverables (pages live, profiles complete, door fixed with crawl evidence, monthly answer comparisons) are the only hard commitments.

## 10. Day 90 (九十天结账)

Three points (start, D60, D90) with the same pool, engines and passes; a wider 10-pass sample is stored separately and never enters the before/after comparison; noise band re-measured; X/20 screenshots; a stop list (pages asked 30+ times and never cited). Decision: seats above the band or cited pages +3 → expand to the next batch of questions · deliverables incomplete → finish them first · all layers pass, nothing moved → hold position and say so plainly · stuck at layer 3 (not reachable) → wrong target, replace the intent · the business will not publish a checkable price or cannot edit its site → hold position only (on the strict side, judge "no price" by tiered fixed prices, not by ranges).

Full chapter: https://canlah.ai/zh/playbook/measure/#g11-7-4-守位与九十天结账
