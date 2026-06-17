# Awesome Presentation Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources for **automatic presentation, slide, and poster generation** — organized by generation paradigm.

## Contents

- [Papers](#papers)
  - [Prompt / Topic → Slides](#prompt--topic--slides)
  - [Document → Slides](#document--slides)
  - [Paper / Document → Poster](#paper--document--poster)
  - [Slide Editing & Agentic Manipulation](#slide-editing--agentic-manipulation)
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
| [DeepPresenter: Environment-Grounded Reflection for Agentic Presentation Generation](https://arxiv.org/abs/2602.22839) | arXiv | 2026 | Dual-agent (Researcher + Presenter) · environment-grounded reflection on rendered slides; SOTA with reduced cost | [📄](https://arxiv.org/abs/2602.22839) [💻](https://github.com/icip-cas/PPTAgent) |
| [Design First, Code Later: Aesthetically Pleasing Template-Free Slides Generation (DeepSlides)](https://arxiv.org/abs/2605.26451) | arXiv | 2026 | Hierarchical decoupled design-then-code workflow; SlideQwens models (multi-agent RL); SlideDesign dataset | [📄](https://arxiv.org/abs/2605.26451) |

### Document → Slides

> The model ingests a long document (report, paper, PDF) and converts it into structured slides.

| Paper | Venue | Year | Paradigm | Links |
|-------|-------|------|----------|-------|
| [DOC2PPT: Automatic Presentation Slides Generation from Scientific Documents](https://arxiv.org/abs/2101.11796) | AAAI 2022 | 2021 | Hierarchical Seq2Seq · summarization + retrieval + layout | [📄](https://arxiv.org/abs/2101.11796) |
| [D2S: Document-to-Slide Generation via Query-Based Text Summarization](https://arxiv.org/abs/2105.03664) | NAACL 2021 | 2021 | Retrieval + BART summarization (introduces SciDuet) | [📄](https://arxiv.org/abs/2105.03664) [🗂️](https://gem-benchmark.com/data_cards/SciDuet) |
| [GNN Meets LLM for Document-to-Presentation Transformation with Attribution](https://arxiv.org/abs/2405.13095) | EMNLP Findings 2024 | 2024 | GNN + LLM · non-linear mapping with source attribution | [📄](https://arxiv.org/abs/2405.13095) |
| [Enhancing Presentation Slide Generation by LLMs: A Multi-Staged Approach (DocPres)](https://arxiv.org/abs/2406.06556) | INLG 2024 | 2024 | Multi-stage LLM + VLM pipeline | [📄](https://arxiv.org/abs/2406.06556) |
| [SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation](https://arxiv.org/abs/2512.04529) | arXiv | 2025 | Multi-agent · Outliner → Mapper → Speaker → Arranger → Refiner | [📄](https://arxiv.org/abs/2512.04529) |
| [PresentAgent: Multimodal Agent for Presentation Video Generation](https://arxiv.org/abs/2507.04036) | arXiv | 2025 | Multimodal agent · document → narrated presentation *video* (slides + synced speech); PresentEval | [📄](https://arxiv.org/abs/2507.04036) |
| [Auto-Slides: An Interactive Multi-Agent System for Creating and Customizing Research Presentations](https://arxiv.org/abs/2509.11062) | arXiv | 2025 | Interactive multi-agent · paper → pedagogically structured multimodal slides with editing | [📄](https://arxiv.org/abs/2509.11062) [🌐](https://auto-slides.github.io/) |
| [SlideBot: A Multi-Agent Framework for Generating Informative, Reliable, Multi-Modal Presentations](https://arxiv.org/abs/2511.09804) | EAAI 2026 | 2025 | Multi-agent · retrieval + structured planning + code-gen; grounding to reduce hallucination | [📄](https://arxiv.org/abs/2511.09804) |
| [SlideTailor: Personalized Presentation Slide Generation for Scientific Papers](https://arxiv.org/abs/2512.20292) | AAAI 2026 | 2025 | Agentic · preference-conditioned, progressively generated editable slides; chain-of-speech | [📄](https://arxiv.org/abs/2512.20292) |
| [Narrative-Driven Paper-to-Slide Generation via ArcDeck](https://arxiv.org/abs/2604.11969) | arXiv | 2026 | Multi-agent · discourse-tree structure modeling for narrative coherence; ArcBench | [📄](https://arxiv.org/abs/2604.11969) |
| [Paper2Video: Automatic Video Generation from Scientific Papers](https://arxiv.org/abs/2510.05096) | arXiv | 2025 | Multi-agent PaperTalker · slides + subtitles + speech + talking-head rendering; Paper2Video benchmark (101 pairs) | [📄](https://arxiv.org/abs/2510.05096) [💻](https://github.com/showlab/Paper2Video) [🌐](https://showlab.github.io/Paper2Video/) |
| [SynLecSlideGen: AI-Generated Lecture Slides for Improving Slide Element Detection and Retrieval](https://arxiv.org/abs/2506.23605) | ECIR 2026 | 2025 | LLM + web-image pipeline → synthetic lecture slides for pretraining; RealSlide benchmark (1,050 annotated slides) | [📄](https://arxiv.org/abs/2506.23605) |

### Paper / Document → Poster

> Scientific paper or document as input; the output is a formatted research poster.

| Paper | Venue | Year | Paradigm | Links |
|-------|-------|------|----------|-------|
| [Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers](https://arxiv.org/abs/2505.21497) | NeurIPS 2025 D&B | 2025 | Multi-agent (top-down PosterAgent) · first poster benchmark | [📄](https://arxiv.org/abs/2505.21497) [💻](https://github.com/Paper2Poster/Paper2Poster) [🌐](https://paper2poster.github.io/) |
| [PosterGen: Aesthetic-Aware Paper-to-Poster Generation via Multi-Agent LLMs](https://arxiv.org/abs/2508.17188) | 2025 | 2025 | Multi-agent · Parser → Layout → Stylist → Renderer | [📄](https://arxiv.org/abs/2508.17188) [💻](https://github.com/Y-Research-SBU/PosterGen) |
| [Neural Content Extraction for Poster Generation of Scientific Papers](https://arxiv.org/abs/2112.08550) | arXiv | 2021 | Neural extraction · text + figures + tables jointly | [📄](https://arxiv.org/abs/2112.08550) |
| [Learning to Generate Posters of Scientific Papers](https://arxiv.org/abs/1604.01219) | AAAI 2016 | 2016 | Data-driven graphical model · panel layout prediction | [📄](https://arxiv.org/abs/1604.01219) |
| [P2P: Automated Paper-to-Poster Generation and Fine-Grained Benchmark](https://arxiv.org/abs/2505.17104) | ICLR 2026 | 2025 | LLM multi-agent · HTML-rendered posters; P2PInstruct (30k+) + P2PEval | [📄](https://arxiv.org/abs/2505.17104) [💻](https://github.com/multimodal-art-projection/P2P) |
| [SciPostGen: Bridging the Gap between Scientific Papers and Poster Layouts](https://arxiv.org/abs/2511.22490) | arXiv | 2025 | Retrieval-augmented poster layout generation + large-scale paper→layout dataset | [📄](https://arxiv.org/abs/2511.22490) [🌐](https://omron-sinicx.github.io/paper2layout/) |

### Slide Editing & Agentic Manipulation

> Models and benchmarks for *editing* existing decks via natural-language instructions (rather than generating from scratch).

| Paper | Venue | Year | Paradigm | Links |
|-------|-------|------|----------|-------|
| [Talk to Your Slides: High-Efficiency Slide Editing via Language-Driven Structured Data Manipulation](https://arxiv.org/abs/2505.11604) | ACL 2026 | 2025 | LLM agent · edits underlying structured slide data (not pixels); TSBench (379 instructions) | [📄](https://arxiv.org/abs/2505.11604) [💻](https://github.com/KyuDan1/Talk-to-Your-Slides) |
| [PPTArena: A Benchmark for Agentic PowerPoint Editing](https://arxiv.org/abs/2512.03042) | arXiv | 2025 | Benchmark · 100 decks / 2,125 slides; dual-VLM judge; PPTPilot agent | [📄](https://arxiv.org/abs/2512.03042) [💻](https://github.com/michaelofengend/PPTArena) |
| [APEX: Academic Poster Editing Agentic Expert](https://arxiv.org/abs/2601.04794) | arXiv | 2026 | First agentic framework for interactive academic poster editing; multi-level PPTX API + review-adjust; APEX-Bench (514 instructions) | [📄](https://arxiv.org/abs/2601.04794) [💻](https://github.com/Breesiu/APEX) |
| [DECKBench: Benchmarking Multi-Agent Frameworks for Academic Slide Generation and Editing](https://arxiv.org/abs/2602.13318) | arXiv | 2026 | Benchmark covering generation + multi-turn editing; assesses slide/deck fidelity, coherence, layout, instruction following | [📄](https://arxiv.org/abs/2602.13318) |

### Layout Generation

> Models focused on placing and sizing elements (text boxes, images, charts) on a slide or poster canvas.

| Paper | Venue | Year | Paradigm | Links |
|-------|-------|------|----------|-------|
| [PosterLlama: Bridging Design Ability of LM to Content-Aware Layout Generation](https://arxiv.org/abs/2404.00995) | ECCV 2024 | 2024 | LLM · elements serialized as HTML; two-stage VL training | [📄](https://arxiv.org/abs/2404.00995) |
| [PosterLLaVa: A Unified Multi-modal Layout Generator with LLM](https://arxiv.org/abs/2406.02884) | arXiv | 2024 | Multimodal LLM · unified across design domains | [📄](https://arxiv.org/abs/2406.02884) |
| [Relation-Aware Diffusion Model for Controllable Poster Layout Generation](https://arxiv.org/abs/2306.09086) | CIKM 2023 | 2023 | Diffusion · element-relation conditioning | [📄](https://arxiv.org/abs/2306.09086) |
| [ReLayout: Integrating Relation Reasoning for Content-aware Layout Generation with MLLMs](https://arxiv.org/abs/2507.05568) | arXiv | 2025 | MLLM · relation chain-of-thought (region/salient/margin) + prototype rebalance sampler | [📄](https://arxiv.org/abs/2507.05568) |
| [LLMs as Layout Designers: Enhanced Spatial Reasoning for Content-Aware Layout Generation (LaySPA)](https://arxiv.org/abs/2509.16891) | arXiv | 2025 | RL · explicit spatial reasoning with hybrid geometric/structural/visual rewards | [📄](https://arxiv.org/abs/2509.16891) |
| [UniLayDiff: A Unified Diffusion Transformer for Content-Aware Layout Generation](https://arxiv.org/abs/2512.08897) | arXiv | 2025 | Multi-modal diffusion transformer · single model for conditional/unconditional layout | [📄](https://arxiv.org/abs/2512.08897) |
| [iPoster: Content-Aware Layout Generation for Interactive Poster Design via Graph-Enhanced Diffusion Models](https://arxiv.org/abs/2603.29469) | CHI EA 2026 | 2026 | Graph-enhanced diffusion · user-constrained interactive poster layout | [📄](https://arxiv.org/abs/2603.29469) |
| [AeSlides: Incentivizing Aesthetic Layout in LLM-Based Slide Generation via Verifiable Rewards](https://arxiv.org/abs/2604.22840) | arXiv | 2026 | RL (GRPO) · verifiable aesthetic rewards (aspect ratio, whitespace, collisions, balance) | [📄](https://arxiv.org/abs/2604.22840) [💻](https://github.com/ympan0508/aeslides) |
| [SlideCoder: Layout-aware RAG-enhanced Hierarchical Slide Generation from Design](https://arxiv.org/abs/2506.07964) | EMNLP 2025 | 2025 | Image → code · Color Gradient Segmentation + hierarchical RAG for design-to-PPTX code; SlideMaster 7B; Slide2Code benchmark | [📄](https://arxiv.org/abs/2506.07964) [💻](https://github.com/vinsontang1/SlideCoder) |

### Evaluation

> Frameworks and benchmarks designed to assess quality of generated presentations.

| Paper | Venue | Year | What it Measures | Links |
|-------|-------|------|-----------------|-------|
| [PPTEval](https://arxiv.org/abs/2501.03936) | arXiv | 2025 | Content · Design · Coherence (introduced with PPTAgent) | [📄](https://arxiv.org/abs/2501.03936) |
| [REFLEX: Reference-Free Evaluation of Presentation Content](https://arxiv.org/abs/2505.18240) | arXiv | 2025 | Reference-free quality score + actionable feedback; RefSlides benchmark | [📄](https://arxiv.org/abs/2505.18240) |
| [SlideAudit: Automated Evaluation of Presentation Slides](https://arxiv.org/abs/2508.03630) | UIST 2025 | 2025 | Design-flaw taxonomy; 2,400 expert-annotated slides | [📄](https://arxiv.org/abs/2508.03630) |
| [VLM-SlideEval: Evaluating VLMs on Structured Comprehension and Perturbation Sensitivity in PPT](https://arxiv.org/abs/2510.22045) | arXiv | 2025 | Element extraction · perturbation robustness · narrative-order comprehension | [📄](https://arxiv.org/abs/2510.22045) |
| [SlidesGen-Bench: Evaluating Slides Generation via Computational and Quantitative Metrics](https://arxiv.org/abs/2601.09487) | arXiv | 2026 | Content · Aesthetics · Editability (computational metrics + Slides-Align preferences) | [📄](https://arxiv.org/abs/2601.09487) [💻](https://github.com/YunqiaoYang/SlidesGen-Bench) |
| [PresentBench: A Fine-Grained Rubric-Based Benchmark for Slide Generation](https://arxiv.org/abs/2603.07244) | arXiv | 2026 | Instance-specific binary checklists (238 instances, avg. 54.1 items) | [📄](https://arxiv.org/abs/2603.07244) [💻](https://github.com/PresentBench/PresentBench) |
| [PPTBench: Towards Holistic Evaluation of Large Language Models for PowerPoint Layout and Design Understanding](https://arxiv.org/abs/2512.02624) | arXiv | 2025 | 958 PPTX files · 4,439 samples across Detection / Understanding / Modification / Generation; exposes MLLM layout-reasoning gap | [📄](https://arxiv.org/abs/2512.02624) |

---

## Datasets & Benchmarks

| Dataset | Year | Size | Task | Links |
|---------|------|------|------|-------|
| [SlidesBench](https://github.com/para-lost/AutoPresent) | 2025 | 7k train / 585 test · 10 domains | Slide generation | [💻](https://github.com/para-lost/AutoPresent) |
| [PPTC](https://arxiv.org/abs/2311.01767) | 2023 | 279 multi-turn sessions | PPTX task completion (create / edit) | [📄](https://arxiv.org/abs/2311.01767) [💻](https://github.com/gydpku/PPTC) |
| [PPTC-R](https://arxiv.org/abs/2403.03788) | 2024 | PPTC + perturbations | PPTX task robustness | [📄](https://arxiv.org/abs/2403.03788) |
| [SlideVQA](https://arxiv.org/abs/2301.04883) | 2023 | 2.6k decks / 52k images / 14.5k Qs | Slide visual question answering | [📄](https://arxiv.org/abs/2301.04883) [🗂️](https://huggingface.co/datasets/NTT-hil-insight/SlideVQA) |
| [SciDuet](https://gem-benchmark.com/data_cards/SciDuet) | 2021 | ICML'19 + NeurIPS'18&19 + ACL pairs | Document-to-slide retrieval | [🗂️](https://gem-benchmark.com/data_cards/SciDuet) |
| [ArcBench](https://huggingface.co/datasets/ArcDeck/ArcBench) | 2026 | 100 oral paper + slide-deck pairs (ICML/ICLR/NeurIPS/CVPR/ICCV) | Paper-to-slide generation & evaluation | [🗂️](https://huggingface.co/datasets/ArcDeck/ArcBench) [📄](https://arxiv.org/abs/2604.11969) |
| [P2PInstruct / P2PEval](https://github.com/multimodal-art-projection/P2P) | 2025 | 30k+ instructions · 121 paper-poster eval pairs | Paper-to-poster generation & fine-grained eval | [💻](https://github.com/multimodal-art-projection/P2P) [📄](https://arxiv.org/abs/2505.17104) |
| [PosterSum](https://huggingface.co/datasets/rohitsaxena/PosterSum) | 2025 | 16,305 poster images + abstract summaries | Scientific poster understanding / summarization | [🗂️](https://huggingface.co/datasets/rohitsaxena/PosterSum) [💻](https://github.com/saxenarohit/postersum) [📄](https://arxiv.org/abs/2502.17540) |
| [TSBench](https://github.com/KyuDan1/Talk-to-Your-Slides) | 2025 | 379 human-verified edit instructions | Instruction-based slide editing | [💻](https://github.com/KyuDan1/Talk-to-Your-Slides) [📄](https://arxiv.org/abs/2505.11604) |
| [Slide2Code](https://github.com/vinsontang1/SlideCoder) | 2025 | Difficulty-tiered samples (Slide Complexity Metric) | Slide design image → PPTX code generation | [💻](https://github.com/vinsontang1/SlideCoder) [📄](https://arxiv.org/abs/2506.07964) |
| [Paper2Video Benchmark](https://github.com/showlab/Paper2Video) | 2025 | 101 paper–video pairs (avg. 16 slides / 6 min 15 s) | Paper → narrated presentation video | [💻](https://github.com/showlab/Paper2Video) [📄](https://arxiv.org/abs/2510.05096) |
| [APEX-Bench](https://github.com/Breesiu/APEX) | 2026 | 514 academic poster editing instructions (multi-dimensional taxonomy) | Instruction-based poster editing | [💻](https://github.com/Breesiu/APEX) [📄](https://arxiv.org/abs/2601.04794) |

---

## Open-Source Projects

### AI Slide & Poster Generators

| Project | Input | Output | Description | Links |
|---------|-------|--------|-------------|-------|
| [Presenton](https://github.com/presenton/presenton) | Text prompt / doc | PPTX · PDF | Self-hostable AI generator with REST API | [💻](https://github.com/presenton/presenton) |
| [PPTAgent](https://github.com/icip-cas/PPTAgent) | Topic + reference deck | PPTX | Agentic, edit-based generation (ICIP-CAS) | [💻](https://github.com/icip-cas/PPTAgent) |
| [AutoPresent](https://github.com/para-lost/AutoPresent) | Text instruction | HTML / slides | Code-gen model + SlidesBench benchmark | [💻](https://github.com/para-lost/AutoPresent) |
| [Powerpointer-For-Local-LLMs](https://github.com/CyberTimon/Powerpointer-For-Local-LLMs) | Text prompt | PPTX | Local OpenAI-compatible LLM + python-pptx | [💻](https://github.com/CyberTimon/Powerpointer-For-Local-LLMs) |
| [ALLWEONE Presentation AI](https://github.com/allweonedev/presentation-ai) | Prompt + preferences | Editable deck · PPTX | Open-source Gamma alternative for themed AI presentations | [💻](https://github.com/allweonedev/presentation-ai) |
| [Paper2Poster](https://github.com/Paper2Poster/Paper2Poster) | Paper PDF | PPTX poster | NeurIPS 2025 multi-agent paper-to-poster automation | [💻](https://github.com/Paper2Poster/Paper2Poster) [🌐](https://paper2poster.github.io/) |
| [PosterGen](https://github.com/Y-Research-SBU/PosterGen) | Paper PDF + logos | PNG · PPTX poster | Aesthetic-aware multi-agent (LangGraph) paper-to-poster | [💻](https://github.com/Y-Research-SBU/PosterGen) |
| [SlideDeck AI](https://github.com/barun-saha/slide-deck-ai) | Topic / PDF | PPTX | Multi-provider (Gemini/OpenAI/Azure/Anthropic) deck co-creation, with offline Ollama mode | [💻](https://github.com/barun-saha/slide-deck-ai) |

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
| [Genspark AI Slides](https://www.genspark.ai) | Prompt · topic | Export-ready deck | Agentic "Super Agent" handles research, writing, and design end-to-end (2025) |
| [Skywork AI Slides](https://skywork.ai) | Prompt + data/branding | PPTX · Google Slides | Agentic deck builder with data viz and cited, research-backed content (2025) |
| [Manus Slides](https://manus.im) | Prompt · research goal | PPTX | Slide module of the Manus general AI agent; decks from deep research (2025) |
| [Alai](https://getalai.com) | Content · PDF · PPT | Designed deck | YC-backed, control-focused maker with per-slide layout variations (2025) |

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
