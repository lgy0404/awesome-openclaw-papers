# Contributing

Thanks for helping grow the OpenClaw research community!

## How It Works

```
Submit Issue / Edit YAML  →  PR Created  →  Merge  →  Website Auto-Rebuilds
```

All content lives in one file: [`docs/_data/papers.yml`](docs/_data/papers.yml).
The website is generated automatically from this file via GitHub Pages.

## Option A: Submit via Issue (Easiest)

1. Go to [New Issue → Add Paper / Resource](../../issues/new?template=add-paper.yml)
2. Fill out the form
3. A PR is **automatically created** from your submission
4. Once a maintainer approves and merges, the website updates instantly

No git knowledge required.

## Option B: Edit the Data File Directly

1. Fork this repository
2. Edit `docs/_data/papers.yml`
3. Add your entry (see format below)
4. Submit a Pull Request

### Adding a Paper

Find the right category and append your entry:

```yaml
- title: "Your Paper Title"
  description: >
    Brief summary of the paper's contribution.
  date: "2026-03"
  links:
    arxiv: https://arxiv.org/abs/XXXX.XXXXX
    code: https://github.com/...
  tags: [keyword1, keyword2]
```

**Required:** `title`, `description`, at least one link.
**Optional:** `date`, `tags`, `authors`, multiple link types (`arxiv`, `pdf`, `code`, `project`, `url`).

### Adding a Blog Post

```yaml
blog_posts:
  - title: "Article Title"
    description: Brief description.
    url: https://example.com/article
    tags: [topic1, topic2]
```

### Adding a Project

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
    name: "Category Name"
    icon: "🔬"
    description: Brief description
    papers: []
```

The website automatically picks up new categories.

## Validation

A CI check validates your YAML on every PR. To validate locally:

```bash
pip install pyyaml
python scripts/validate_papers.py
```

## Quality Checklist

- [ ] Directly related to OpenClaw or its ecosystem
- [ ] Description is 1-2 sentences, focused on the contribution
- [ ] At least one working link provided
- [ ] Placed in the correct category
- [ ] No duplicate entries
