from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
INDEX_FILE = POSTS_DIR / "index.json"
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}

    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        data[key.strip()] = value
    return data


def build_posts_index() -> list[dict[str, str]]:
    posts: list[dict[str, str]] = []

    for post_file in sorted(POSTS_DIR.glob("*.md")):
        frontmatter = parse_frontmatter(post_file.read_text(encoding="utf-8"))
        posts.append(
            {
                "slug": post_file.stem,
                "title": frontmatter.get("title", post_file.stem.replace("-", " ").title()),
                "category": frontmatter.get("category", ""),
                "date": frontmatter.get("date", ""),
                "excerpt": frontmatter.get("excerpt", ""),
            }
        )

    posts.sort(key=lambda post: post.get("date", ""), reverse=True)
    return posts


def main() -> None:
    posts = build_posts_index()
    INDEX_FILE.write_text(
        json.dumps(posts, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
