"""Tests for c2004 SPA route → source file resolution."""
from __future__ import annotations

from pathlib import Path

import pytest

from rebuild.analysis.c2004_route_resolver import (
    extract_module_from_page_slug,
    resolve_c2004_route,
    route_slug,
)


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("/connect-test-customers", "connect-test-customers"),
        ("/connect-template2?theme=dark", "connect-template2"),
    ],
)
def test_route_slug(path: str, expected: str) -> None:
    assert route_slug(path) == expected


@pytest.mark.parametrize(
    ("slug", "module"),
    [
        ("connect-test-customers", "connect-test"),
        ("connect-test-device-types", "connect-test-device"),
        ("connect-template2", "connect-template2"),
    ],
)
def test_extract_module_from_page_slug(slug: str, module: str) -> None:
    assert extract_module_from_page_slug(slug) == module


def test_resolve_connect_test_customers_finds_wrapper_and_impl() -> None:
    repo = Path("/home/tom/github/maskservice/c2004")
    if not repo.exists():
        pytest.skip("c2004 repo not available")

    resolution = resolve_c2004_route(repo, "/connect-test-customers")
    assert resolution.module == "connect-test"
    assert any(p.name == "customers.page.ts" for p in resolution.page_implementations)
    assert any(p.name == "connect-test.view.ts" for p in resolution.module_files)


def test_resolve_connect_menu_editor_finds_wrapper() -> None:
    repo = Path("/home/tom/github/maskservice/c2004")
    if not repo.exists():
        pytest.skip("c2004 repo not available")

    resolution = resolve_c2004_route(repo, "/connect-menu-editor")
    assert resolution.module == "connect-menu-editor"
    assert any(p.name == "connect-menu-editor.page.ts" for p in resolution.page_wrappers)


def test_resolve_connect_template2_finds_module_view() -> None:
    repo = Path("/home/tom/github/maskservice/c2004")
    if not repo.exists():
        pytest.skip("c2004 repo not available")

    resolution = resolve_c2004_route(repo, "/connect-template2")
    assert resolution.module == "connect-template2"
    assert any(p.name == "connect-template2.view.ts" for p in resolution.module_files)


def test_resolve_connect_test_device_types() -> None:
    repo = Path("/home/tom/github/maskservice/c2004")
    if not repo.exists():
        pytest.skip("c2004 repo not available")

    resolution = resolve_c2004_route(repo, "/connect-test-device-types")
    assert resolution.module == "connect-test-device"
    assert any(p.name == "device-types.page.ts" for p in resolution.page_implementations)
