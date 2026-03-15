#!/usr/bin/env python3
"""Parse a GitHub Issue body (from the add-paper form) and append an entry to papers.yml."""

import os
import re
import yaml
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "docs" / "_data" / "papers.yml"

CATEGORY_MAP = {
    "core-framework": "core-framework",
    "reinforcement-learning": "reinforcement-learning",
    "security-safety": "security-safety",
    "multi-agent": "multi-agent",
    "benchmark-evaluation": "benchmark-evaluation",
    "memory-architecture": "memory-architecture",
    "skills-tool-use": "skills-tool-use",
    "blog": "blog",
    "project": "project",
}


def parse_issue_body(body: str) -> dict:
    """Extract structured fields from GitHub Issue form body.

    GitHub renders issue form fields as:
    ### Field Label\n\nvalue\n\n### Next Field ...
    """
    sections = re.split(r"###\s+", body)
    fields = {}
    for section in sections:
        section = section.strip()
        if not section:
            continue
        lines = section.split("\n", 1)
        label = lines[0].strip()
        value = lines[1].strip() if len(lines) > 1 else ""
        if value == "_No response_" or not value:
            continue
        fields[label] = value
    return fields


def field(fields: dict, *keys: str) -> str:
    for k in keys:
        if k in fields:
            return fields[k].strip()
    return ""


def main():
    body = os.environ.get("ISSUE_BODY", "")
    if not body:
        print("ERROR: ISSUE_BODY is empty")
        return

    fields = parse_issue_body(body)
    print(f"Parsed fields: {list(fields.keys())}")

    title = field(fields, "Title")
    category = field(fields, "Category")
    description = field(fields, "Brief Description")
    arxiv = field(fields, "arXiv / Paper Link")
    code = field(fields, "Code Repository")
    url = field(fields, "Other Link (project page, blog post, etc.)")
    date = field(fields, "Publication Date")
    tags_raw = field(fields, "Tags (comma-separated)")

    if not title:
        print("ERROR: Title is required")
        return

    tags = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    cat_id = CATEGORY_MAP.get(category, "")

    if cat_id == "blog":
        entry = {"title": title, "description": description}
        if url:
            entry["url"] = url
        elif arxiv:
            entry["url"] = arxiv
        if tags:
            entry["tags"] = tags
        data.setdefault("blog_posts", []).append(entry)
        print(f"Added blog post: {title}")

    elif cat_id == "project":
        entry = {"name": title, "description": description}
        entry["url"] = url or code or arxiv or ""
        data.setdefault("projects", []).append(entry)
        print(f"Added project: {title}")

    else:
        entry = {"title": title, "description": description}
        if date:
            entry["date"] = date
        links = {}
        if arxiv:
            links["arxiv"] = arxiv
        if code:
            links["code"] = code
        if url:
            links["url"] = url
        if not links:
            links["url"] = "TBD"
        entry["links"] = links
        if tags:
            entry["tags"] = tags

        target_cat = None
        for cat in data.get("categories", []):
            if cat["id"] == cat_id:
                target_cat = cat
                break

        if target_cat is None:
            print(f"WARNING: Category '{cat_id}' not found, adding to first category")
            target_cat = data["categories"][0]

        target_cat.setdefault("papers", []).append(entry)
        print(f"Added paper to '{target_cat['name']}': {title}")

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)

    print("papers.yml updated successfully")


if __name__ == "__main__":
    main()
