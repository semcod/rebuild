"""RestoreService integration with c2004 route resolver."""
from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from rebuild.application.services.restore_service import RestoreService


def test_find_route_files_connect_test_customers() -> None:
    repo = Path("/home/tom/github/maskservice/c2004")
    if not repo.exists():
        pytest.skip("c2004 repo not available")

    svc = RestoreService(repo)
    files = svc._find_route_files("/connect-test-customers")
    assert files
    assert any("customers.page.ts" in str(f) for f in files)


def test_find_route_files_api_returns_empty() -> None:
    repo = Path("/home/tom/github/maskservice/c2004")
    if not repo.exists():
        pytest.skip("c2004 repo not available")

    svc = RestoreService(repo)
    assert svc._find_route_files("/api/v3/health") == []


def test_extract_endpoint_copies_route_files(tmp_path: Path) -> None:
    repo = Path("/home/tom/github/maskservice/c2004")
    if not repo.exists():
        pytest.skip("c2004 repo not available")

    svc = RestoreService(repo)
    target = tmp_path / "out"
    svc.extract_endpoint("/connect-test-customers", date(2025, 1, 1), target)
    copied = list(target.rglob("customers.page.ts"))
    assert copied, "expected customers.page.ts in restored output"
