# Analyze

> See also: [CLI Reference](../reference/cli.md#rebuild-analyze) · [Architecture](../architecture.md#3-intelligence-layer-analysis) · [Case Study: c2004](../case_study_c2004.md)

The `analyze` sub-commands inspect your codebase for structural and semantic issues.

## Duplicates

```bash
rebuild analyze duplicates /path/to/repo
rebuild analyze duplicates /path/to/repo --min-lines 4 --semantic
```

Finds structurally identical and semantically similar code fragments. Output groups duplicates by similarity and suggests which to extract.

## Services

```bash
rebuild analyze services /path/to/repo
```

Builds a dependency graph of Python services/classes. Detects import cycles.

## Git Truth

```bash
rebuild analyze truth /path/to/repo
```

Correlates git history with test results to identify the "best" version of each function — highest test pass rate and lowest complexity.

> **Note:** Truth analysis is **Python-only** (AST). For c2004 SPA routes such as `/connect-test-customers`, use `rebuild restore` (see below) or `git log -- connect-test/`.

## c2004 SPA routes (`restore`)

`rebuild restore` now resolves c2004 flat page routes via `rebuild.analysis.c2004_route_resolver`:

- `/connect-test-customers` → `connect-test/.../customers.page.ts` (through `connect-test-customers.page.ts` wrapper)
- `/connect-template2` → `connect-template2/.../connect-template2.view.ts`
- Copies matching `connect-*/frontend` packages, not only `frontend/`

```bash
rebuild restore /connect-test-customers /path/to/c2004 --output ./restored
```

Previously, restore searched for the literal path string (`/connect-test-customers`) and found **0 files**, because c2004 generates routes from page names in `page.registry.ts`.

## Vector Search

```bash
# Build index
rebuild analyze vector-build /path/to/repo

# Query
rebuild analyze vector-query /path/to/repo "authentication middleware"
```

SQLite-backed semantic code search using sentence-transformers embeddings.

## Multi-repo

```bash
rebuild analyze multi-repo /repo-a /repo-b /repo-c
```

Cross-repository dependency and duplication analysis.
