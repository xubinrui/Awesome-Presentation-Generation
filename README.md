# Awesome Presentation Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources for **automatic presentation, slide, and poster generation** — organized by generation paradigm.

## Contents

- [Papers](#papers)
  - [Prompt / Topic → Slides](#prompt--topic--slides)
  - [Document → Slides](#document--slides)
  - [Paper / Document → Poster](#paper--document--poster)
  - [Layout Generation](#layout-generation)
  - [Evaluation](#evaluation)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Open-Source Projects](#open-source-projects)
  - [AI Slide & Poster Generators](#ai-slide--poster-generators)
  - [Slide Authoring Frameworks](#slide-authoring-frameworks)
  - [Programmatic Deck Libraries](#programmatic-deck-libraries)
- [Commercial Products](#commercial-products)
  - [General-Purpose AI Generators](#general-purpose-ai-generators)
  - [Plug-in / Add-on Tools](#plug-in--add-on-tools)
  - [Document & File Input](#document--file-input)
  - [Chinese-Market Products](#chinese-market-products)
- [Related Awesome Lists](#related-awesome-lists)

---

## Papers

### Prompt / Topic → Slides

> The model receives a short text prompt or topic and generates a complete slide deck.

| Paper | Venue | Year | Paradigm | Links |
|-------|-------|------|----------|-------|
| [PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides](https://arxiv.org/abs/2501.03936) | arXiv | 2025 | Agentic edit-based (analyze reference deck → iterative edits) | [📄](https://arxiv.org/abs/2501.03936) [💻](https://github.com/icip-cas/PPTAgent) |
| [AutoPresent: Designing Structured Visuals from Scratch](https://arxiv.org/abs/2501.00912) | CVPR 2025 | 2025 | Code generation (8B Llama → rendering code) | [📄](https://arxiv.org/abs/2501.00912) [💻](https://github.com/para-lost/AutoPresent) |
| [Textual-to-Visual Iterative Self-Verification for Slide Generation](https://arxiv.org/abs/2502.15412) | arXiv | 2025 | LLM pipeline · Reviewer–Refiner self-verification loop | [📄](https://arxiv.org/abs/2502.15412) |
| [EvoPresent: Self-Improvement Aesthetic Agents for Academic Presentations](https://arxiv.org/abs/2510.05571) | ICLR 2026 | 2025 | Agentic · multi-task RL aesthetic model (PresAesth) | [📄](https://arxiv.org/abs/2510.05571) [💻](https://github.com/eric-ai-lab/EvoPresent) |
| [PASS: Presentation Automation for Slide Generation and Speech](https://arxiv.org/abs/2501.06497) | arXiv | 2025 | LLM pipeline · slides + AI voiceover | [📄](https://arxiv.org/abs/2501.06497) |

### Document → Slides

> The model ingests a long document (report, paper, PDF) and converts it into structured slides.

| Paper | Venue | Year | Paradigm | Links |
|-------|-------|------|----------|-------|
| [DOC2PPT: Automatic Presentation Slides Generation from Scientific Documents](https://arxiv.org/abs/2101.11796) | AAAI 2022 | 2021 | Hierarchical Seq2Seq · summarization + retrieval + layout | [📄](https://arxiv.org/abs/2101.11796) |
| [D2S: Document-to-Slide Generation via Query-Based Text Summarization](https://arxiv.org/abs/2105.03664) | NAACL 2021 | 2021 | Retrieval + BART summarization (introduces SciDuet) | [📄](https://arxiv.org/abs/2105.03664) [🗂️](https://gem-benchmark.com/data_cards/SciDuet) |
| [GNN Meets LLM for Document-to-Presentation Transformation with Attribution](https://arxiv.org/abs/2405.13095) | EMNLP Findings 2024 | 2024 | GNN + LLM · non-linear mapping with source attribution | [📄](https://arxiv.org/abs/2405.13095) |
| [Enhancing Presentation Slide Generation by LLMs: A Multi-Staged Approach (DocPres)](https://arxiv.org/abs/2406.06556) | INLG 2024 | 2024 | Multi-stage LLM + VLM pipeline | [📄](https://arxiv.org/abs/2406.06556) |
| [SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation](https://arxiv.org/abs/2512.04529) | arXiv | 2025 | Multi-agent · Outliner → Mapper → Speaker → Arranger → Refiner | [📄](https://arxiv.org/abs/2512.04529) |

### Paper / Document → Poster

> Scientific paper or document as input; the output is a formatted research poster.

| Paper | Venue | Year | Paradigm | Links |
|-------|-------|------|----------|-------|
| [Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers](https://arxiv.org/abs/2505.21497) | NeurIPS 2025 D&B | 2025 | Multi-agent (top-down PosterAgent) · first poster benchmark | [📄](https://arxiv.org/abs/2505.21497) [💻](https://github.com/Paper2Poster/Paper2Poster) [🌐](https://paper2poster.github.io/) |
| [PosterGen: Aesthetic-Aware Paper-to-Poster Generation via Multi-Agent LLMs](https://arxiv.org/abs/2508.17188) | 2025 | 2025 | Multi-agent · Parser → Layout → Stylist → Renderer | [📄](https://arxiv.org/abs/2508.17188) [💻](https://github.com/Y-Research-SBU/PosterGen) |
| [Neural Content Extraction for Poster Generation of Scientific Papers](https://arxiv.org/abs/2112.08550) | arXiv | 2021 | Neural extraction · text + figures + tables jointly | [📄](https://arxiv.org/abs/2112.08550) |
| [Learning to Generate Posters of Scientific Papers](https://arxiv.org/abs/1604.01219) | AAAI 2016 | 2016 | Data-driven graphical model · panel layout prediction | [📄](https://arxiv.org/abs/1604.01219) |

### Layout Generation

> Models focused on placing and sizing elements (text boxes, images, charts) on a slide or poster canvas.

| Paper | Venue | Year | Paradigm | Links |
|-------|-------|------|----------|-------|
| [PosterLlama: Bridging Design Ability of LM to Content-Aware Layout Generation](https://arxiv.org/abs/2404.00995) | ECCV 2024 | 2024 | LLM · elements serialized as HTML; two-stage VL training | [📄](https://arxiv.org/abs/2404.00995) |
| [PosterLLaVa: A Unified Multi-modal Layout Generator with LLM](https://arxiv.org/abs/2406.02884) | arXiv | 2024 | Multimodal LLM · unified across design domains | [📄](https://arxiv.org/abs/2406.02884) |
| [Relation-Aware Diffusion Model for Controllable Poster Layout Generation](https://arxiv.org/abs/2306.09086) | CIKM 2023 | 2023 | Diffusion · element-relation conditioning | [📄](https://arxiv.org/abs/2306.09086) |

### Evaluation

> Frameworks and benchmarks designed to assess quality of generated presentations.

| Paper | Venue | Year | What it Measures | Links |
|-------|-------|------|-----------------|-------|
| [PPTEval](https://arxiv.org/abs/2501.03936) | arXiv | 2025 | Content · Design · Coherence (introduced with PPTAgent) | [📄](https://arxiv.org/abs/2501.03936) |
| [REFLEX: Reference-Free Evaluation of Presentation Content](https://arxiv.org/abs/2505.18240) | arXiv | 2025 | Reference-free quality score + actionable feedback; RefSlides benchmark | [📄](https://arxiv.org/abs/2505.18240) |
| [SlideAudit: Automated Evaluation of Presentation Slides](https://arxiv.org/abs/2508.03630) | UIST 2025 | 2025 | Design-flaw taxonomy; 2,400 expert-annotated slides | [📄](https://arxiv.org/abs/2508.03630) |

---

## Datasets & Benchmarks

| Dataset | Year | Size | Task | Links |
|---------|------|------|------|-------|
| [SlidesBench](https://github.com/para-lost/AutoPresent) | 2025 | 7k train / 585 test · 10 domains | Slide generation | [💻](https://github.com/para-lost/AutoPresent) |
| [PPTC](https://arxiv.org/abs/2311.01767) | 2023 | 279 multi-turn sessions | PPTX task completion (create / edit) | [📄](https://arxiv.org/abs/2311.01767) [💻](https://github.com/gydpku/PPTC) |
| [PPTC-R](https://arxiv.org/abs/2403.03788) | 2024 | PPTC + perturbations | PPTX task robustness | [📄](https://arxiv.org/abs/2403.03788) |
| [SlideVQA](https://arxiv.org/abs/2301.04883) | 2023 | 2.6k decks / 52k images / 14.5k Qs | Slide visual question answering | [📄](https://arxiv.org/abs/2301.04883) [🗂️](https://huggingface.co/datasets/NTT-hil-insight/SlideVQA) |
| [SciDuet](https://gem-benchmark.com/data_cards/SciDuet) | 2021 | ICML'19 + NeurIPS'18&19 + ACL pairs | Document-to-slide retrieval | [🗂️](https://gem-benchmark.com/data_cards/SciDuet) |

---

## Open-Source Projects

### AI Slide & Poster Generators

| Project | Input | Output | Description | Links |
|---------|-------|--------|-------------|-------|
| [Presenton](https://github.com/presenton/presenton) | Text prompt / doc | PPTX · PDF | Self-hostable AI generator with REST API | [💻](https://github.com/presenton/presenton) |
| [PPTAgent](https://github.com/icip-cas/PPTAgent) | Topic + reference deck | PPTX | Agentic, edit-based generation (ICIP-CAS) | [💻](https://github.com/icip-cas/PPTAgent) |
| [AutoPresent](https://github.com/para-lost/AutoPresent) | Text instruction | HTML / slides | Code-gen model + SlidesBench benchmark | [💻](https://github.com/para-lost/AutoPresent) |
| [Powerpointer-For-Local-LLMs](https://github.com/CyberTimon/Powerpointer-For-Local-LLMs) | Text prompt | PPTX | Local OpenAI-compatible LLM + python-pptx | [💻](https://github.com/CyberTimon/Powerpointer-For-Local-LLMs) |

### Slide Authoring Frameworks

> Markdown / code → presentation (no AI generation; used as rendering backends by AI tools).

| Project | Language / Stack | Output Formats | Description | Links |
|---------|-----------------|---------------|-------------|-------|
| [reveal.js](https://github.com/hakimel/reveal.js) | HTML / JS | HTML · PDF | De-facto HTML presentation framework | [💻](https://github.com/hakimel/reveal.js) |
| [Slidev](https://github.com/slidevjs/slidev) | Vue / Markdown | HTML · PDF · PPTX | Developer-focused slides from extended Markdown | [💻](https://github.com/slidevjs/slidev) |
| [Marp](https://github.com/marp-team/marp-cli) | Markdown | HTML · PDF · PPTX | Markdown presentation ecosystem | [💻](https://github.com/marp-team/marp-cli) |
| [Quarto](https://github.com/quarto-dev/quarto-cli) | Markdown + code | reveal.js · Beamer · PPTX | Scientific publishing system | [💻](https://github.com/quarto-dev/quarto-cli) |
| [Spectacle](https://github.com/FormidableLabs/spectacle) | React / JSX | HTML | React-based presentation library | [💻](https://github.com/FormidableLabs/spectacle) |
| [remark](https://github.com/gnab/remark) | Markdown | HTML | In-browser Markdown-driven slides | [💻](https://github.com/gnab/remark) |
| [reveal-md](https://github.com/webpro/reveal-md) | Markdown | HTML · PDF | Run reveal.js from plain Markdown files | [💻](https://github.com/webpro/reveal-md) |

### Programmatic Deck Libraries

> Libraries for reading and writing PPTX/ODP files in code — the backbone of most LLM generators.

| Library | Language | Description | Links |
|---------|----------|-------------|-------|
| [python-pptx](https://github.com/scanny/python-pptx) | Python | Create, read, and update PPTX files | [💻](https://github.com/scanny/python-pptx) |
| [PptxGenJS](https://github.com/gitbrent/PptxGenJS) | JavaScript | Build PPTX in Node, React, or browser | [💻](https://github.com/gitbrent/PptxGenJS) |
| [Apache POI](https://github.com/apache/poi) | Java | MS Office formats including PPTX (HSLF / XSLF) | [💻](https://github.com/apache/poi) |
| [Pandoc](https://github.com/jgm/pandoc) | Haskell / CLI | Universal converter → reveal.js, Beamer, PPTX | [💻](https://github.com/jgm/pandoc) |

---

## Commercial Products

### General-Purpose AI Generators

> Create slides from a text prompt or outline; no source document required.

| Product | Input | Export | Notable Feature |
|---------|-------|--------|----------------|
| [Gamma](https://gamma.app) | Prompt · outline | PDF · PPT · web | Largest user base (70M+); one-click regeneration |
| [Beautiful.ai](https://www.beautiful.ai) | Prompt · outline | PPTX · PDF | Smart slide templates with auto-layout |
| [Decktopus](https://www.decktopus.com) | Prompt | PPTX · PDF | Built-in form & voiceover features |
| [Presentations.ai](https://www.presentations.ai) | Prompt | PPTX | Design-first; brand kit support |
| [Pitch](https://pitch.com) | Prompt · template | PDF · PPTX | Team collaboration + analytics |
| [Chronicle](https://chroniclehq.com) | Prompt · block editor | PDF | Interactive story blocks |
| [AiPPT](https://www.aippt.com) | Prompt | PPTX · PDF | One-click generation; 200+ templates |

### Plug-in / Add-on Tools

> Work inside existing editors (PowerPoint, Google Slides) rather than replacing them.

| Product | Platform | Notable Feature |
|---------|----------|----------------|
| [Microsoft 365 Copilot](https://www.microsoft.com/microsoft-365/copilot) | PowerPoint (native) | Generates decks from Word docs, prompts, or meeting notes |
| [Canva Magic Design](https://www.canva.com/magic-design/) | Canva | Prompt → branded deck; integrated asset library |
| [Plus AI](https://plusai.com) | Google Slides · PowerPoint | Edits existing decks; brand style learning |
| [SlidesAI](https://www.slidesai.io) | Google Slides | Text-to-slides add-on; script import |
| [MagicSlides](https://www.magicslides.app) | Google Slides · PowerPoint | Input: URL, PDF, YouTube, text; 100+ languages |

### Document & File Input

> Products that accept a document, PDF, or URL as the primary source.

| Product | Input Types | Notable Feature |
|---------|------------|----------------|
| [Napkin AI](https://www.napkin.ai) | Text / notes | Converts text into diagrams and infographics for slides |
| [Slidebean](https://slidebean.com) | Outline · template | Startup-focused; pitch deck financial model builder |

### Chinese-Market Products

| Product | Company | Input | Notable Feature |
|---------|---------|-------|----------------|
| [通义 (Tongyi)](https://tongyi.aliyun.com) | Alibaba | Prompt · doc · audio | One-sentence / document / voice → PPT |
| [讯飞智文 (Zhiwen)](https://zhiwen.xfyun.cn) | iFlytek | Prompt · doc | PPTX + Word + mind map; speech-script export |
| [Kimi](https://kimi.moonshot.cn) | Moonshot AI | Prompt · doc | AiPPT agent integration |
| [Mindshow](https://www.mindshow.fun) | Mindshow | Outline | Outline → slides; GPT-backed |

> ⚠️ [Tome](https://tome.app) discontinued AI slide generation in April 2025 and pivoted to a sales platform.

---

## Related Awesome Lists

| List | Description |
|------|-------------|
| [awesome-llm](https://github.com/Hannibal046/Awesome-LLM) | Large language models — the foundation of modern slide generation |
| [awesome-document-understanding](https://github.com/tstanislawek/awesome-document-understanding) | Document AI, closely related to document-to-slides |
| [awesome-multimodal-large-language-models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) | Multimodal LLMs used in slide and layout understanding |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs for new papers, tools, or fixes are welcome.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)
