"""Test to strictly enforce version parity across all carriers and package code."""

from __future__ import annotations

import re
from pathlib import Path

import rebuild


def test_package_version_is_valid_semver():
    """__version__ must be a valid semver string and not 'unknown'."""
    assert rebuild.__version__ != "unknown"
    assert re.match(r"^\d+\.\d+\.\d+", rebuild.__version__), f"Invalid version format: {rebuild.__version__}"


def test_version_carrier_parity():
    """VERSION file, pyproject.toml, and rebuild.__version__ must match strictly."""
    root = Path(__file__).resolve().parent.parent
    version_file = root / "VERSION"
    assert version_file.is_file(), "VERSION file is missing"
    expected_version = version_file.read_text(encoding="utf-8").strip()

    # 1. Check rebuild.__version__
    assert rebuild.__version__ == expected_version, (
        f"rebuild.__version__ ({rebuild.__version__}) does not match VERSION ({expected_version})"
    )

    # 2. Check pyproject.toml
    pyproject_file = root / "pyproject.toml"
    assert pyproject_file.is_file(), "pyproject.toml is missing"
    pyproject_text = pyproject_file.read_text(encoding="utf-8")
    match = re.search(r'(?m)^version\s*=\s*["\']([^"\']+)["\']', pyproject_text)
    assert match, "version not declared in pyproject.toml"
    pyproject_version = match.group(1)
    assert pyproject_version == expected_version, (
        f"pyproject.toml version ({pyproject_version}) does not match VERSION ({expected_version})"
    )
