#!/usr/bin/env python3
"""Generate README.md from docs/_data/papers.yml.

Keeps the data file as the single source of truth — run this script
after editing papers.yml to regenerate the README automatically.

Usage:
    python scripts/generate_readme.py
"""

import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_PATH = ROOT / "docs" / "_data" / "papers.yml"
README_PATH = ROOT / "README.md"


def link_badges(links: dict) -> str:
    parts = []
    if links.get("arxiv"):
        parts.append(f"[[arXiv]]({links['arxiv']})")
    if links.get("pdf"):
        parts.append(f"[[PDF]]({links['pdf']})")
    if links.get("code"):
        parts.append(f"[[Code]]({links['code']})")
    if links.get("project"):
        parts.append(f"[[Project]]({links['project']})")
    if links.get("url"):
        parts.append(f"[[Link]]({links['url']})")
    return " ".join(parts)


def generate():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    lines = []
    w = lines.append

    w("# Awesome OpenClaw Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    w("")
    w("> A curated list of academic papers, technical reports, and research related to [OpenClaw](https://github.com/openclaw/openclaw) — the open-source, self-hosted AI assistant platform.")
    w("")
    w("OpenClaw is an open-source personal AI agent that runs on your own devices and connects to 50+ messaging platforms. It supports multiple LLM backends (Claude, GPT, Gemini, local models), features a modular skill system with 5,700+ community-maintained skills, and implements advanced memory architecture for persistent context.")
    w("")
    w("This repository tracks the latest academic research around OpenClaw to promote community development and facilitate knowledge sharing.")
    w("")
    w("**🌐 [Browse the interactive website →](https://openclaw.github.io/awesome-openclaw-papers/)**")
    w("")
    w("---")
    w("")

    # Table of contents
    w("## Contents")
    w("")
    for cat in data["categories"]:
        anchor = cat["name"].lower().replace(" ", "-").replace("&", "").replace("  ", "-")
        w(f"- [{cat['name']}](#{anchor})")
    w("- [Blog Posts & Technical Articles](#blog-posts--technical-articles)")
    w("- [Related Projects](#related-projects)")
    w("")
    w("---")
    w("")

    # Categories
    for cat in data["categories"]:
        w(f"## {cat['icon']} {cat['name']}")
        w("")
        for paper in cat.get("papers", []):
            desc = paper["description"].strip().replace("\n", " ")
            date_str = ""
            if paper.get("date"):
                date_str = f" *({paper['date']})*"
            badges = link_badges(paper.get("links", {}))
            w(f"- **{paper['title']}**{date_str} — {desc} {badges}")
            w("")

    # Blog posts
    w("## 📝 Blog Posts & Technical Articles")
    w("")
    for post in data.get("blog_posts", []):
        w(f"- [{post['title']}]({post['url']}) — {post['description']}")
    w("")

    # Projects
    w("## 📦 Related Projects")
    w("")
    w("| Project | Description | Link |")
    w("|---------|-------------|------|")
    for proj in data.get("projects", []):
        w(f"| {proj['name']} | {proj['description']} | [GitHub]({proj['url']}) |")
    w("")
    w("---")
    w("")

    # Footer
    w("## Contributing")
    w("")
    w("Contributions are welcome! The easiest way to add a paper:")
    w("")
    w("1. Edit [`docs/_data/papers.yml`](docs/_data/papers.yml) — the single source of truth")
    w("2. Submit a Pull Request")
    w("3. The website auto-rebuilds on merge")
    w("")
    w("See the [Contributing Guidelines](CONTRIBUTING.md) for details, or [submit via Issue](../../issues/new?template=add-paper.yml).")
    w("")
    w("## License")
    w("")
    w("[CC0 1.0 Universal](LICENSE)")
    w("")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"README.md generated ({len(lines)} lines)")


if __name__ == "__main__":
    generate()
