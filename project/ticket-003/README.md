# Ticket 003: Resolve c2004 SPA routes and copy packages in restore service

- **ID**: ticket-003
- **Owner**: agent:antigravity
- **Status**: IN_PROGRESS
- **Workflow state**: EDIT
- **Created**: 2026-09-27

## Goal and scope

Enhance `RestoreService` to resolve c2004 flat SPA page routes (e.g. `/connect-test-customers`) to module source files and copy relevant `connect-*` packages while safely ignoring dangling symlinks in c2004.

## Acceptance criteria

- [x] AC-01: `resolve_c2004_route` maps flat routes to module pages, wrappers, and module shell files.
- [x] AC-02: `RestoreService.extract_endpoint` copies route SPA files and dependent monorepo packages.
- [x] AC-03: `shutil.copytree` handles symlinks safely without crashing on broken symlinks (`symlinks=True, ignore_dangling_symlinks=True`).
- [x] AC-04: Unit tests in `tests/test_c2004_restore_routes.py` and `tests/test_c2004_route_resolver.py` pass cleanly.
