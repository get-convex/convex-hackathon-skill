#!/usr/bin/env python3
"""Run dependency-free checks for the publishable skill package."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse the skill's two simple YAML string fields."""
    if not text.startswith("---\n"):
        raise AssertionError("SKILL.md must start with YAML frontmatter")

    marker = text.find("\n---\n", 4)
    if marker == -1:
        raise AssertionError("SKILL.md frontmatter is not closed")

    values: dict[str, str] = {}
    for line in text[4:marker].splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            raise AssertionError(f"Invalid frontmatter line: {line}")
        values[key.strip()] = value.strip()
    return values


def check_relative_links(path: Path) -> None:
    """Ensure relative Markdown links resolve inside the package."""
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        resolved = (path.parent / target.split("#", 1)[0]).resolve()
        assert resolved.exists(), f"Broken link in {path.name}: {target}"


def main() -> None:
    """Validate the package structure and core behavior instructions."""
    text = SKILL.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)

    assert set(frontmatter) == {"name", "description"}
    assert frontmatter["name"] == "convex-hackathon-skill"
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", frontmatter["name"])
    assert len(text.splitlines()) < 500

    required_phrases = (
        "references/log-format.md",
        "leave the file unchanged",
        "Never open or dump `.env`",
        "Never create a Git commit",
        "Without Git",
        "working tree",
    )
    for phrase in required_phrases:
        assert phrase in text, f"Missing required instruction: {phrase}"

    for package_file in (
        ROOT / "agents" / "openai.yaml",
        ROOT / "references" / "log-format.md",
        ROOT / "README.md",
    ):
        assert package_file.is_file(), f"Missing package file: {package_file}"

    # ChatGPT Sites URLs end in .chatgpt.site; codex.site does not exist.
    log_format = (ROOT / "references" / "log-format.md").read_text(encoding="utf-8")
    assert "*.chatgpt.site" in log_format, "Live app rule must accept *.chatgpt.site"
    assert "codex.site" not in log_format, "codex.site is not a real URL suffix"

    for markdown_file in ROOT.rglob("*.md"):
        # Skip hidden folders such as .git and .cursor; they are not package files.
        if any(part.startswith(".") for part in markdown_file.relative_to(ROOT).parts[:-1]):
            continue
        check_relative_links(markdown_file)
        contents = markdown_file.read_text(encoding="utf-8")
        assert "TODO" not in contents, f"Unresolved TODO in {markdown_file}"

    print("Package validation passed")


if __name__ == "__main__":
    main()
