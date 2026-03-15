#!/usr/bin/env python3
"""Validate the structure of docs/_data/papers.yml."""

import sys
import yaml
from pathlib import Path


def validate():
    data_path = Path(__file__).parent.parent / "docs" / "_data" / "papers.yml"
    if not data_path.exists():
        print(f"ERROR: {data_path} not found")
        return False

    with open(data_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    errors = []

    if "categories" not in data:
        errors.append("Missing top-level 'categories' key")
    else:
        seen_ids = set()
        for i, cat in enumerate(data["categories"]):
            prefix = f"categories[{i}]"
            if "id" not in cat:
                errors.append(f"{prefix}: missing 'id'")
            elif cat["id"] in seen_ids:
                errors.append(f"{prefix}: duplicate id '{cat['id']}'")
            else:
                seen_ids.add(cat["id"])

            if "name" not in cat:
                errors.append(f"{prefix}: missing 'name'")

            for j, paper in enumerate(cat.get("papers", [])):
                p = f"{prefix}.papers[{j}]"
                if "title" not in paper:
                    errors.append(f"{p}: missing 'title'")
                if "description" not in paper:
                    errors.append(f"{p}: missing 'description'")
                if "links" not in paper:
                    errors.append(f"{p}: missing 'links'")
                elif not isinstance(paper["links"], dict) or len(paper["links"]) == 0:
                    errors.append(f"{p}: 'links' must have at least one entry")

    for i, post in enumerate(data.get("blog_posts", [])):
        prefix = f"blog_posts[{i}]"
        if "title" not in post:
            errors.append(f"{prefix}: missing 'title'")
        if "url" not in post:
            errors.append(f"{prefix}: missing 'url'")

    for i, proj in enumerate(data.get("projects", [])):
        prefix = f"projects[{i}]"
        if "name" not in proj:
            errors.append(f"{prefix}: missing 'name'")
        if "url" not in proj:
            errors.append(f"{prefix}: missing 'url'")

    if errors:
        print(f"VALIDATION FAILED — {len(errors)} error(s):\n")
        for e in errors:
            print(f"  ✗ {e}")
        return False

    total = sum(len(c.get("papers", [])) for c in data["categories"])
    blogs = len(data.get("blog_posts", []))
    projects = len(data.get("projects", []))
    print(f"VALIDATION PASSED ✓")
    print(f"  {total} papers across {len(data['categories'])} categories")
    print(f"  {blogs} blog posts, {projects} projects")
    return True


if __name__ == "__main__":
    sys.exit(0 if validate() else 1)
