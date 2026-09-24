# GEO Playbook · agent edition

**A field-tested method, packaged for AI agents, for getting a business named in AI answers (ChatGPT, Google AI Overviews and AI Mode, Perplexity) without promising rankings.**
一套有实测依据的 GEO 方法，打包成 AI 助手能照着执行的 skill：让 AI 在回答买家问题时更可能点到你的名字。不承诺排名。

By [Canlah AI](https://canlah.ai) · Singapore · v1.0 · content CC BY 4.0, code MIT

## Read the full playbook · 完整版在官网

This repository is the condensed version for agents. The full text for people lives only on the website:

- **Full playbook (Chinese)**: https://canlah.ai/zh/playbook/ — 9 chapters and 4 appendices, a blueprint for each of the 46 page types, the evidence behind each rule, plus a dental and aesthetics edition. 完整版（中文）
- **Quick guide (English)**: https://canlah.ai/playbook/ — the whole method on 12 pages. 英文轻量版
- The quick guide is also downloadable from those pages as PDF and PPTX. Its text is not mirrored here: the website is the only home of the playbook text.

Every reference file in this repo links to the matching chapter section on canlah.ai.

## Install · 安装

### Claude Code

As a plugin, from inside Claude Code:

```
/plugin marketplace add Canlah-AI/geo-playbook
/plugin install geo-playbook@canlah-ai
```

Or as a personal skill:

```bash
git clone https://github.com/Canlah-AI/geo-playbook ~/.claude/skills/geo-playbook
```

(Copying only `SKILL.md` and `references/` into `~/.claude/skills/geo-playbook/` also works.) The skill loads when you ask things like "audit my site for ChatGPT visibility", "why does AI get our prices wrong", "write a price guide page AI will quote" or "we're a dental clinic, what can we publish?".

### Other agents (Codex, Cursor, OpenClaw and others)

Point the agent at [`AGENTS.md`](AGENTS.md): copy `AGENTS.md` and `references/` into your project root, or add this repository as a submodule. `AGENTS.md` has the same operating instructions as `SKILL.md` without any Claude-specific parts. If you use the skills CLI: `npx skills add Canlah-AI/geo-playbook`.

## The method in five steps · 五步

1. **Measure first.** Write 30 questions real buyers ask (from their own words, ad keywords, real search queries; never AI-generated), ask them, save the answers, and measure how much results swing on their own. Freeze the questions for the quarter.
2. **Open the door.** Let AI crawlers read the page text: snippet switches (`nosnippet`), robots.txt retrieval crawlers, the WAF, and prices in the initial HTML (major AI crawlers do not run JavaScript).
3. **Be recognised.** The same name, address, phone, registration numbers and prices everywhere: a plain HTML facts page, person pages, five business profiles.
4. **Price page + off-site.** The first page is an all-products price guide (English and Chinese). Then get correct facts onto the pages AI already cites: official registers, associations, manufacturer locators, bylined factual articles, correction letters.
5. **Check monthly.** Same questions, same engines, three numbers kept apart: times named, cited pages that mention you (X/20), facts AI gets wrong.

Steps 2 and 3 are pass or fail: if they fail, everything else is multiplied by zero. The agent edition runs these as eight steps: decide the regulatory side → door check → identity → freeze question pool and baseline → pick targets → write pages by type → off-site → monthly retest. See [`SKILL.md`](SKILL.md).

## How this differs from other GEO material · 和别的 GEO 资料的区别

Full account, with the book section behind each point: [`CREDITS.md`](CREDITS.md).

- **Every rule states its evidence and sample size.** Rules are labelled "measured n/N", "measured, 1 case" or "not measured". Where measurement disagreed with common practice, we followed the measurement: quoted sentences were almost always the first sentence of a paragraph (legal 15/18); about 73% of locatable quoted facts sat in the first 30% of the page (55/75); few cited pages were 1,800–3,000 words long, so there is no global word minimum.
- **ChatGPT and Google AI Mode are measured, and written for, separately.** They cite different kinds of pages. In dental and aesthetics, ChatGPT mostly cited government and public institutions (72%) while AI Mode mostly cited other clinics' price pages (88%); in e-commerce the two engines' cited URLs did not overlap at all. So every page carries an "own sentence" for ChatGPT and a "market sentence" for AI Mode, and retests record the engines separately.
- **46 page types, counted one by one.** 9 types measured on both engines, 33 on ChatGPT only, 4 seen only in an external teardown and marked unmeasured. Each type has a block order, the block AI most often copies, which engine mainly cites it, and what each regulatory side may do with it.
- **Regulated industries: three sides, six switches, three compliance labels.** Four questions place a business on the strictly regulated, lightly regulated or unregulated side; six switches add hard gates (for example agency liability, legally required fields, a ban on peer comparison). Every compliance sentence carries one label: "explicit in the rule text", "conservative line, not explicit in the rule text" or "source text not obtained". A client's sign-off can relax only the first two kinds of stop, never an explicit ban. Every ban comes with what to write in its place.
- **Chinese pages and local anchoring.** Chinese pages are written from Chinese buyer questions, not translated, and must name the country in the H1, give an S$ amount with its tax basis in the first paragraph, and name a real MRT station or area.

## Evidence base · 实测口径

Both rounds were completed on 2026-09-23 on Singapore businesses in five industries: dental and aesthetics, family law, tuition and education, B2B SaaS, e-commerce and consumer goods.

- **Round 1, two engines**: 60 questions (6 in Chinese), ChatGPT and Google AI Mode, **526 citations** across about 300 domains, **92 cited pages taken apart** one by one.
- **Round 2, ChatGPT only**: 10 questions per industry (OpenAI API, gpt-5.5 + web search, Singapore location), **about 290 citations**, 228 of them on page types not seen in round 1.

Limits: tier B page types have ChatGPT evidence only; quote positions were estimated by eye; there is no long-term outcome data yet; samples are small and Singapore-only; probes run through APIs, which differ systematically from the web interfaces; the raw data is not public yet. Details: [`CREDITS.md`](CREDITS.md), section "What we have not done".

## What's in this repository · 仓库内容

```
SKILL.md                     Claude Code skill: the operating guide for agents
AGENTS.md                    the same guide for any agent that reads AGENTS.md
references/
  sides-and-compliance.md    three sides, six switches, three labels, sign-off rules
  page-types.md              46 page types: intent, engine, block order, what AI copies
  audit-checklist.md         five door gates, identity checks, per-page gates
  measurement.md             three numbers, noise band, baseline, monthly routine
  myths.md                   five things sold as GEO, and what to do instead
tools/                       build scripts for the book and site (MIT)
.claude-plugin/              plugin and marketplace manifests
CREDITS.md                   what we borrowed, how we differ, what we have not done
LICENSE                      CC BY 4.0 (content)
LICENSE-CODE                 MIT (code in tools/)
```

## Credits · 致谢

This playbook was not written from scratch. We borrowed template structures, sentence patterns and rule names from Aaron He's open-source [aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills) (Apache-2.0), rewritten rather than copied; five page types come from a teardown of a GEO agency's public blog (not named; four are the unmeasured tier C types, the fifth was merged into a measured type); and the rules rest on public studies, official crawler documentation and regulations listed row by row. None of the people or organisations credited took part in or reviewed this work. Full list and attributions: [`CREDITS.md`](CREDITS.md). Wrong attribution? Please open an issue.

## License · 许可

- Content (all Markdown in this repository and the playbook on canlah.ai): [CC BY 4.0](LICENSE). Attribute as: *GEO Playbook by Canlah AI, https://canlah.ai/zh/playbook/*.
- Code in `tools/`: [MIT](LICENSE-CODE), © 2026 Canlah AI.

## Related · 互链

- **canlah.ai**: full playbook https://canlah.ai/zh/playbook/ · English quick guide https://canlah.ai/playbook/
- **[Canlah-AI/seven-engines-geo-forensics](https://github.com/Canlah-AI/seven-engines-geo-forensics)**: our source-forensics case study that put one commercial question to seven search and AI-answer engines in one night, with raw data, frozen classification code and verified mechanism claims (CC BY 4.0, DOI 10.5281/zenodo.22225223). It asks whether engines cite the same sources; this playbook asks what a cited page looks like and how to write one.
- **[aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills)**: Aaron He's open-source marketing skills (seven disciplines, 120 skills), a source of several templates we adapted; see [`CREDITS.md`](CREDITS.md).

Questions or help with a first round: admin@canlah.ai
