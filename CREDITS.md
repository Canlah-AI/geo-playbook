# 致谢与区别说明 · Credits and How This Playbook Differs

[中文](#中文) · [English](#english)

最后更新 / Last updated: 2026-09-24

---

## 中文

《GEO Playbook》（下称「本书」）不是从零写出来的。这一页讲三件事：

1. 我们借了谁的什么；
2. 我们做法不同的地方，每一条在书里的依据；
3. 我们还没做到的。

下面列出的个人和机构都没有参与或审阅本书。列出名字只是为了标明出处，不代表他们认可本书的结论。署名或引用有错，请开 issue 告诉我们。

括号里的数字是书中小节号，例如（5.9）指第 5.9 节，（A.3）指附录 A.3。

### 一、我们借鉴了谁的什么

#### 1. Aaron He 的开源技能仓 aaron-marketing-skills

- 仓库：https://github.com/aaron-he-zhu/aaron-marketing-skills ，Apache-2.0 授权。
- 我们对照的版本是 main 分支 `a8fcbd5`（v20.1.0，2026-09-22 推送），逐个文件读过。之后的版本可能有变化。
- 本书没有收录该仓的原文件。我们借的是模板结构、句型和规则名，翻译或改写后写进了书里；这一页就是这些借用的统一出处说明。

**书里直接用上的：**

| 我们借的 | 来自哪个文件 | 在书里用在哪 |
|---|---|---|
| 批量页模板：Intro → Evidence block → Decision → FAQ → CTA，空字段自动隐藏 | `seo-geo/implement/page-play-builder/references/programmatic.md` | 单项目价格页（5.11） |
| 易变的价格旁边标 as of <日期>，并定期刷新（原文是 prices 30 days） | 同一文件的 Provenance & freshness 一行 | 页型共用件（5.10）、对比页（5.15） |
| 对比页的四种格式：[Competitor] Alternative、Alternatives、You vs [Competitor]、[A] vs [B]，并保留 who should switch / who should not 一节 | `seo-geo/implement/page-play-builder/references/comparison.md` | 对比页（5.15）。我们按监管侧别重新规定了每种格式谁能用 |
| 问答句型：先用 40–60 词直接作答，再列 3–4 个影响因素或前提 | `seo-geo/implement/geo-content-optimizer/references/quotable-content-examples.md` 的 Q&A 一行 | 「市场句」的句型（5.6） |
| Quick Quotability Test（10 条） | 同上 | 交稿自检清单（5.31），前几问由它和各页型的自检合并而成 |
| 「there is no universal word-count threshold for citation」（被引没有通用的字数门槛） | `seo-geo/implement/geo-content-optimizer/references/ai-citation-patterns.md` | 这句话帮我们推翻了自己旧稿里「每页 1,800–3,000 词」的规定。现在的规则是字数按页型定，不设统一下限（5.7） |

**对照过、结论一致的：** 答案前置（CORE-EEAT 的 C02）；对比和规格用表格（O03）；对比页先给 TL;DR 和速览表，再写各自适合谁；榜单先放速览表，每一项注明适合谁；FAQ 段；数据旁写明口径。我们在五个行业的被引页上数到的频次，和这些写法是一致的（A.3）。在我们的样本范围内，这算是对这几条的一次独立检验。

我们对照时逐条看过它的爬虫与收录控制表，每一条都附了官方文档链接。这张表可以和本书开门一章的爬虫用途表（2.4）互相参照。

#### 2. 一家 GEO 服务商的公开博客（不点名）

46 种页型里有 5 种来自我们对一家 GEO 服务商公开博客的拆解，包括：

- C 档四型：pt43 买家选型框架页、pt44 概念支柱页、pt45 新闻与政策解读页、pt46 市场观察页；
- 「一手数据报告页」的自建规格，已并入 pt19 统计源头页。

第 5 章「规模化生产」里拆架构的方法（5.D2–5.D4）也是从这次拆解整理出来的。

我们的公开材料不点名其他 GEO 服务商，所以这里不写这家的名字。这几型在书里整张标着「未实测，规格取自外部拆解」（5.30、B.5），我们没有给它们做过被引实测。

#### 3. 公开研究、官方文档与法规

书里凡是用了外部数字的地方，附录 A 都写了样本、时间，以及能不能对外说。下面的表按附录 A 逐条整理。「链接」一列只照抄附录里已有的链接；附录没给的，只写名字，我们没有补。

**数据研究**

| 机构 | 研究或页面 | 我们用它支撑哪条规则 | 链接 |
|---|---|---|---|
| searchVIU | 实测 ChatGPT、Claude、Perplexity、Gemini、AI Mode 五个系统的实时抓取：都不读 JSON-LD，隐藏的 Microdata、RDFa 也被忽略 | 事实必须用可见 HTML 写出来，一行一个字段（0.1、2.7）。这条推不出「schema 没用」 | 附录未给 |
| Ahrefs | 1,885 个新加 JSON-LD 的页面，对照 4,000 个页面（2025-08 至 2026-03） | JSON-LD 在建站时一次配好，不进每页的检查清单（2.7） | 附录未给 |
| Ahrefs | ChatGPT 引用里 best-of 类博文占 43.8%（750 个查询 / 26,283 个 URL） | 只用来判断一个品类要不要做榜单，不和页型密度并列比较（6.1） | 附录未给 |
| Ahrefs | 2026 年：YouTube 提及和 AI 概览可见度的相关系数是 0.737，外链是 0.218 | 每个厚页配一条本人口述的长视频（6.7）。这是相关，不是因果 | 附录未给 |
| Ahrefs、Profound | Wikipedia 在 ChatGPT 引用中的份额（Ahrefs 2026-07 追踪为 8.9%；Profound 的 6.8 亿条引用中占 7.8%） | 用 Wikidata 和 Wikipedia 做实体锚点（3.4） | 附录未给 |
| Whitespark | 540 个查询、3 个美国城市、6 个行业：价格类信息题的 AI 概览覆盖率 92%，价格加交易的混合题 97% | 第一页写价格指南页（0.1、5.12） | 附录未给 |
| Steady Demand | 1,487 个查询、50 个都市区、14,472 条引用：AI Mode 本地题的引用 79.8% 指回 Google 商家档案 | 商家档案是入场券，不是杠杆（3.4） | 附录未给 |
| Vercel × MERJ | 5 亿次以上的抓取样本：主流 AI 检索爬虫不执行 JS（2024-12） | 价格、成绩、规格必须出现在首屏 HTML 里（5.7、2.9） | 附录未给 |
| SE Ranking | XGBoost 引用预测模型：去掉 llms.txt 之后，预测精度反而提高 | 不把 llms.txt 当杠杆（1.4） | 附录未给 |
| BuzzStream | 屏蔽 GPTBot 的网站有 88.2% 照样被引 | GPTBot 是训练爬虫；robots.txt 里检索段和训练段分开写（2.4、B.1） | 附录未给 |
| Peec | 从 ChatGPT 自身 SSE 的 `result_source` 字段抓到至少八路检索源（2026-05-21 至 07-21） | 本地答案会走 Foursquare、Yelp 等来源，所以五处商家档案要补齐；IndexNow 不是 ChatGPT 这一路的开关（3.4） | 附录未给 |
| Peec | 5.7M 个数据点、近 20 万条回答、8 个引擎：进入 AI 已经在引的榜单并排到第 1 位，可见度 +16.5pp | 只用来排站外的施工顺序，不作效果承诺。+16.5pp 是 B2B SaaS 样本 | 附录未给 |
| Pew | 2025 年，900 名美国用户：约 1% 的访问会点 AI 摘要里的链接 | 买家拿到名字后会回头去搜，所以先要让机器认对是哪一家（1.1、第 3 章） | 附录未给 |
| Muck Rack | 2,500 万条链接、17 个行业：AI 引用 84% 来自 earned media，其中新闻 27%；付费和软文只占 0.3% | 站外的力气花在具名供稿和更新函上，不做付费收录（0.1、6.1） | 附录未给 |
| Omniscient | 搜品牌词时，自有内容只占 23% | 主战场不在自己的官网（1.1） | 附录未给 |
| deltaV | 25,337 条引用的页型分布：comparison 每次检索 1.87 条引用；医疗细分里 articles 占 54%、listicle 占 0% | 页型分布随行业变；在已经决定做的品类里给单页排序（5.1、6.1） | 附录未给 |
| 5WPR | 320+ 个 prompt、10 个都市区、5 个引擎：实体强度带来约 8 倍的差距；78% 的独立本地商家 AI 引用份额约为零 | 纯目录收录的引用密度低，先做个人和机构实体（第 3 章） | 附录未给 |
| 5W Citation Share | YouTube 占 Google AI 答案引用的 23% | 长视频（6.7） | 附录未给 |
| Otterly | 170 万个数据点：播放量、点赞、订阅数与被引的相关系数约 −0.03；94% 的 YouTube AI 引用给了长视频；带时间戳的视频 78% 被重复引用 | 长视频规格：按 H2 打时间戳，描述里放逐字稿（6.7） | 附录未给 |
| Otterly、Axios | 2026-08 ChatGPT 来源重排的追踪：Reddit 份额下跌 73% 以上；机构和政府类来源从约 1/6 涨到接近 1/3 | Reddit 按月读数，占比超过 2% 才排工单（7.3）；机构来源优先（6.4） | 附录未给 |
| PRWeb | 1,120 个查询、7 个行业、13 个城市：裸词 divorce lawyer 在 AI Mode 里 10 个城市都返回零个商家，加上 near me 后 38/38 恢复；专业服务靠教育型内容胜出，消费型服务靠评论量胜出 | 题池配比写死（4.2）；内容形态分专业型和消费型（5.9） | 附录未给 |
| Trakkr | 1,465 个被引页：平均 2,290 词，78% 超过 1,000 词 | 只作长度参考。书里的规则是字数按页型定（5.7） | 附录未给 |
| 汉堡大学 + Leibniz Institute | 2025-11，五周、24,000+ 条答案：接口和网页版的引用分布有系统性偏斜 | 每月加跑一条网页对照腿（4.4） | 附录未给 |

**官方文档与平台条款**

| 机构 | 文档 | 我们用它支撑哪条规则 | 链接 |
|---|---|---|---|
| Google | 爬虫文档；《AI features and your website》 | AI 概览的闸门是 Googlebot 加 nosnippet，不是 Google-Extended（2.2、2.6）；Merchant Center 和 Business Profile 列在最佳实践里，而且不需要额外的 schema（2.7） | 附录未给 |
| Google | 2026-05-15 的 AI 优化指南 | 不需要 llms.txt（1.4） | 附录未给 |
| Apple | 《About Applebot》 | Applebot-Extended 只是退出训练的开关，不影响 Applebot 检索（2.4） | 附录未给 |
| Anthropic | 官方爬虫文档 | ClaudeBot、Claude-SearchBot、Claude-User 都遵守 robots.txt（2.4） | 附录未给 |
| OpenAI | 商户 feed 规格 | 商品详情页的价格和 feed 保持一致（5.20） | `developers.openai.com/commerce/` |
| OpenAI | 商户门户 | 同上 | `chatgpt.com/merchants` |
| Gartner Peer Insights | 激励政策 FAQ；评价来源 FAQ | 平台条款对评价征集的约束（6.5、8.7） | `gpivendorresources.gartner.com/en/articles/6812506-incentives-faqs`；`gpivendorresources.gartner.com/en/articles/6812574-review-sourcing-faqs` |

**法规与监管指引（通用部分）**

| 机构 | 文件 | 我们用它支撑哪条规则 | 链接 |
|---|---|---|---|
| CCCS（新加坡竞争与消费者委员会） | 价格透明指引 | 价格写法的底线，不受管的行业也适用（8.2、8.8） | `cccs.gov.sg/consumer-protection/legislation-and-guidelines/guidelines-on-price-transparency` |
| 新加坡法规 | CPFTA，《消费者保护（公平交易）法》 | 同上 | `sso.agc.gov.sg/Act/CPFTA2003` |
| PDPC | Do Not Call 登记与你的企业 | 外联发信前查免打扰名册（8.2） | `pdpc.gov.sg/overview-of-pdpa/do-not-call-registry/business-owner/do-not-call-registry-and-your-business` |
| China Law Translate | 中国《广告法》（2021）英译 | 面向中国消费者的中文页，要避开绝对化用语（8.9） | `chinalawtranslate.com/advertising-law-2021/` |
| 国家市场监督管理总局 | 《广告绝对化用语执法指南》 | 同上。书里标「未取到原文，不作放宽依据」 | 附录未给 |

各行业主管机构的广告条例，以及条文原文、编号和链接，收在各行业版的附录里，这里不重复。

#### 4. 我们自己的实测（本书的主要依据）

两轮都在 2026-09-23 完成，范围是新加坡的五个行业：牙科·医美、家事法、补习·教育、B2B SaaS、电商·消费品。

- **两腿实测**：60 个问句，其中牙科、法律、补习各有 2 句中文。ChatGPT 和 Google AI Mode 两个引擎都测，共 526 条引用、约 300 个域名，逐页拆了 92 页。
- **单腿补测**：5 个行业各 10 句，只测 ChatGPT（OpenAI 接口 gpt-5.5 + web_search，定位新加坡）。241 条引用。按页型逐页点数（合并了正式与一次补跑，不等于条数）：新页型 228 次、已知九型 63 次。

每一条数据的口径见附录 A.3 和 A.4。

#### 5. 相关的 Canlah 公开仓

- **seven-engines-geo-forensics**：https://github.com/Canlah-AI/seven-engines-geo-forensics （README 标注 CC BY 4.0，DOI 10.5281/zenodo.22225223）。2026-08-29 这一晚，我们用中英两种语言，把同一个商业问句拿去问七个搜索引擎和 AI 答案引擎，把被引的页面都抓下来，用冻结的分类代码给页面分型，再逐条核对各引擎公开的检索机制说明。
- **两个仓怎么互相链接**：它回答的是「不同引擎引的是不是同一批来源」（一个问句、七个引擎、一个晚上），本书接着回答「被引的那一页长什么样、应该怎么写」（两轮共 110 个问句、两个引擎、五个行业）。本仓在这里链到它，那边有原始数据和分类代码可以复跑；它的 README 也会加一行链回本仓。

### 二、我们不一样在哪

aaron-marketing-skills 覆盖七个营销领域、120 个技能，本书只讲一件事：在新加坡怎样让 AI 答案引用你的页面。下面这六点是范围和方法上的不同，每条后面附书里的依据。

**1. 每条规则都写明了实测依据和样本量。**

- 规则按三种标注写：「实测 n/N」「实测 1 例」「未实测」（A.3）。
- 页型按证据分三档：A 档两个引擎都测过（9 型），B 档只测了 ChatGPT（33 型），C 档只在外部拆解里见过、我们没实测（4 型）（5.1）。
- 实测和通行写法冲突时，按实测改。例如：
  - 被抄走的句子几乎都是某一段的第一句（法律 15/18）；
  - 能定位的被抄事实里，约 73% 落在正文前 30%（55/75）；
  - 字数在 1,800–3,000 词之间的被引页很少（法律 2/18、补习 2/8），所以字数不设统一下限（A.3）。
- 和 aaron-marketing-skills 的关系：在我们的被引样本里，外链、署名和问句式 H2 的实际频次，和 CORE-EEAT 的阈值对不上：
  - 有权威外链的页，牙科 1/16，法律 2/18；
  - 具名个人作者，法律 2/18；
  - 有 3 个以上问句式 H2 的页，法律 3/18，SaaS 4/13。

  所以书里不把外链和署名当作被引条件（医疗页的署名是例外，6/12），H2 用陈述句，问句放进 FAQ（A.3）。这不说明那几条作为写作质量规范没有价值：CORE-EEAT 自己写明「advisory until outcome-calibrated」（结果未经校准前仅供参考），它衡量的是内容质量，不是会不会被引。

**2. ChatGPT 和 Google AI Mode 分开测、分开写。**

两个引擎引的不是同一类页（A.3）：

| 行业 | ChatGPT 主要引 | AI Mode 主要引 |
|---|---|---|
| 牙科·医美 | 政府和公立机构，76%（38/50） | 诊所等商业站，75%（39/52） |
| 家事法 | .gov.sg，77%（46/60） | 律所等商业站，69%（36/52） |
| 电商·消费品 | 商品详情页，54% | Google Shopping 商品卡，44%。两边引用的 URL 重叠为 0 |

所以：

- 每页写两种句子：给 ChatGPT 的「本方句」（自家的确定价或规格），给 AI Mode 的「市场句」（区间、影响因素、出处）（5.6）；
- 46 型索引里，每一型都标了主要被哪个引擎引（5.1）；
- 复测时两个引擎分开记（第 7 章）。

**3. 46 种页型是一个个数出来的。**

- 算法：两轮实测得到 9 + 33 型，加上外部拆解的 5 型，再合并 1 个重复，共 46 型。
- 46 型分六个家族：价格、选择与口碑、问题与规则、实体与事实、源头、解读观点。
- 两个页算同一型，要三条全满足：触发的问法同族；被抄句在页面上的位置和形态同族；能用同一张施工图写出来（5.1、A.3）。
- 页型的数量取决于测了多少种问法。以后测更多问法，这个数还会增加。

**4. 受监管行业：三侧、六个开关、三档合规标签。**

- **先判侧别**：用四个问题判出强监管、弱监管、不受管三侧，再勾六个叠加开关，例如代发连带、法定必填字段、禁同行比较（0.2）。
- **每型标开放值**：46 型每一型都标了在三侧各自是建、改、引还是停（5.1）。
- **每条合规句挂一个标签**：「条文明文」「保守线，非条文明文」「未取到原文」。签字的规则是：
  - 遇到三类情况停笔，交客户的合规负责人签字；
  - 签字只能放宽「只有客户知道的事实」和「保守线」这两类；
  - 「条文明文」的禁令，以及标「未取到原文」的条目，签了字也不放行（0.4）。
- **行业版有条文原文**：每条规则带条文号、原文句子和链接（0.4）。
- **禁令都给替代写法**：每条禁令配一条「这一格改写成什么」，不是删掉就算完（0.4）。

**5. 中文，以及新加坡本地。**

- 所有问句都按新加坡定位测，热词取自 Google 自动补全（gl=sg）。实测里 ChatGPT 引用的多是新加坡的政府和公立机构页，例如 MOH、CPF、judiciary、ask.gov.sg（A.3）。
- 中文页不是翻译稿。每个买家类型默认出英文、中文各一页，两页同一档做完（5.9）。
- 中文页有三处写死，缺一处不能上线（5.9）：
  - H1 里有「新加坡」；
  - 首段出现 S$ 金额，并写明含不含 GST；
  - 正文里至少有一处真实的地铁站名或地区名。
- 这样定的原因：实搜时，中文问句的答案抄了别国网站的外币报价（5.9）。

**6. 按行业分版。**

- 通用版只写跨行业都成立的规则。
- 行业版（目前出了牙科·医美版）另外收录这个行业的条文原文、编号和链接，以及行业表头和第一周该做的三件事（0.4、A.1）。
- 附录 C 列出五个已测行业在十个轴上的取值。第 8 章给没写过的行业一套自己判断的四步：十问、判侧、十轴、决策表。
- 同一条规则在不同行业里可能正好相反。例如榜单页，不受管侧可以自己做（自家排第一要披露），强监管侧不做（5.1）。

### 三、我们没做到的

1. **有些数据只测了一个引擎。** B 档 33 型只有 ChatGPT 的证据：AI Mode 的探测配额用完了，没有跑（配额 2026-09-29 重置）。因此这一轮在结构上测不出偏二手整理的页型（A.4）。C 档 4 型我们完全没实测（A.4）。另有一些「探路数」是单引擎、没锁新加坡地区、只取了一次样，书里规定重测之前不对外说（A.1、A.2）。
2. **被抄句的位置是目测的。** 526 条引用里，只有 75 条能在原页上找到被抄的那一句；位置是按页面篇幅目测估出来的，不是按字符逐个编码（A.3）。答案只存了前 600 字，后半段引的是哪一句，没法逐句对上（A.3）。
3. **没有长期效果数据。** 两轮实测都是 2026-09 的一次性快照。按本书方法做出来的页，上线后的排名和 AI 引用还没有复测数据（5.D1）。实体修正多久见效、站外多久见效这些周期，都是推断，书里标了「未实测」（A.1、A.2）。
4. **样本小，范围窄。** 只测了新加坡的五个行业；热词只取自 Google 自动补全，没有用 People Also Ask 和 Reddit 原帖（A.3）；不少页型只有 1 个样本，只能当方向看（A.4）；「推荐型问法会抄评价」这个比例只有 15 个样本（A.2）。
5. **量具有偏差。** 我们的探针走的是接口：ChatGPT 用 OpenAI 接口，AI Mode 用第三方 SERP 接口。用户在网页版看到的可能不一样，公开研究显示接口和网页版的引用分布有系统性偏斜（A.2）。
6. **引用的外部研究多是美国或跨行业样本。** 大多没有在新加坡验证过，很多研究原文没有给链接（A.1、A.5）。
7. **合规规则不是法律意见。** 通用版里的标签只代表举例行业的依据档次，不是你所在行业的法条；书里还有标着「未取到原文」的条目（0.4）。
8. **原始数据还没有公开。** 两轮实测的原始答案和逐页拆解，还没有整理成可以公开的数据集，书里给的是汇总数和样本链接。
9. **书本身也有没理顺的地方。** 例如交稿自检清单的出处标注和实际条数对不上。我们在附录 A.3 照实列了出来，没有改成对得上的说法。

---

## English

The GEO Playbook ("this book") was not written from scratch. This page covers three things:

1. whose work we borrowed and what exactly we took;
2. where our approach differs, with the section of the book that backs each point;
3. what we have not done yet.

None of the people or organizations listed here took part in or reviewed this book. We name them only to credit sources, not to suggest they endorse our conclusions. If you find a wrong attribution or citation, please open an issue.

Numbers in parentheses are book sections: (5.9) means section 5.9, and (A.3) means Appendix A.3.

### 1. What we borrowed, and from whom

#### 1.1 Aaron He's open-source skills repo, aaron-marketing-skills

- Repo: https://github.com/aaron-he-zhu/aaron-marketing-skills (Apache-2.0).
- We read `main` at `a8fcbd5` (v20.1.0, pushed 2026-09-22) file by file. Later versions may differ.
- This book does not include any of the repo's files. We borrowed template structures, sentence patterns and rule names, and translated or rewrote them for the book. This page is the single attribution for those borrowings.

**What we used directly:**

| What we borrowed | Source file | Where it appears in the book |
|---|---|---|
| Batch-page template: Intro → Evidence block → Decision → FAQ → CTA, with empty fields hidden | `seo-geo/implement/page-play-builder/references/programmatic.md` | Single-service price page (5.11) |
| An "as of <date>" label next to volatile prices, refreshed on a schedule (original: prices 30 days) | Same file, "Provenance & freshness" row | Shared page components (5.10); comparison page (5.15) |
| Four comparison formats: [Competitor] Alternative, Alternatives, You vs [Competitor], [A] vs [B], keeping the "who should switch / who should not" section | `seo-geo/implement/page-play-builder/references/comparison.md` | Comparison page (5.15). We re-assigned which format each regulatory side may use |
| Q&A pattern: a direct 40–60-word answer first, then 3–4 factors or caveats | Q&A row of `seo-geo/implement/geo-content-optimizer/references/quotable-content-examples.md` | Pattern for the "market sentence" (5.6) |
| Quick Quotability Test (10 items) | Same file | Pre-publish self-check (5.31); its first questions merge this test with our per-page-type checks |
| "there is no universal word-count threshold for citation" | `seo-geo/implement/geo-content-optimizer/references/ai-citation-patterns.md` | This line helped us drop our own earlier 1,800–3,000-word rule. The current rule sets length by page type, with no global minimum (5.7) |

**Checked, and consistent with our data:** answer first (CORE-EEAT C02); tables for comparisons and specs (O03); a TL;DR and an at-a-glance table on comparison pages, followed by who each option suits; a summary table on list pages, with a "best for" line on each item; an FAQ section; stating how a number was measured. The frequencies we counted on cited pages across five industries agree with these patterns (A.3). Within our sample, that is an independent check of those rules.

We read its crawler and indexing-control table row by row during the comparison; every row links to official documentation. It is a useful companion to the crawler-purpose table in this book's chapter on opening the door to crawlers (2.4).

#### 1.2 A GEO agency's public blog (not named)

5 of the 46 page types come from our teardown of a GEO agency's public blog:

- the four tier-C types: pt43 buyer's selection framework, pt44 concept pillar, pt45 news and policy explainer, pt46 market observation;
- the build spec for a first-party data report, now merged into pt19, the statistics-source page.

The architecture-teardown method in the scaled-production part of Chapter 5 (5.D2–5.D4) also came out of this teardown.

Our public materials do not name other GEO agencies, so we leave this one unnamed. In the book, each of these types is marked "not measured; spec taken from an external teardown" (5.30, B.5). We have not run citation tests on them.

#### 1.3 Public research, official documentation and regulation

Wherever the book uses an outside number, Appendix A gives its sample, date and whether it may be quoted externally. The tables below follow Appendix A row by row. The "Link" column copies only links that already appear in the appendix. Where the appendix gives none, we list the name only and did not add one.

**Studies**

| Organization | Study or page | Rule it supports in the book | Link |
|---|---|---|---|
| searchVIU | Live-fetch tests across ChatGPT, Claude, Perplexity, Gemini and AI Mode: none read JSON-LD, and hidden Microdata and RDFa were ignored too | Facts must be written in visible HTML, one field per line (0.1, 2.7). This does not show that schema is useless | Not given in the appendix |
| Ahrefs | 1,885 pages that added JSON-LD, against 4,000 control pages (2025-08 to 2026-03) | Set up JSON-LD once when the site is built; it is not on the per-page checklist (2.7) | Not given in the appendix |
| Ahrefs | Best-of posts account for 43.8% of ChatGPT citations (750 queries / 26,283 URLs) | Used only to decide whether a category needs list pages at all; never compared side by side with page-type density (6.1) | Not given in the appendix |
| Ahrefs | 2026: YouTube mentions correlate 0.737 with AI Overview visibility; backlinks, 0.218 | Pair each substantial page with a long video the practitioner narrates in person (6.7). This is correlation, not causation | Not given in the appendix |
| Ahrefs, Profound | Wikipedia's share of ChatGPT citations (8.9% in Ahrefs' 2026-07 tracking; 7.8% of Profound's 680M citations) | Wikidata and Wikipedia as entity anchors (3.4) | Not given in the appendix |
| Whitespark | 540 queries, 3 US cities, 6 industries: AI Overviews appear on 92% of informational price queries and 97% of price-plus-transaction queries | Write the price guide before any other page (0.1, 5.12) | Not given in the appendix |
| Steady Demand | 1,487 queries, 50 metro areas, 14,472 citations: 79.8% of AI Mode local citations point back to Google Business Profiles | A business profile gets you in the door; it is not a lever (3.4) | Not given in the appendix |
| Vercel × MERJ | 500M+ crawl samples: the main AI retrieval crawlers do not execute JavaScript (2024-12) | Prices, results and specs must be in the initial HTML (5.7, 2.9) | Not given in the appendix |
| SE Ranking | XGBoost citation model: removing llms.txt made its predictions more accurate | Do not treat llms.txt as a lever (1.4) | Not given in the appendix |
| BuzzStream | 88.2% of sites that block GPTBot are still cited | GPTBot is a training crawler; write retrieval and training sections of robots.txt separately (2.4, B.1) | Not given in the appendix |
| Peec | At least eight retrieval sources captured from the `result_source` field in ChatGPT's own SSE stream (2026-05-21 to 07-21) | Local answers draw on Foursquare, Yelp and others, so complete all five business listings; IndexNow is not a switch for ChatGPT (3.4) | Not given in the appendix |
| Peec | 5.7M data points, about 200K answers, 8 engines: getting into a list AI already cites, in first place, adds 16.5pp of visibility | Used only to order off-site work, never as a promise of results. The +16.5pp figure is from a B2B SaaS sample | Not given in the appendix |
| Pew | 2025, 900 US users: about 1% of visits click a link in an AI summary | Buyers take the name and search again, so machines must first identify you correctly (1.1, Chapter 3) | Not given in the appendix |
| Muck Rack | 25M links, 17 industries: 84% of AI citations come from earned media, 27% from news alone; paid and advertorial, 0.3% | Off-site effort goes to bylined contributions and update requests, not paid placements (0.1, 6.1) | Not given in the appendix |
| Omniscient | Owned content is 23% of results even on brand queries | Most of the contest happens off your own site (1.1) | Not given in the appendix |
| deltaV | Page-type distribution across 25,337 citations: comparison pages get 1.87 citations per search; in healthcare, articles 54% and listicles 0% | Page-type mix varies by industry; used to rank pages within a category you have already chosen (5.1, 6.1) | Not given in the appendix |
| 5WPR | 320+ prompts, 10 metros, 5 engines: entity strength is associated with a roughly 8x difference; 78% of independent local businesses have near-zero AI citation share | Directory listings alone have the lowest citation density; build the person and organization entity first (Chapter 3) | Not given in the appendix |
| 5W Citation Share | YouTube is 23% of citations in Google's AI answers | Long-form video (6.7) | Not given in the appendix |
| Otterly | 1.7M data points: views, likes and subscribers correlate about −0.03 with citation; 94% of YouTube AI citations go to long videos; 78% of timestamped videos are cited repeatedly | Video spec: timestamps per H2, full transcript in the description (6.7) | Not given in the appendix |
| Otterly, Axios | Tracking of ChatGPT's 2026-08 source reshuffle: Reddit's share fell 73% or more; institutional and government sources rose from about 1/6 to nearly 1/3 | Read Reddit share monthly and act only above 2% (7.3); institutional sources first (6.4) | Not given in the appendix |
| PRWeb | 1,120 queries, 7 industries, 13 cities: the bare query "divorce lawyer" returned zero businesses in AI Mode across 10 cities, and adding "near me" restored 38/38; professional services won on educational content, consumer services on review volume | Fixed ratios for the question pool (4.2); professional and consumer content handled differently (5.9) | Not given in the appendix |
| Trakkr | 1,465 cited pages: 2,290 words on average; 78% over 1,000 words | Length reference only. The book sets length by page type (5.7) | Not given in the appendix |
| University of Hamburg + Leibniz Institute | 2025-11, five weeks, 24,000+ answers: citation distributions differ systematically between API and web interfaces | Add a web-interface control run every month (4.4) | Not given in the appendix |

**Official documentation and platform terms**

| Organization | Document | Rule it supports in the book | Link |
|---|---|---|---|
| Google | Crawler documentation; "AI features and your website" | The gate for AI Overviews is Googlebot plus nosnippet, not Google-Extended (2.2, 2.6); Merchant Center and Business Profile are on the best-practice list, and no extra schema is needed (2.7) | Not given in the appendix |
| Google | AI optimization guide, 2026-05-15 | llms.txt is not needed (1.4) | Not given in the appendix |
| Apple | "About Applebot" | Applebot-Extended only opts you out of training; it does not affect Applebot retrieval (2.4) | Not given in the appendix |
| Anthropic | Official crawler documentation | ClaudeBot, Claude-SearchBot and Claude-User all follow robots.txt (2.4) | Not given in the appendix |
| OpenAI | Merchant feed specification | Product-page prices must match the feed (5.20) | `developers.openai.com/commerce/` |
| OpenAI | Merchant portal | Same as above | `chatgpt.com/merchants` |
| Gartner Peer Insights | Incentives FAQ; review-sourcing FAQ | Platform terms that limit how reviews may be requested (6.5, 8.7) | `gpivendorresources.gartner.com/en/articles/6812506-incentives-faqs`; `gpivendorresources.gartner.com/en/articles/6812574-review-sourcing-faqs` |

**Regulation and regulatory guidance (cross-industry)**

| Organization | Document | Rule it supports in the book | Link |
|---|---|---|---|
| CCCS (Competition and Consumer Commission of Singapore) | Guidelines on price transparency | Minimum standard for how prices are written; applies to unregulated industries too (8.2, 8.8) | `cccs.gov.sg/consumer-protection/legislation-and-guidelines/guidelines-on-price-transparency` |
| Singapore statute | CPFTA, Consumer Protection (Fair Trading) Act | Same as above | `sso.agc.gov.sg/Act/CPFTA2003` |
| PDPC | Do Not Call Registry and your business | Check the Do Not Call registry before outreach (8.2) | `pdpc.gov.sg/overview-of-pdpa/do-not-call-registry/business-owner/do-not-call-registry-and-your-business` |
| China Law Translate | English translation of China's Advertising Law (2021) | Chinese-language pages aimed at mainland consumers avoid absolute claims (8.9) | `chinalawtranslate.com/advertising-law-2021/` |
| State Administration for Market Regulation (China) | Enforcement guidelines on absolute terms in advertising | Same as above. Marked in the book as "source text not obtained; not a basis for relaxing a rule" | Not given in the appendix |

Industry regulators' advertising codes, with their original text, clause numbers and links, are in the appendix of each industry edition and are not repeated here.

#### 1.4 Our own measurements (the book's main evidence)

Both rounds were completed on 2026-09-23 and covered five Singapore industries: dental and aesthetics, family law, tuition and education, B2B SaaS, and e-commerce and consumer goods.

- **Two-engine round**: 60 questions, 6 of them in Chinese (2 each in dental, legal and tuition). Both ChatGPT and Google AI Mode were tested: 526 citations across about 300 domains, with 92 pages taken apart one by one.
- **ChatGPT-only round**: 10 questions per industry, ChatGPT only (OpenAI API, gpt-5.5 + web_search, Singapore location). 241 citations. Page-type tallies (228 mentions of page types not seen in the first round, 63 of the nine known ones) combine the official run and one extra run, so they are mention counts, not citation counts.

Appendix A.3 and A.4 give the method for every figure.

#### 1.5 Related Canlah public repos

- **seven-engines-geo-forensics**: https://github.com/Canlah-AI/seven-engines-geo-forensics (README states CC BY 4.0; DOI 10.5281/zenodo.22225223). On the night of 2026-08-29 we put one commercial question, in English and Chinese, to seven search and AI-answer engines. We captured every cited page, classified the pages with frozen code, and checked each engine's published retrieval claims one by one.
- **How the two repos link**: that repo asks whether different engines cite the same sources (one question, seven engines, one night). This book asks the next question: what does a cited page look like, and how should you write one (110 questions over two rounds, two engines, five industries)? This page links to it for the raw data and code you can rerun, and its README will get a line linking back here.

### 2. Where we differ

aaron-marketing-skills covers seven marketing disciplines with 120 skills. This book covers one thing: getting your pages cited in AI answers in Singapore. The six points below are differences in scope and method, each with the section that supports it.

**1. Every rule states its evidence and sample size.**

- Rules carry one of three labels: "measured n/N", "measured, 1 case" or "not measured" (A.3).
- Page types fall into three evidence tiers: tier A was tested on both engines (9 types), tier B on ChatGPT only (33 types), and tier C comes only from an external teardown and has not been measured (4 types) (5.1).
- Where measurement conflicts with common practice, we follow the measurement. For example:
  - the quoted sentence is almost always the first sentence of a paragraph (legal 15/18);
  - about 73% of the quoted facts we could locate sit in the first 30% of the page (55/75);
  - few cited pages fall in the 1,800–3,000-word range (legal 2/18, tuition 2/8), so there is no global word minimum (A.3).
- Relation to aaron-marketing-skills: in our cited sample, how often pages had outbound links, bylines and question-style H2s did not match the CORE-EEAT thresholds:
  - pages with authoritative outbound links: dental 1/16, legal 2/18;
  - named individual authors: legal 2/18;
  - three or more question-style H2s: legal 3/18, SaaS 4/13.

  So the book does not treat outbound links or bylines as conditions for citation (bylines on medical pages are the exception, 6/12). H2s are statements, and questions go in the FAQ (A.3). This does not mean those rules have no value as writing-quality standards. CORE-EEAT says itself that it is "advisory until outcome-calibrated", and it measures content quality, not whether a page gets cited.

**2. ChatGPT and Google AI Mode are measured, and written for, separately.**

The two engines cite different kinds of pages (A.3):

| Industry | ChatGPT mostly cites | AI Mode mostly cites |
|---|---|---|
| Dental and aesthetics | Government and public institutions, 76% (38/50) | Clinics and other commercial sites, 75% (39/52) |
| Family law | .gov.sg, 77% (46/60) | Law firms and other commercial sites, 69% (36/52) |
| E-commerce and consumer goods | Product detail pages, 54% | Google Shopping cards, 44%. The two engines' cited URLs do not overlap at all |

So:

- every page carries two kinds of sentence: an "own sentence" for ChatGPT (your fixed price or spec) and a "market sentence" for AI Mode (a range, the factors behind it, and a source) (5.6);
- the 46-type index marks which engine mainly cites each type (5.1);
- retests record the two engines separately (Chapter 7).

**3. The 46 page types were counted one by one.**

- The count: 9 + 33 types from the two rounds, plus 5 from the external teardown, minus 1 duplicate, gives 46.
- The 46 types fall into six families: price, selection and reputation, questions and rules, entity and facts, primary sources, and commentary.
- Two pages count as the same type only if all three hold: the questions that trigger them belong to one family; the quoted sentence sits in the same place and form on the page; and one build spec can produce both (5.1, A.3).
- The number of types depends on how many kinds of question we test. It will grow as we test more.

**4. Regulated industries: three sides, six switches, three compliance labels.**

- **Decide your side first**: four questions place a business on the strictly regulated, lightly regulated or unregulated side. Six extra switches are then checked, such as liability for publishing on a client's behalf, legally required fields, and a ban on comparing with peers (0.2).
- **Openness per type**: each of the 46 types is marked build, adapt, cite-only or stop for each side (5.1).
- **Every compliance sentence carries a label**: "explicit in the rule text", "conservative line, not explicit in the rule text" or "source text not obtained". Sign-off works like this:
  - in three situations, writing stops and the client's compliance lead must sign off;
  - a sign-off can relax only two kinds of item: facts only the client knows, and conservative lines;
  - bans that are explicit in the rule text, and items marked "source text not obtained", stay in force even with a signature (0.4).
- **Rule text in the industry editions**: each rule comes with its clause number, the original sentence and a link (0.4).
- **Every ban has a replacement**: each ban says what to write in that slot instead, rather than leaving a gap (0.4).

**5. Chinese, and local to Singapore.**

- Every question was tested with a Singapore location, using keywords from Google autocomplete (gl=sg). In our data, ChatGPT mostly cited Singapore government and public pages such as MOH, CPF, judiciary and ask.gov.sg (A.3).
- A Chinese page is not a translation. Each buyer type gets an English page and a Chinese page by default, finished in the same batch (5.9).
- Three things are fixed on every Chinese page, and a page missing any one of them does not go live (5.9):
  - the H1 contains 新加坡 (Singapore);
  - the first paragraph has an S$ amount and says whether GST is included;
  - the body names at least one real MRT station or neighbourhood.
- The reason: in a live search, the answer to a Chinese question copied a foreign site's price in another currency (5.9).

**6. Separate editions by industry.**

- The general edition keeps only rules that hold across industries.
- Industry editions (dental and aesthetics so far) add that industry's rule text, clause numbers and links, table headers, and the three tasks for week one (0.4, A.1).
- Appendix C lists the ten-axis values for the five industries we measured. Chapter 8 gives four steps for judging an industry the book does not cover: ten questions, deciding the side, the ten axes, and a decision table.
- The same rule can reverse between industries. For example, an unregulated business may publish its own list page (disclosing if it ranks itself first), while a strictly regulated one does not publish list pages at all (5.1).

### 3. What we have not done

1. **Some data covers only one engine.** Tier B's 33 types have ChatGPT evidence only: the AI Mode probe quota ran out, so that engine was not run (the quota resets on 2026-09-29). As a result, that round could not detect page types that summarize other sources (A.4). Tier C's 4 types have no measurements at all (A.4). Some early figures come from one engine, one sample, without a Singapore location lock. The book forbids quoting them externally until they are retested (A.1, A.2).
2. **Quote positions are visual estimates.** Of 526 citations, only 75 could be traced to a specific sentence on the source page. Positions were estimated by eye from page length, not coded character by character (A.3). Only the first 600 characters of each answer were saved, so quotes in the second half of long answers cannot be matched sentence by sentence (A.3).
3. **No long-term results.** Both rounds are one-off snapshots from 2026-09. Pages built with this method have no follow-up data yet on rankings or AI citations after launch (5.D1). Timelines such as how soon entity fixes show up and how long off-site work takes are inferences, marked "not measured" in the book (A.1, A.2).
4. **Small samples, narrow scope.** Only five industries, all in Singapore. Keywords came only from Google autocomplete, without People Also Ask or Reddit threads (A.3). Many page types rest on a single case and are directional only (A.4). The finding that recommendation-style questions copy reviews rests on 15 samples (A.2).
5. **Our instruments have a bias.** Our probes run through APIs: the OpenAI API for ChatGPT and a third-party SERP API for AI Mode. Users of the web interfaces may see something different, and public research shows citation distributions differ systematically between API and web (A.2).
6. **Most outside studies use US or cross-industry samples.** Most have not been validated in Singapore, and many of the original studies give no link (A.1, A.5).
7. **The compliance rules are not legal advice.** In the general edition, a label describes the evidence level in an example industry, not the law in your industry. Some items are still marked "source text not obtained" (0.4).
8. **The raw data is not public yet.** The raw answers and page-by-page teardowns from both rounds have not been prepared as a public dataset. The book reports totals and sample URLs.
9. **The book still has loose ends.** For example, the source note on the pre-publish self-check does not match the actual number of questions. Appendix A.3 lists the mismatch as it stands; we did not paper over it.
