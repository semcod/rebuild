#!/usr/bin/env python3
"""
Semantic version bump script for rebuild.

Usage:
    python scripts/bump_version.py patch   # 0.1.19 -> 0.1.20
    python scripts/bump_version.py minor   # 0.1.19 -> 0.2.0
    python scripts/bump_version.py major   # 0.1.19 -> 1.0.0
    python scripts/bump_version.py --show  # print current version

The script:
1. Reads current version from rebuild/__init__.py
2. Bumps according to semver (major/minor/patch)
3. Updates rebuild/__init__.py and pyproject.toml
4. Prepends a new section in CHANGELOG.md under [Unreleased]
5. Prints a summary of changes made (dry-run safe: use --dry-run)
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
INIT_FILE = ROOT / "rebuild" / "__init__.py"
PYPROJECT = ROOT / "pyproject.toml"
CHANGELOG = ROOT / "CHANGELOG.md"
VERSION_FILE = ROOT / "VERSION"


def read_version() -> str:
    text = INIT_FILE.read_text()
    m = re.search(r'__version__\s*=\s*["\'](.+?)["\']', text)
    if not m:
        raise ValueError("Could not find __version__ in rebuild/__init__.py")
    return m.group(1)


def bump(version: str, part: str) -> str:
    parts = version.split(".")
    if len(parts) != 3:
        raise ValueError(f"Expected MAJOR.MINOR.PATCH, got: {version!r}")
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    if part == "major":
        return f"{major + 1}.0.0"
    elif part == "minor":
        return f"{major}.{minor + 1}.0"
    elif part == "patch":
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError(f"Unknown bump part: {part!r}. Use major|minor|patch")


def update_init(new_version: str, dry_run: bool) -> None:
    text = INIT_FILE.read_text()
    updated = re.sub(
        r'(__version__\s*=\s*["\'])(.+?)(["\'])',
        lambda m: f"{m.group(1)}{new_version}{m.group(3)}",
        text,
    )
    if not dry_run:
        INIT_FILE.write_text(updated)
    print(f"  {'[dry-run] ' if dry_run else ''}rebuild/__init__.py  → __version__ = {new_version!r}")


def update_pyproject(new_version: str, dry_run: bool) -> None:
    text = PYPROJECT.read_text()
    updated = re.sub(
        r'(^\s*version\s*=\s*["\'])([^"\']+)(["\'])',
        lambda m: f"{m.group(1)}{new_version}{m.group(3)}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if not dry_run:
        PYPROJECT.write_text(updated)
    print(f"  {'[dry-run] ' if dry_run else ''}pyproject.toml       → version = {new_version!r}")


def update_version_file(new_version: str, dry_run: bool) -> None:
    if not dry_run:
        VERSION_FILE.write_text(f"{new_version}\n", encoding="utf-8")
    print(f"  {'[dry-run] ' if dry_run else ''}VERSION              → {new_version!r}")


def collect_unreleased_entries() -> list[str]:
    """Collect lines between [Unreleased] and the next ## [ section."""
    text = CHANGELOG.read_text()
    lines = text.splitlines()
    in_unreleased = False
    entries: list[str] = []
    for line in lines:
        if re.match(r"^##\s*\[Unreleased\]", line, re.IGNORECASE):
            in_unreleased = True
            continue
        if in_unreleased and re.match(r"^##\s*\[", line):
            break
        if in_unreleased and line.strip():
            entries.append(line)
    return entries


def get_git_log_since_last_tag() -> list[str]:
    """Return one-line git log entries since the last tag."""
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "describe", "--tags", "--abbrev=0"],
            capture_output=True, text=True, check=False,
        )
        last_tag = result.stdout.strip() if result.returncode == 0 else ""
        range_arg = f"{last_tag}..HEAD" if last_tag else "HEAD"
        log = subprocess.run(
            ["git", "-C", str(ROOT), "log", range_arg, "--oneline", "--no-merges"],
            capture_output=True, text=True, check=False,
        )
        if log.returncode == 0:
            return [line for line in log.stdout.splitlines() if line.strip()]
    except Exception:
        pass
    return []


def categorize_commits(commits: list[str]) -> dict[str, list[str]]:
    categories: dict[str, list[str]] = {
        "Added": [],
        "Changed": [],
        "Fixed": [],
        "Test": [],
        "Docs": [],
        "Other": [],
    }
    for line in commits:
        msg = re.sub(r"^[0-9a-f]{7,}\s+", "", line).strip()
        lower = msg.lower()
        if any(k in lower for k in ("add ", "feat", "implement", "new ")):
            categories["Added"].append(msg)
        elif any(k in lower for k in ("fix", "bug", "error", "patch")):
            categories["Fixed"].append(msg)
        elif any(k in lower for k in ("test", "coverage", "spec")):
            categories["Test"].append(msg)
        elif any(k in lower for k in ("doc", "readme", "changelog")):
            categories["Docs"].append(msg)
        elif any(k in lower for k in ("refactor", "change", "update", "improve", "bump")):
            categories["Changed"].append(msg)
        else:
            categories["Other"].append(msg)
    return {k: v for k, v in categories.items() if v}


def build_new_section(new_version: str, commits: list[str], unreleased: list[str]) -> str:
    today = date.today().isoformat()
    lines = [f"## [{new_version}] - {today}", ""]
    categories = categorize_commits(commits)

    if unreleased:
        lines.append("### Unreleased")
        for entry in unreleased:
            lines.append(entry)
        lines.append("")

    for cat, items in categories.items():
        lines.append(f"### {cat}")
        for item in items:
            lines.append(f"- {item}")
        lines.append("")

    if not unreleased and not categories:
        lines.append("### Changed")
        lines.append(f"- Version bump to {new_version}")
        lines.append("")

    return "\n".join(lines)


def update_changelog(new_version: str, dry_run: bool) -> None:
    commits = get_git_log_since_last_tag()
    unreleased = collect_unreleased_entries()
    new_section = build_new_section(new_version, commits, unreleased)

    text = CHANGELOG.read_text()
    # Insert new section after [Unreleased] block
    unreleased_pattern = re.compile(
        r"(##\s*\[Unreleased\][^\n]*\n)(.*?)(##\s*\[)",
        re.DOTALL,
    )
    if unreleased_pattern.search(text):
        updated = unreleased_pattern.sub(
            lambda m: f"{m.group(1)}\n{new_section}\n{m.group(3)}",
            text,
            count=1,
        )
    else:
        updated = text + f"\n{new_section}\n"

    # Add link references at the bottom
    repo_url = "https://github.com/semcod/resplit"
    current_version = read_version()
    link_line = f"[{new_version}]: {repo_url}/compare/v{current_version}...v{new_version}\n"
    if link_line.strip() not in updated:
        updated += link_line

    if not dry_run:
        CHANGELOG.write_text(updated)
    print(f"  {'[dry-run] ' if dry_run else ''}CHANGELOG.md         → added [{new_version}] section ({len(commits)} commits)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic version bump for rebuild")
    parser.add_argument("part", nargs="?", choices=["major", "minor", "patch"],
                        help="Which part of semver to bump")
    parser.add_argument("--show", action="store_true", help="Print current version and exit")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change, don't write")
    args = parser.parse_args()

    current = read_version()

    if args.show:
        print(f"rebuild v{current}")
        return

    if not args.part:
        parser.error("Specify bump part: major | minor | patch")

    new_version = bump(current, args.part)
    print(f"\nBumping rebuild {current} → {new_version} ({args.part})\n")

    update_init(new_version, args.dry_run)
    update_pyproject(new_version, args.dry_run)
    update_version_file(new_version, args.dry_run)
    update_changelog(new_version, args.dry_run)

    if not args.dry_run:
        print(f"\n✓ Version bumped to {new_version}")
        print("  Next steps:")
        print("    git add rebuild/__init__.py pyproject.toml CHANGELOG.md VERSION")
        print(f"    git commit -m 'chore: bump version to {new_version}'")
        print(f"    git tag v{new_version}")
        print("    git push && git push --tags")
    else:
        print(f"\n[dry-run] No files modified. Would bump to {new_version}")


if __name__ == "__main__":
    main()
