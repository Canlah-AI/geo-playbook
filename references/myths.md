# Myths · 常被当 GEO 卖的五样

Condensed from GEO Playbook 1.4 and the quick guide. Full text (Chinese): https://canlah.ai/zh/playbook/how-ai-answers/#g1-1-4-不要做的三类事

Use this file when a user, a vendor pitch or an existing plan proposes one of these. Say what the evidence shows, then move the budget back to the five steps. Do not attack whoever sold it; do not name them.

## The five things sold as GEO (don't pay for them yet)

| What you will hear | What the evidence says | What to do instead |
|---|---|---|
| "You need llms.txt." | Removing llms.txt from a citation-prediction model made its predictions *more* accurate (SE Ranking); Google's AI optimization guide says AI Overviews and AI Mode do not need it. | Skip it. Spend the time on the door (gate 1) and on visible HTML facts. |
| "Add structured data to every page." | The five major AI systems read no JSON-LD when fetching live; hidden Microdata and RDFa were ignored and test prices were taken from visible HTML (searchVIU). After pages added JSON-LD, AI Overview citations fell 4.6%, the only significant effect (Ahrefs, 1,885 pages vs 4,000 controls). | Write every fact in visible HTML, one field per line. Set up one schema template when the site is built (Organization + Person + sameAs) and stop. Schema is not useless: it helps Google's knowledge graph indirectly. |
| "Pay for directories, listings and advertorials." | 84% of AI citations come from earned media (27% from news); paid and advertorial content is 0.3% (Muck Rack, 25M links, cross-industry, not validated in Singapore). Paying changes none of the words about you on the cited pages. | Bylined factual contributions, update and correction letters, official registers, association profiles, manufacturer locators. Paid spots only at fixed rate cards, marked "paid listing" in every report. |
| "Chase video views." | Views, likes and subscribers correlate about −0.03 with citation (a 1.7M-data-point public study). What matters is text around the video: 94% of YouTube AI citations go to long videos and timestamped videos are cited repeatedly. YouTube mentions correlate 0.737 with AI Overview visibility (Ahrefs; correlation, not causation). | An 8–15 minute video narrated by the named expert, full transcript in the description, timestamps per H2. Judge it by whether AI repeats what was said, not by views. |
| "Block GPTBot and you're out of ChatGPT" (or "block it to protect yourself"). | GPTBot is a training crawler; 88.2% of sites that block it are still cited (BuzzStream). ChatGPT search uses `OAI-SearchBot`; live fetches use `ChatGPT-User`, whose real switch is the WAF. | Decide training crawlers as a licensing question. Make sure `OAI-SearchBot` and `Bingbot` are allowed and the WAF lets `ChatGPT-User` in. |

## Also: things that do not move rankings (做了不动排名)

| Don't | Do instead |
|---|---|
| Treat `sameAs` as the main entity lever | A visible `<dl>` with one field per line + clickable links |
| Stack FAQPage schema, add self-ratings | Question-style H2s + a short FAQ at the end of the page |
| Keep a six-category ledger of citation sources | Assign work by page type (comparison / article listicle / category directory / profile / government register / review site / community / own site) |
| Notarised screenshots or permutation tests at baseline | Store raw answers + measure the noise band |
| Put pure symptom questions in the pool | Symptom + option + price questions |
| Build one page per wording variant | Variants become H2s of the same page |
| Spend 3–4 hours on a "positioning statement" | Write six answer sentences for the first intent cluster; AI reads HTML, third-party pages and knowledge graphs, not your strategy documents |

## Things that make it worse (做了会变差)

| Don't | Do instead |
|---|---|
| Append allow groups to the end of robots.txt | Copy the wildcard group's N `Disallow` lines into every named group (N × 12) |
| Rewrite old pages | Only expand them: URL, H1 and ranking paragraphs stay; at most double the body |
| Edit Wikipedia body text to add yourself | Only add checkable sources to existing entries, without your name |
| Create a Wikidata item with no third-party sources | Wait for press coverage, a journal byline or an association notice |
| On a regulated side: request reviews, buy list spots, write "from" prices | Check the side rules first ([sides-and-compliance.md](sides-and-compliance.md)) |
| Send out materials that name competitors | Keep them internal |
| Change questions, engines or passes mid-quarter | Keep frozen what was frozen |

## Wrong criteria that hide the cause (会让你查不出原因)

| Wrong criterion | Right one |
|---|---|
| `curl` with a faked crawler UA and read the content | Browser UA for content; crawler UA for status code only |
| IndexNow as the ChatGPT switch | Paste the URL into ChatGPT and have it quote the price line |
| "Is GPTBot blocked?" | "Is OAI-SearchBot allowed?" |
| `Google-Extended` for AI Overviews | `Googlebot` + snippet switches |
| Adding the engines into one score | Three lines, never added, never used to confirm each other |
| API results described as what users see | "On the model API" |
| "69% of AI crawlers don't execute JS" | No execution evidence at all; exceptions are Gemini and Applebot |
| Bare category words as most of the pool | Location ≥60%, price ≥30%, bare ≤10% |
| One run, one engine → "zero visibility" | n ≤ 3 on one engine is directional only |
| X/20 rose, so skip triage | Seats within the noise band → triage from layer 1 |

## Two disciplines

1. **Tag every action ①, ② or ③** — ① put your words onto pages already cited; ② get your own page into the candidate set (door open + high-density page type + checkable numbers + sources + visible update date); ③ make the words about you consistent (unique spelling, `/facts`, person pages, six traces aligned, corrections). An action that cannot be tagged is deleted, however much it looks like marketing (proposal decks, competitor tables, repositioning, social posts).
2. **Confidence** — a low-confidence action is still written down, marked "not measured". An action whose mechanism cannot be tagged ①②③ is not "not measured"; it is "does not hold". Never mix the two.
