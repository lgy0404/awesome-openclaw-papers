# Contributing to Awesome OpenClaw Papers

Thank you for your interest in contributing! This project uses a **data-driven architecture** — all content lives in a single YAML file, and the website + README are generated automatically.

## Quick Start (3 Steps)

1. **Fork** this repository
2. **Edit** [`docs/_data/papers.yml`](docs/_data/papers.yml) — the single source of truth
3. **Submit** a Pull Request — the website auto-rebuilds on merge

That's it! No need to touch HTML, CSS, or README.md.

## Data File Format

All entries live in `docs/_data/papers.yml`. Here's how to add each type:

### Adding a Paper

Add your entry under the matching category's `papers` list:

```yaml
- title: "Your Paper Title"
  authors: "Author A, Author B"     # optional
  description: >
    A 1-2 sentence summary of the paper's
    key contribution.
  date: "2026-03"                    # optional, YYYY-MM
  links:
    arxiv: https://arxiv.org/abs/XXXX.XXXXX
    pdf: https://example.com/paper.pdf   # optional
    code: https://github.com/...         # optional
    project: https://example.com         # optional
  tags: [security, agent, benchmark]     # optional
```

**Required fields:** `title`, `description`, at least one entry in `links`

### Adding a Blog Post

```yaml
blog_posts:
  - title: "Your Article Title"
    description: Brief description of the article.
    url: https://example.com/article
    tags: [architecture, tutorial]
```

### Adding a Related Project

```yaml
projects:
  - name: ProjectName
    description: What the project does
    url: https://github.com/org/repo
```

### Adding a New Category

```yaml
categories:
  - id: your-category-id
    name: "Your Category Name"
    icon: "🔬"
    description: Brief description of this category
    papers:
      - title: "First Paper"
        description: >
          Description here.
        links:
          arxiv: https://arxiv.org/abs/XXXX.XXXXX
```

The website and filter buttons will automatically pick up new categories.

## Regenerating README.md

The README is auto-generated from the YAML data. After editing `papers.yml`:

```bash
python3 scripts/generate_readme.py
```

## Validating Your Changes

A CI check runs automatically on PRs. To validate locally:

```bash
python3 scripts/validate_papers.py
```

## Local Preview

To preview the website locally:

```bash
cd docs
bundle install
bundle exec jekyll serve
# Open http://localhost:4000
```

## Quality Checklist

- [ ] Paper is directly related to OpenClaw or its ecosystem
- [ ] Description is concise (1-2 sentences) and focuses on the contribution
- [ ] At least one working link is provided
- [ ] Entry is placed in the correct category
- [ ] YAML syntax is valid
- [ ] No duplicate entries

## Don't Want to Edit YAML?

[Submit a paper via GitHub Issue](../../issues/new?template=add-paper.yml) and a maintainer will add it for you.

## Code of Conduct

Please be respectful and constructive. We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).
