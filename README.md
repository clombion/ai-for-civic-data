# AI for Civic Data

A case study library for civil society data practitioners — showing how to use
AI to work faster without losing control of your analysis.

**Live site:** https://[your-org].github.io/ai-for-civic-data/

---

## How it works

The site is a single HTML file built from YAML content files by a small Python
script. On every push to `main`, a GitHub Action rebuilds `index.html` and
deploys it to GitHub Pages.

```
_cases/          ← one YAML file per case study
_glossary.yaml   ← glossary terms
template.html    ← HTML/CSS/JS with {{CASES_JSON}} and {{GLOSSARY_JSON}} placeholders
build.py         ← reads YAML, injects JSON into template, writes index.html
```

## Adding a case study

Create a new file in `_cases/` named `your-case-id.yaml`. The filename
determines the sort order (alphabetical), so prefix with a number if order
matters: `01-summarise-policy.yaml`.

Required fields:

```yaml
id: your-case-id           # must match filename (without .yaml)
title: "Your Case Title"
shortDesc: "One sentence shown on the card."
context: >
  Two or three sentences explaining the situation and the key question.
  Use > for multi-line prose to avoid YAML quoting issues.
mode: prompt-guided        # or: pipeline
pipelineTags: [analyse, present]   # any of: define find get verify clean analyse present
topicTags: [policy, documents]
material: "policy documents"       # shown in the madlib filter sentence
hasSkill: false            # true if a skill file is available

risks:
  - risk:
      title: "What goes wrong"
      body: "Description of the failure mode."
    good:
      title: "What the principles change"
      body: "How applying the principles addresses this."

principles:
  - name: Objective         # must be one of the 5 principle names
    tag: "Subtitle shown under the name"
    body: >
      Explanation of how to apply this principle to this specific task.
    ex1:
      lbl: "Example label"
      txt: "Example content shown in the code-style box."
    # ex2, warn are optional
    warn: "Warning text shown in red."

prompt: |
  Your prompt template here.
  Use [PLACEHOLDER] for slots the user fills in.
```

Commit and push to `main` — the site rebuilds automatically within ~30 seconds.

## Editing the glossary

Edit `_glossary.yaml`. Each entry:

```yaml
- term: Term name
  def: "Definition text."
  related: [Other term, Another term]   # optional
  tags: [principle]                     # principle | pipeline | artifact | tool | methodology
  link:                                 # optional
    url: https://example.com
    label: "Link text →"
```

## Local development

```bash
pip install pyyaml
python build.py
open index.html
```

## Deployment

GitHub Pages is configured to serve from the `gh-pages` branch. The GitHub
Action in `.github/workflows/build.yml` handles this automatically on every
push to `main`.

To set up on a new repo:
1. Push this repo to GitHub
2. Go to Settings → Pages → Source → Deploy from branch → `gh-pages`
3. Push any change to `main` to trigger the first build

## Prompt conventions

In prompt templates:
- `[PLACEHOLDER]` — something the user must fill in before use
- Lines starting with `#` — section headers (rendered in grey)

The build script passes prompt text through as-is, so standard YAML block
scalar (`|`) preserves line breaks correctly.
