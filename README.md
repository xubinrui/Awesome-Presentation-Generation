# Awesome Presentation Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome resources for **automatic presentation, slide, and poster generation** — papers, datasets, benchmarks, tools, and products that turn ideas, documents, and data into beautiful decks.

Presentation generation sits at the intersection of large language models, multimodal understanding, document summarization, and layout design. This list tracks the fast-moving research literature alongside the open-source tooling and commercial products that make AI-powered deck creation real.

Contributions are very welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request.

## Contents

- [Surveys & Overviews](#surveys--overviews)
- [Papers](#papers)
  - [LLM & Agent-Based Slide Generation](#llm--agent-based-slide-generation)
  - [Document-to-Slides](#document-to-slides)
  - [Scientific Paper-to-Slides & Poster Generation](#scientific-paper-to-slides--poster-generation)
  - [Layout Generation](#layout-generation)
  - [Evaluation](#evaluation)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Open-Source Projects](#open-source-projects)
  - [AI / LLM Slide Generators](#ai--llm-slide-generators)
  - [Slide Frameworks & Authoring](#slide-frameworks--authoring)
  - [Programmatic Deck Libraries](#programmatic-deck-libraries)
- [Commercial Products](#commercial-products)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)
- [License](#license)

Legend: 📄 paper · 💻 code · 🗂️ dataset · 🌐 project page

---

## Surveys & Overviews

There is not yet a dedicated peer-reviewed survey focused solely on presentation generation. The closest entry points are the benchmark/framework papers that broadly review the field — **[PPTAgent](https://arxiv.org/abs/2501.03936)** (task formulation and evaluation) and **[AutoPresent](https://arxiv.org/abs/2501.00912)** (problem taxonomy and the SlidesBench benchmark) are the best starting points. *Contributions of a true survey paper are especially welcome.*

## Papers

### LLM & Agent-Based Slide Generation

- **PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides** (2025) — A two-stage, edit-based agentic framework that analyzes a reference deck, then iteratively generates editing actions; introduces the PPTEval framework (Content / Design / Coherence). [📄](https://arxiv.org/abs/2501.03936) [💻](https://github.com/icip-cas/PPTAgent)
- **AutoPresent: Designing Structured Visuals from Scratch** (CVPR 2025) — An 8B Llama-based model trained on 7k instruction–code pairs that generates slides programmatically; introduces the SlidesBench benchmark. [📄](https://arxiv.org/abs/2501.00912) [💻](https://github.com/para-lost/AutoPresent)
- **Textual-to-Visual Iterative Self-Verification for Slide Generation** (2025) — Decomposes slide generation into content and layout, with an LLM Reviewer + Refiner self-verification loop that renders textual layouts to visual form for review. [📄](https://arxiv.org/abs/2502.15412)
- **PASS: Presentation Automation for Slide Generation and Speech** (2025) — A modular pipeline automating both slide generation and AI voiceover delivery from a document. [📄](https://arxiv.org/abs/2501.06497)
- **EvoPresent: Self-Improvement Aesthetic Agents for Academic Presentations** (2025) — A self-improvement agent framework unifying narrative, aesthetic design, and virtual-character delivery; introduces PresAesth, a multi-task RL aesthetic model. [📄](https://arxiv.org/abs/2510.05571) [💻](https://github.com/eric-ai-lab/EvoPresent)
- **SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation** (2025) — A visual-in-the-loop multi-agent framework (Outliner, Mapper, Speaker, Arranger, Refiner) that turns papers into editable PPTX. [📄](https://arxiv.org/abs/2512.04529)

### Document-to-Slides

- **DOC2PPT: Automatic Presentation Slides Generation from Scientific Documents** (AAAI 2022) — Seminal work: hierarchical seq2seq with summarization, retrieval, and layout prediction; released a ~6K paired document–slide dataset. [📄](https://arxiv.org/abs/2101.11796)
- **D2S: Document-to-Slide Generation via Query-Based Text Summarization** (NAACL 2021) — Title-driven retrieval plus BART long-form QA summarization; introduces the SciDuet dataset. [📄](https://arxiv.org/abs/2105.03664) [🗂️](https://gem-benchmark.com/data_cards/SciDuet)
- **Presentations Are Not Always Linear! GNN Meets LLM for Document-to-Presentation Transformation with Attribution** (EMNLP Findings 2024) — Combines a GNN and an LLM to capture non-linear content-to-slide mapping with source attribution. [📄](https://arxiv.org/abs/2405.13095)
- **Enhancing Presentation Slide Generation by LLMs with a Multi-Staged End-to-End Approach (DocPres)** (INLG 2024) — A multi-stage LLM + VLM pipeline that splits long multimodal documents into shorter sub-tasks. [📄](https://arxiv.org/abs/2406.06556)

### Scientific Paper-to-Slides & Poster Generation

- **Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers** (NeurIPS 2025 D&B) — Introduces the first poster-generation benchmark and metric suite (Visual Quality, Textual Coherence, PaperQuiz) plus PosterAgent, a top-down multi-agent pipeline. [📄](https://arxiv.org/abs/2505.21497) [💻](https://github.com/Paper2Poster/Paper2Poster) [🌐](https://paper2poster.github.io/)
- **PosterGen: Aesthetic-Aware Paper-to-Poster Generation via Multi-Agent LLMs** (2025) — A four-agent design workflow (Parser/Curator, Layout, Stylist, Renderer) with a VLM-based design rubric. [📄](https://arxiv.org/abs/2508.17188) [💻](https://github.com/Y-Research-SBU/PosterGen)
- **Neural Content Extraction for Poster Generation of Scientific Papers** (2021) — Treats poster generation as document summarization; a neural extractive model jointly extracts text, figures, and tables. [📄](https://arxiv.org/abs/2112.08550)
- **Learning to Generate Posters of Scientific Papers** (AAAI 2016) — Seminal data-driven graphical-model framework for poster panel layout; released a labeled Poster–Paper dataset. [📄](https://arxiv.org/abs/1604.01219)

### Layout Generation

- **PosterLlama: Bridging Design Ability of Language Model to Content-Aware Layout Generation** (ECCV 2024) — Reformats layout elements as HTML to leverage LLM design knowledge via two-stage vision-language training. [📄](https://arxiv.org/abs/2404.00995)
- **PosterLLaVa: Constructing a Unified Multi-modal Layout Generator with LLM** (2024) — A unified multimodal LLM-based layout generator spanning multiple design domains. [📄](https://arxiv.org/abs/2406.02884)
- **Relation-Aware Diffusion Model for Controllable Poster Layout Generation** (CIKM 2023) — A diffusion-based model incorporating element relations for controllable poster layouts. [📄](https://arxiv.org/abs/2306.09086)

### Evaluation

- **PPTEval** (2025) — Multi-dimensional evaluation of generated presentations across Content, Design, and Coherence; introduced with PPTAgent. [📄](https://arxiv.org/abs/2501.03936)
- **REFLEX: A Reference-Free Framework to Evaluate Presentation Content with Actionable Feedback** (2025) — Reference-free metrics plus the RefSlides benchmark; fine-tunes LLMs on perturbed negative samples to produce scores and feedback. [📄](https://arxiv.org/abs/2505.18240)
- **SlideAudit: A Dataset and Taxonomy for Automated Evaluation of Presentation Slides** (UIST 2025) — An expert-derived taxonomy of slide design flaws plus 2,400 annotated slides; benchmarks LLMs at flaw detection. [📄](https://arxiv.org/abs/2508.03630)

## Datasets & Benchmarks

- **SlidesBench** — The first slide-generation benchmark: 7k training and 585 test examples across 10 domains (from AutoPresent). [💻](https://github.com/para-lost/AutoPresent)
- **PPTC: Evaluating LLMs for PowerPoint Task Completion** (ACL Findings 2024) — 279 multi-turn sessions for creating/editing PPTX, with a PPTX-Match evaluation system. [📄](https://arxiv.org/abs/2311.01767) [💻](https://github.com/gydpku/PPTC)
- **PPTC-R: Evaluating the Robustness of LLMs for PowerPoint Task Completion** (2024) — A robustness variant of PPTC across instruction perturbations and software versions. [📄](https://arxiv.org/abs/2403.03788)
- **SlideVQA: Document Visual Question Answering on Multiple Images** (AAAI 2023) — 2.6k+ slide decks / 52k+ images / 14.5k questions requiring single-hop, multi-hop, and numerical reasoning. [📄](https://arxiv.org/abs/2301.04883) [🗂️](https://huggingface.co/datasets/NTT-hil-insight/SlideVQA)
- **SciDuet** — Paper–slide pairs scraped from ICML'19, NeurIPS'18&19, and ACL; introduced with D2S. [🗂️](https://gem-benchmark.com/data_cards/SciDuet)

## Open-Source Projects

### AI / LLM Slide Generators

- **[Presenton](https://github.com/presenton/presenton)** — Open-source, locally-runnable AI presentation generator with an API; exports PPTX/PDF (a Gamma / Beautiful.ai alternative).
- **[PPTAgent](https://github.com/icip-cas/PPTAgent)** — The reference implementation of the agentic, edit-based reflective PowerPoint generation framework.
- **[AutoPresent](https://github.com/para-lost/AutoPresent)** — Model, training data, and the SlidesBench benchmark for generating slides as code.
- **[Powerpointer-For-Local-LLMs](https://github.com/CyberTimon/Powerpointer-For-Local-LLMs)** — Generates PPTX using local, OpenAI-compatible LLMs plus python-pptx.

### Slide Frameworks & Authoring

- **[reveal.js](https://github.com/hakimel/reveal.js)** — The de-facto HTML presentation framework, with Markdown support.
- **[Slidev](https://github.com/slidevjs/slidev)** — Developer-focused, Vue-based slides written in extended Markdown.
- **[Marp](https://github.com/marp-team/marp-cli)** / **[Marpit](https://github.com/marp-team/marpit)** — Markdown presentation ecosystem; exports HTML/PDF/PPTX.
- **[Quarto](https://github.com/quarto-dev/quarto-cli)** — Scientific publishing system; renders reveal.js / Beamer / PPTX from Markdown plus code.
- **[Spectacle](https://github.com/FormidableLabs/spectacle)** — A React-based presentation library.
- **[remark](https://github.com/gnab/remark)** — A simple, in-browser, Markdown-driven slideshow tool.
- **[reveal-md](https://github.com/webpro/reveal-md)** — Run reveal.js presentations straight from Markdown files.

### Programmatic Deck Libraries

- **[python-pptx](https://github.com/scanny/python-pptx)** — Python library to create, read, and update PPTX files. The backbone of most LLM slide generators.
- **[PptxGenJS](https://github.com/gitbrent/PptxGenJS)** — Build PowerPoint PPTX in JavaScript (Node, React, browser).
- **[Apache POI](https://github.com/apache/poi)** — Java library for Microsoft Office formats including PPTX (HSLF/XSLF).
- **[Pandoc](https://github.com/jgm/pandoc)** — Universal document converter; outputs reveal.js, Beamer, PPTX, and more.

## Commercial Products

| Product | Description |
| --- | --- |
| [Gamma](https://gamma.app) | Market-leading text-to-deck AI; generates full decks from a prompt in seconds. |
| [Microsoft 365 Copilot](https://www.microsoft.com/microsoft-365/copilot) | AI slide designer built into PowerPoint; generates decks from prompts and documents. |
| [Canva Magic Design](https://www.canva.com/magic-design/) | Turns a short prompt into polished deck themes inside Canva's editor. |
| [Beautiful.ai](https://www.beautiful.ai) | AI presentation maker with smart templates and auto-layout; enterprise-ready. |
| [Plus AI](https://plusai.com) | AI add-on with native Google Slides / PowerPoint integration. |
| [SlidesAI](https://www.slidesai.io) | Text-to-slides add-on, best for Google Slides users. |
| [MagicSlides](https://www.magicslides.app) | AI PPT maker from URLs, PDFs, and YouTube in 100+ languages. |
| [Decktopus](https://www.decktopus.com) | Budget AI deck generator with templates and PPTX export. |
| [Presentations.ai](https://www.presentations.ai) | Design-centric AI deck platform with PPTX export. |
| [Pitch](https://pitch.com) | Collaborative presentation platform with AI assistance. |
| [Chronicle](https://chroniclehq.com) | AI-native presentation/storytelling tool with interactive blocks. |
| [Napkin AI](https://www.napkin.ai) | Turns text into editable diagrams and visuals for slides. |
| [Tongyi 通义](https://tongyi.aliyun.com) | Alibaba's LLM with one-sentence / document / audio-to-PPT agents. |
| [iFlytek Zhiwen 讯飞智文](https://zhiwen.xfyun.cn) | Spark-based AI PPT / Word / mind-map generator with speech-script export. |
| [Mindshow](https://www.mindshow.fun) | LLM-backed outline-to-slides tool. |
| [AiPPT](https://www.aippt.com) | One-click AI PowerPoint / Google Slides generator. |

> Note: [Tome](https://tome.app) was an influential AI deck tool but **discontinued its AI slide generation in April 2025** and pivoted to a sales platform; it is listed here for historical reference.

## Related Awesome Lists

- [awesome-llm](https://github.com/Hannibal046/Awesome-LLM) — Large language models, the foundation of modern presentation generation.
- [awesome-document-understanding](https://github.com/tstanislawek/awesome-document-understanding) — Document AI, closely related to document-to-slides.
- [awesome-multimodal-large-language-models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) — Multimodal LLMs used for slide and layout understanding.

## Contributing

Contributions of any size are welcome — a new paper, a fixed link, a better description. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for the guidelines and quality bar.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work. See [LICENSE](LICENSE).
