# rebuild

## Code Evolution Intelligence Engine

![Version](https://img.shields.io/badge/version-0.1.46-blue) ![Python](https://img.shields.io/badge/python-3.11+-blue) ![License](https://img.shields.io/badge/license-Apache--2.0-green) ![Tests](https://img.shields.io/badge/tests-634%20passing-brightgreen) ![Coverage](https://img.shields.io/badge/coverage-72%25-brightgreen)

**Historical deployment analysis & Code Intelligence** — walk git history day by day, deploy per commit, test all endpoints, capture screenshots, and **analyze code evolution** to find duplicates, rank quality, and generate refactor plans.

> **SUMD stats** (v0.1.23): 3722 functions · 161 classes · 167 files · CC̄ = 3.9

---

### AI Cost Tracking

![PyPI](https://img.shields.io/badge/pypi-costs-blue) ![Version](https://img.shields.io/badge/version-0.1.46-blue) ![Python](https://img.shields.io/badge/python-3.9+-blue) ![License](https://img.shields.io/badge/license-Apache--2.0-green)
![AI Cost](https://img.shields.io/badge/AI%20Cost-$41.90-orange) ![Human Time](https://img.shields.io/badge/Human%20Time-44.9h-blue) ![Model](https://img.shields.io/badge/Model-openrouter%2Fqwen%2Fqwen3--coder--next-lightgrey)

- 🤖 **LLM usage:** $41.9003 (72 commits)
- 👤 **Human dev:** ~$4490 (44.9h @ $100/h, 30min dedup)

Generated on 2026-10-18 using [openrouter/qwen/qwen3-coder-next](https://openrouter.ai/qwen/qwen3-coder-next)

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| **[Getting Started](docs/getting-started/installation.md)** | Installation, quickstart, configuration |
| **[Walk Command](docs/guide/walk.md)** | Core walk workflow — deploy modes, output, rebuild.yaml |
| **[Analyze](docs/guide/analyze.md)** | Duplicates, service graph, truth, vector search, multi-repo |
| **[Refactor](docs/guide/refactor.md)** | AI-powered refactor plans + execution |
| **[Auto-PR](docs/guide/auto-pr.md)** | Automated GitHub/GitLab PR creation |
| **[Plugins](docs/guide/plugins.md)** | Custom scanners & reporters via entry points |
| **[CLI Reference](docs/reference/cli.md)** | All commands and options |
| **[Config Reference](docs/reference/config.md)** | Full `rebuild.yaml` field reference |
| **[Architecture](docs/architecture.md)** | 5-layer design, services, data flow |
| **[Case Study: c2004](docs/case_study_c2004.md)** | Real-world analysis of a large ecosystem |
| **[c2004 Testing Log](docs/c2004.md)** | Detailed test log with commands & results |
| **[Usage Guide](docs/usage.md)** | Step-by-step guide (all features) |
| **[Changelog](CHANGELOG.md)** | Release history (current: v0.1.23) |
| **[Roadmap](TODO.md)** | Completed phases 10–16, future plans |
| **[Analysis (P1–P4)](ANALYSIS.md)** | Refactoring hotspots, infra gaps, missing features, test debt + sprint plan |

---

## 🚀 Quick Start

```bash
# Install
pip install rebuild

# Initialise config
rebuild init /path/to/my-service

# Walk last 14 days (dry-run, no deploy)
rebuild walk /path/to/my-service --deploy none --days 14 --dry-run

# Serve results
rebuild serve --results-dir /path/to/my-service/.rebuild
```

See **[Installation](docs/getting-started/installation.md)** and **[Quick Start](docs/getting-started/quickstart.md)** for details.

---

## What it does

| # | Layer | Description |
|---|-------|-------------|
| 1 | **[Intelligence](docs/guide/analyze.md)** | Structural & semantic duplicates (Python/JS/TS), service graphs, vector search, quality ranking |
| 2 | **[Decision Engine](docs/guide/refactor.md)** | AI-powered refactoring plans + automated execution |
| 3 | **[Walk](docs/guide/walk.md)** | Git history iteration (Incremental, Replay, Accelerator modes) |
| 4 | **[Deploy](docs/reference/cli.md#rebuild-walk)** | Docker Compose / Replay / Accelerator hot-reload per commit |
| 5 | **[Scan & Test](docs/usage.md#3-historical-analysis-the-walk)** | OpenAPI, FastAPI routes, Traefik discovery; auth, param substitution, body injection |
| 6 | **[Visualization](docs/usage.md#6-visualization)** | D3.js graphs, health dashboards, SSE streaming, evolution playback |
| 7 | **[Automation](docs/guide/auto-pr.md)** | Auto PR, [DSL scripting](docs/usage.md#8-dsl-scripting), [NLP commands](docs/usage.md#8-dsl-scripting), [Plugins](docs/guide/plugins.md), [Notifications](docs/reference/config.md) |

---

## 🚀 c2004 Case Study

Applying `rebuild` to the massive **c2004** project (88 subdirectories, thousands of files).
See full details: **[Case Study](docs/case_study_c2004.md)** · **[Testing Log](docs/c2004.md)**

### 1. Duplication Detection
```bash
rebuild analyze duplicates /path/to/c2004
```
![Duplication Analysis](docs/img/c2004_duplication.png)
*Result: Found 1,597 duplicate groups across Python and JS/TS files.*

### 2. Architecture Graph
```bash
rebuild analyze services /path/to/c2004/backend --export
```
![Architecture Graph](docs/img/c2004_graph.png)
*Result: Interactive D3.js map highlighting circular dependencies.*

### 3. AI Refactor Planning
```bash
rebuild refactor plan /path/to/c2004/backend --ai
rebuild refactor pr /path/to/c2004/backend
```
*Result: 122 high-impact suggestions with automated PR descriptions.*

### 4. Health Dashboard
```bash
rebuild dashboard --repo /path/to/c2004
```
![Health Dashboard](docs/img/c2004_dashboard.png)
*Result: Correlation between technical debt and API pass rates.*

---

## Examples

Explore ready-to-run scenarios in [`examples/`](examples/):
- **[01-dry-run-walk](examples/01-dry-run-walk/)**: Standard walk + intelligence.
- **[02-docker-compose-project](examples/02-docker-compose-project/)**: Full pipeline with **Docker isolation**.
- **[03-restore-endpoint](examples/03-restore-endpoint/)**: Discovering "truth" and extracting endpoints.

---

## Project Status

All **Phases 10–16** completed. See **[TODO.md](TODO.md)** for full roadmap.

| Milestone | Status |
|-----------|--------|
| c2004 Testing & Intelligence (Phase 10) | ✅ Done |
| Semantic Embeddings & Vector Search (Phase 11) | ✅ Done |
| Multi-Repo & Real-time (Phase 12) | ✅ Done |
| UI/UX (Phase 13) | ✅ Done |
| Production Readiness (Phase 14) | ✅ Done |
| c2004 Integration (Phase 15) | ✅ Done |
| Production Release (Phase 16) | ✅ Done — PyPI, CI/CD, Docker, MkDocs, Plugins, Notifications |

**Current:** v0.1.23 · 634 tests · 72% coverage

---

## License

Licensed under Apache-2.0.
