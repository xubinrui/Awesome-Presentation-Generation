# Contributing

Thank you for helping make **Awesome Presentation Generation** better! 🎉

Please ensure your pull request adheres to the following guidelines.

## What to add

We welcome additions that are clearly related to **automatic presentation, slide, or poster generation**, including:

- Research papers (with a venue/year and a link to the paper)
- Datasets and benchmarks
- Open-source projects and libraries
- Commercial products with a meaningful AI generation capability
- Surveys, blog posts, and tutorials of lasting value

## Quality bar

- **Search the list first** — make sure the entry does not already exist and isn't a duplicate of an existing one.
- Add **one item per pull request** when possible; it makes review easier.
- The item should be **awesome** — well-known, well-maintained, or genuinely novel. Brand-new repos with little traction may be asked to wait.
- Check your spelling and grammar.

## Formatting

- Place the entry in the **most appropriate section**, in a sensible order (papers are roughly chronological/topical; tools are by relevance). The [taxonomy guide](docs/taxonomy.md) explains what each section covers.
- Use the established **table format** for the section. For papers:

  ```markdown
  | [Title](paper-url) | Venue | Year | One-line paradigm/contribution | [📄](paper-url) [💻](code-url) [🗂️](dataset-url) |
  ```

- Descriptions should be **concise, neutral, and informative** — no marketing language.
- Use `https` links and make sure they resolve. CI runs a [link checker](.github/workflows/link-check.yml) and a [format checker](scripts/check_list.py) on every PR; you can run the latter locally with `python3 scripts/check_list.py`.
- Update the [Contents](README.md#contents) table if you add a new section.

## Submitting

1. Fork the repository and create a branch.
2. Make your change.
3. Open a pull request with a clear title (e.g. `Add PaperX to LLM & Agent-Based Slide Generation`) and a short note on why the item belongs here.

If you're unsure whether something fits, open an issue and ask — we're happy to help.
