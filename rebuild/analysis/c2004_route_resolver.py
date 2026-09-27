from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

_IGNORED_PARTS = frozenset(
    {
        "node_modules",
        ".venv",
        "venv",
        "__pycache__",
        ".git",
        "dist",
        "archive",
        ".rebuild",
        "code2llm_output",
    }
)

# Mirrors frontend/src/registry/page.registry.ts PAGE_MODULE_OVERRIDES
_PAGE_MODULE_OVERRIDES: dict[str, str] = {
    "connect-menu-valid": "connect-menu-editor",
    "connect-role-permissions": "connect-config",
    "connect-template-json": "connect-config",
    "connect-test-device-types": "connect-test-device",
    "connect-test-device-testing": "connect-test-device",
    "hardware-status": "connect-devtools",
}

# Longest-prefix module ids in c2004 monorepo (multi-segment names).
_KNOWN_CONNECT_MODULES: tuple[str, ...] = (
    "connect-live-protocol",
    "connect-test-protocol",
    "connect-test-device",
    "connect-menu-editor",
    "connect-menu-tree",
    "connect-template2",
    "connect-workshop",
    "connect-scenario",
    "connect-template",
    "connect-manager",
    "connect-reports",
    "connect-devtools",
    "connect-config",
    "connect-router",
    "connect-encoder",
    "connect-data",
    "connect-test",
    "connect-id",
)

_RE_EXPORT = re.compile(
    r"""export\s+\*\s+from\s+['"](?P<target>[^'"]+)['"]\s*;""",
    re.MULTILINE,
)


@dataclass
class C2004RouteResolution:
    route: str
    slug: str
    module: str
    page_wrappers: list[Path] = field(default_factory=list)
    page_implementations: list[Path] = field(default_factory=list)
    module_files: list[Path] = field(default_factory=list)
    registry_files: list[Path] = field(default_factory=list)

    @property
    def all_files(self) -> list[Path]:
        ordered: list[Path] = []
        for group in (
            self.page_wrappers,
            self.page_implementations,
            self.module_files,
            self.registry_files,
        ):
            for path in group:
                if path not in ordered:
                    ordered.append(path)
        return ordered

    @property
    def package_roots(self) -> list[Path]:
        roots: list[Path] = []
        for path in self.all_files:
            root = _package_root(path)
            if root and root not in roots:
                roots.append(root)
        return roots


def route_slug(endpoint_path: str) -> str:
    return endpoint_path.strip("/").split("?")[0].split("#")[0]


def extract_module_from_page_slug(slug: str) -> str:
    if slug in _PAGE_MODULE_OVERRIDES:
        return _PAGE_MODULE_OVERRIDES[slug]

    for module in _KNOWN_CONNECT_MODULES:
        if slug == module or slug.startswith(f"{module}-"):
            return module

    parts = slug.split("-")
    if len(parts) >= 2 and parts[0] == "connect":
        return f"{parts[0]}-{parts[1]}"
    return parts[0] if parts else slug


def resolve_c2004_route(repo_path: Path, endpoint_path: str) -> C2004RouteResolution:
    """Map a c2004 SPA route (flat or module base) to source files."""
    repo_path = repo_path.resolve()
    slug = route_slug(endpoint_path)
    module = extract_module_from_page_slug(slug)
    resolution = C2004RouteResolution(route=endpoint_path, slug=slug, module=module)

    page_name = f"{slug}.page.ts"
    for wrapper in _search_files(repo_path, page_name):
        resolution.page_wrappers.append(wrapper)
        impl = _resolve_ts_reexport(repo_path, wrapper)
        if impl:
            resolution.page_implementations.append(impl)

    if not resolution.page_implementations:
        for suffix in _page_suffixes(slug, module):
            for impl in _search_files(repo_path, f"{suffix}.page.ts"):
                if _belongs_to_module(impl, module):
                    resolution.page_implementations.append(impl)

    resolution.module_files.extend(_module_shell_files(repo_path, module))
    resolution.registry_files.extend(_registry_files(repo_path, slug, module))
    return resolution


def _page_suffixes(slug: str, module: str) -> list[str]:
    candidates: list[str] = []
    prefix = f"{module}-"
    if slug.startswith(prefix):
        candidates.append(slug[len(prefix) :])
    if slug.startswith("connect-test-"):
        candidates.append(slug[len("connect-test-") :])
    # de-dupe while preserving order
    seen: set[str] = set()
    out: list[str] = []
    for item in candidates:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def _search_module_pages(repo_path: Path, module: str) -> list[Path]:
    pages: list[Path] = []
    for base in _module_search_roots(repo_path, module):
        pages_dir = base / "pages"
        if pages_dir.is_dir():
            pages.extend(sorted(pages_dir.glob("*.page.ts")))
    return pages


def _belongs_to_module(path: Path, module: str) -> bool:
    parts = path.parts
    return module in parts or f"connect-{module.split('-', 1)[-1]}" in parts


def _module_shell_files(repo_path: Path, module: str) -> list[Path]:
    names = (
        f"{module}.module.ts",
        f"{module}.view.ts",
        "pages-index.ts",
    )
    found: list[Path] = []
    for base in _module_search_roots(repo_path, module):
        for name in names:
            candidate = base / name
            if candidate.exists():
                found.append(candidate)
        pages_dir = base / "pages"
        if pages_dir.is_dir():
            for page in sorted(pages_dir.glob("*.page.ts")):
                if page not in found:
                    found.append(page)
    return found


def _module_search_roots(repo_path: Path, module: str) -> list[Path]:
    roots: list[Path] = []
    host = repo_path / "frontend" / "src" / "modules" / module
    if host.exists():
        roots.append(host.resolve())
    pkg = repo_path / module / "frontend" / "src" / "modules" / module
    if pkg.exists():
        roots.append(pkg.resolve())
    return roots


def _registry_files(repo_path: Path, slug: str, module: str) -> list[Path]:
    registry = repo_path / "frontend" / "src" / "registry"
    found: list[Path] = []
    for name in ("page.registry.ts", "route.registry.ts", "module.registry.ts"):
        path = registry / name
        if not path.exists():
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if slug in content or f"'{module}'" in content or f"/{slug}" in content:
            found.append(path)
    return found


def _search_files(repo_path: Path, filename: str) -> list[Path]:
    matches: list[Path] = []
    roots = [
        repo_path / "frontend" / "src",
        *repo_path.glob("connect-*/frontend/src"),
    ]
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob(filename):
            if _is_ignored(path):
                continue
            if path not in matches:
                matches.append(path)
    return matches


def _resolve_ts_reexport(repo_path: Path, wrapper: Path) -> Path | None:
    try:
        content = wrapper.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    match = _RE_EXPORT.search(content)
    if not match:
        return None
    target = match.group("target")
    if not target.startswith("."):
        return None

    resolved = (wrapper.parent / target).resolve()
    if resolved.suffix != ".ts":
        resolved = resolved.with_suffix(".ts")
    if resolved.exists():
        return resolved

    basename = Path(target).name
    module_hint = extract_module_from_page_slug(route_slug(wrapper.stem))
    for candidate in _search_files(repo_path, basename):
        if _belongs_to_module(candidate, module_hint):
            return candidate
    return None


def _package_root(path: Path) -> Path | None:
    parts = path.parts
    for idx, part in enumerate(parts):
        if part.startswith("connect-") and idx + 1 < len(parts) and parts[idx + 1] == "frontend":
            return Path(*parts[: idx + 2])
    if "frontend" in parts:
        idx = parts.index("frontend")
        return Path(*parts[: idx + 1])
    return None


def _is_ignored(path: Path) -> bool:
    return any(part in _IGNORED_PARTS for part in path.parts)
