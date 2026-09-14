# Changelog

> See also: [README](README.md) · [Roadmap (TODO)](TODO.md) · [Analysis (P1–P4)](ANALYSIS.md) · [Architecture](docs/architecture.md) · [Usage Guide](docs/usage.md)

## Completed Roadmap — Phases 10–16

Aggregated summary of completed work, moved here from `TODO.md` on 2026-05-07.
Detailed per-version notes appear in entries below.

### Phase 10 — c2004 Testing & Improvements ✅ (sesja 2026-05-01, v0.1.13–v0.1.18)
- **Clone for walk**: Pipeline klonuje repo do `.rebuild/repo/` — oryginał nienaruszony
- **git checkout --force**: Bezpieczne przełączanie commitów w klonie
- **Replay mode fix**: `start()` w replay tylko sprawdza health, nie uruchamia nowego compose
- **Replay reload**: `docker restart <name>` bezpośrednio po nazwie kontenera
- **history_service**: Obsługa nowego formatu `results.json` (dict z kluczem `results`)
- **index.html**: Eksport JSON/YAML/TOON + toolbar w nawigacji
- **`rebuild serve`**: Komenda do serwowania raportów na HTTP
- **Deploy Log Details**: Pełne docker logs w `DayResult` + raporty failed deployów
- **Param Substitution**: OpenAPI/FastAPI scanner — `{param}` → wartości z `rebuild.yaml`
- **Fixture Seed**: `test_fixtures:` w `rebuild.yaml`
- **Auth Config**: `auth:` w `rebuild.yaml` dla custom headers (Bearer tokens)
- **Replay + volume mount**: Code mount per commit zamiast obrazu
- **`init` w klonie**: Nie modyfikuje oryginalnego repo
- **Deploy Retry**: Retry z backoff dla niestabilnych deployów
- **Health Check Verbose**: Szczegółowy log curl output przy fail
- **Manual Override**: `patch/` directory w `.rebuild/` z auto-applied fixes
- **Token Propagation**: Login raz, propagacja Bearer do wszystkich requestów
- **Per-Endpoint Body**: `body:` dla POST/PUT/PATCH w konfiguracji
- **Failure Grouping**: Raport HTML grupuje błędy (auth/template/missing)
- **Trend Chart**: Health% w czasie (Chart.js / SVG inline)
- **Endpoint Diff**: Endpointy znikłe/nowe między commitami
- **Response Time Tracking**: `time_ms` dla wszystkich requestów
- **Analyze c2004**: `duplicates` (1597 grup), `services`, `truth` na wybrane moduły

### Phase 11 — Deep Semantic Analysis ✅
- **Semantic Embeddings**: `sentence-transformers` w `duplication_engine` → [Analyze docs](docs/guide/analyze.md#vector-search)
- **Vector Search**: SQLite-backed vector DB → [CLI: vector-build/vector-query](docs/reference/cli.md#rebuild-analyze-vector-build-path)

### Phase 12 — Real-time & Cross-Repo ✅
- **Multi-Repo Support**: Cross-repo dependency analysis → [Analyze: multi-repo](docs/guide/analyze.md#multi-repo)
- **Real-time Monitoring**: Live SSE event log w dashboard → [Visualization](docs/usage.md#6-visualization)
- **Auto-PR Agent**: Auto PRs na GitHub/GitLab → [Auto-PR docs](docs/guide/auto-pr.md)

### Phase 13 — UI/UX Refinement ✅
- **D3.js Code Evolution**: Playback graf zależności w czasie
- **TUI Refactor**: Domain logic wyodrębniona z `interfaces/tui.py`

### Phase 14 — Production Readiness ✅ (ukończone 2026-05-01)
- **Test Coverage ≥60%**: 347 testów, 60% coverage
- **`--health-timeout` CLI**: Dla dużych stacków → [CLI Reference](docs/reference/cli.md#rebuild-walk)
- **Deploy Error Classification**: `compose_build_fail`, `port_conflict`, `migration_fail`, `missing_env` → [Architecture: Deploy Error](docs/architecture.md#deploy-error-classification)
- **Documentation Update**: `docs/usage.md`, `docs/architecture.md`, `README.md`
- **Service Table**: Kompletna tabela usług → [Architecture: Key Services](docs/architecture.md#key-services)

### Phase 15 — c2004 Integration & Stability ✅
- **c2004 npm ci fix**: `if [ -f package-lock.json ]; then npm ci; else npm install; fi`
- **c2004 Walk z `--deploy none`**: 442 endpointy w 1-day test walk
- **Config Validation**: Pydantic schema dla `rebuild.yaml` + czytelne błędy
- **PipelineEvent Import Fix**: Przeniesione do `domain_events.py` jako legacy class
- **Walk Result Regression Guard**: Auto-flag spadku health% >20%
- **c2004 Dashboard**: 444 endpointów wyświetlane poprawnie
- **`--output` respects rebuild.yaml**: `output.dir` z YAML nadpisuje domyślne `.rebuild`
- **Deploy log truncation**: Limit 200 linii w `results.json` z info o obcięciu
- **Health verbose summary**: Status + first 200 bytes body przy fail
- **Endpoint count diff warning**: Ostrzeżenie przy zmianie >10% między dniami

### Phase 16 — Production Release ✅
- **PyPI Package**: `rebuild` na PyPI v0.1.20 → [PyPI](https://pypi.org/project/rebuild/)
- **CI/CD Pipeline**: GitHub Actions — testy, ruff, coverage gate ≥70% → [`.github/workflows/`](.github/workflows/)
- **Semantic Versioning**: Auto-bump z CHANGELOG → `scripts/bump_version.py`
- **Docker Image**: `ghcr.io/semcod/rebuild:latest` → `Dockerfile` + `.github/workflows/docker.yml`
- **Config Validation (pydantic)**: `RebuildConfig`, `ConfigSchemaValidator`, `load_and_validate()` → [Config Reference](docs/reference/config.md)
- **Plugin System**: `BaseScanner`, `BaseReporter`, `PluginRegistry`, entry points `rebuild.scanners`/`rebuild.reporters`, `rebuild plugins` CLI → [Plugin docs](docs/guide/plugins.md)
- **Documentation Site**: MkDocs Material → [GitHub Pages](https://semcod.github.io/resplit)
- **TUI Full Features**: j/k navigation, g/G, live log, endpoint browser
- **Export Formats**: CSV + Markdown summary
- **Notification Hooks**: Slack/Discord webhooks na deploy fail / health regression → [Config Reference](docs/reference/config.md)
- **Snapshot Management**: LRU cache, `max_snapshots`, `_auto_prune()`, `prune_old(keep=N)`, `stats()`
- **Test Coverage ≥70%**: Osiągnięto 72% (634 testów)

---

## [Unreleased]

## [0.1.40] - 2026-09-14

### Fixed
- [ticket-002] build: remove pfix auto-repair configuration

## [0.1.39] - 2026-09-08

### Docs
- docs: adopt pinned local OneDev and Validator publication policy

## [0.1.38] - 2026-07-20

### Fixed
- fix(tests): catch Typer vendored exit type

### Test
- chore(deps): require testql 1.2.64
- chore(deps): require testql 1.2.63

## [0.1.37] - 2026-07-08

### Unreleased
### Merged
- Merged divergent origin/main history (bump chain up to 0.1.25, including a `tests/test_e2e_tui.py` update); local version numbering (0.1.36) kept as authoritative.
### Sprint 1 — Quality Gates + Infra Foundation (2026-05-07)
Hardening pipeline'u CI bez zmian architektury. Patrz [ANALYSIS.md](ANALYSIS.md) Sprint 1.
#### Added
- **`.pre-commit-config.yaml`** — ruff (lint+format), mypy (non-blocking), built-in hygiene hooks (trailing-ws, eof, check-yaml/toml/large-files, debug-statements)
- **`docker-compose.example.yml`** — przykład deployment z rebuild + dashboard + repo mount na `localhost:7821`
- **`ANALYSIS.md`** — kompletna analiza P1–P4 + plan sprintów 1–5+ wzorowana na metodologii Semcod GitHub App
#### Changed
- **`.github/workflows/ci.yml`** — dodany krok `mypy` jako `continue-on-error` (non-blocking, gotowy do promowania w Sprincie 3)
- **`.github/workflows/docker.yml`** — multi-arch build `linux/amd64,linux/arm64` + `setup-qemu-action@v3`. Krytyczne dla testowania na ARM (case c2004).
- **`TODO.md`** — przeniesione Phasy 10–16 do [CHANGELOG: Completed Roadmap](#completed-roadmap--phases-1016); zostawione tylko Phase 17 + plan sprintów
#### Fixed
- **Ruff config bug** w [`.github/workflows/ci.yml`](.github/workflows/ci.yml): usunięte `--ignore W503` (W503 to flake8 pseudo-rule, nieistniejąca w ruff). CI fail-ował natychmiast przy lint step.
- **354 błędów stylu w `rebuild/`**: 302 auto-fix (whitespace, redundant f-strings, etc.) + 52 unsafe-fix (W291, W293) + 7 ręcznych E701 (`if x: continue` → wieloliniowe) + 3 brakujące importy F821:
  - `rebuild/application/services/override_service.py`: `Optional` z `typing`
  - `rebuild/infrastructure/shell_adapter.py`: `Path` z `pathlib` (×2)
### Sprint 2 — Konsolidacja Duplikatów (2026-05-07)
Refactor niskiego ryzyka eliminujący duplikaty wskazane w [ANALYSIS.md](ANALYSIS.md) §P1.
#### Added
- **`rebuild/application/services/regression_service.py`** — single source of truth dla detekcji regresji health-pct.
  - Public: `compute_health_trend(results, threshold) -> List[HealthTrendPoint]`
  - Adapter dict (dla `reporter.py`): `compute_health_trend_dict(results, threshold) -> dict[day, label]`
  - Adapter list (dla `helpers.py`): `compute_health_trend_labels(results, threshold) -> List[str]`
  - Stała: `DEFAULT_REGRESSION_THRESHOLD_PP = 20.0`
  - Frozen dataclass `HealthTrendPoint(day, health_pct, delta, label, is_regression)`
- **`collect_cli_overrides(ctx, names)`** w `rebuild/interfaces/commands/helpers.py` — eliminuje 14× duplikat `ctx.get_parameter_source(name) == ParameterSource.COMMANDLINE` w typer commands.
#### Changed
- **`rebuild/application/services/reporting/reporter.py:_health_trend_by_day`** → cienki adapter delegujący do `regression_service.compute_health_trend_dict`. Public method signature i zachowanie zachowane (subclass-safe).
- **`rebuild/interfaces/commands/helpers.py:compute_health_trend_labels`** → cienki adapter delegujący do `regression_service.compute_health_trend_labels`. Public function signature zachowana — wszystkie istniejące testy i importy działają bez zmian.
- **`rebuild/interfaces/cli.py:walk()`** zredukowane z 44 LOC body do 13 LOC. Usunięty nieużywany import `from click.core import ParameterSource`.
#### Deprecated
- **`rebuild.domain.dsl`** (legacy v1): dodany `DeprecationWarning` przy imporcie modułu + `.. deprecated:: 0.1.26` w docstringu. Pełne usunięcie odroczone do Sprintu 4 — `dsl_v2` nie pokrywa wszystkich komend (`evolution`, `auto_pr`, `restore`, `serve`); pełnym zamiennikiem będzie `testql` (PyPI v0.6.18).
- **`Endpoint.testql_passed`** field: explicit komentarz że to placeholder na Sprint 4 (currently never populated by walk/test pipelines).
#### Verification
- `ruff check rebuild/ --select E,W,F --ignore E501` → **All checks passed**
- `pytest -k "trend or regression or health"` → 8 passed (pełna pokrywalność migracji)
- `pytest`: 631 passed, 3 preexisting failures (`TestCLISubprocessE2E.*` — środowiskowy `No module named rebuild`, nie regresja)
### Sprint 3 — Showcase + Performance (2026-05-07)
Materiał case-study + dowód wydajności. Patrz [ANALYSIS.md](ANALYSIS.md) Sprint 3.
#### Added
- **`scripts/benchmark_scanner_cache.py`** — kompletny benchmark diff-aware cache: synthetic FastAPI fixture, parametry `--commits/--files/--churn/--seed`, output text albo JSON (`-q`). Mierzy speedup, hit rate, i `cache_stats`.
- **`docs/benchmarks.md`** — zmierzone wyniki: **5.5–6.6× speedup** przy realistycznych parametrach (200-500 plików, 5% churn, hit rate 91.8%). Tabela rozdzielczo-zależna od churn (5-50%).
- **`scripts/run_c2004_full.sh`** — kanoniczny reproducer dla c2004 case-study: pre-flight checks (rebuild/git/docker), auto-clone, walk z docker-compose, dashboard, summary stats. `SKIP_DEPLOY=1` dla dry-run mode.
- **`examples/05-ci-integrations/`** — gotowe recipes:
  - `github-actions.yml` — PR diff scan + auto-comment, nightly full walk z artifactami, secrets dla webhooks
  - `gitlab-ci.yml` — MR scan + scheduled nightly z dind
  - `circleci.yml` — workflows `pr` (lekki) i `nightly` (machine + docker)
  - `README.md` z customisation guide
- **`tests/test_plugins.py`** — 25 testów pokrywających `rebuild/plugins/` (registry, BaseScanner, BaseReporter, ScanResult, entry-point discovery z mockowanym `importlib.metadata`).
- **`tests/test_api_app.py`** — 15 testów dla command + query endpointów (`/commands/{walk,analyze,snapshot,prune,dsl,nlp}`, `/queries/{history,day,snapshots,plugins}`).
#### Changed
- **`rebuild/application/services/scanner_service.py`** — content-hash cache:
  - Nowa metoda `_endpoints_for_python_file(py_file) -> List[Endpoint]` cache'uje wynik AST parse + decorator scan po SHA-1 zawartości pliku.
  - Public API: property `cache_stats: {"hits", "misses", "size"}`, metoda `reset_cache()`.
  - Cache jest **on by default**, process-local, automatycznie współdzielony przez wszystkie scany w tym samym walku (`BasePipeline` tworzy jeden `ScannerService`).
  - Cykliczne typowanie: dodany `Dict` + `hashlib` import.
  - Hit rate na poziomie 91.8% przy 5% churn (typowy commit).
- **`rebuild/interfaces/api/app.py`** — naprawiony realny bug: usunięte `from __future__ import annotations` (powodowało, że FastAPI traktował pydantic Command modele jako query params, zwracając 422 dla każdego POST `/commands/*`). Wszystkie 4 endpointy (`/commands/walk|analyze|snapshot|prune`) teraz akceptują JSON body. Dodany `Body(...)` + `model_rebuild()` dla forward-ref resolution.
#### Fixed
- **API command endpoints zwracały 422** — szczegóły wyżej w Changed. Bug był present od Phase 16 (pierwsze CQRS API), nigdy niepokryty testem POST.
#### Verification
- `ruff check rebuild/ scripts/benchmark_scanner_cache.py --select E,W,F --ignore E501` → **All checks passed**
- `pytest tests/test_plugins.py` → 25 passed
- `pytest tests/test_api_app.py tests/test_cqrs_arch.py` → 97 passed (15 nowych + 82 cqrs_arch)
- `pytest tests/test_scanner_service.py` → 19 passed (11 starych + 8 nowych dla cache)
- **Coverage**: 75% → 77% (`plugins/` 0→100%, `api/app.py` 58→78%)
- `bash -n scripts/run_c2004_full.sh` → syntax OK
- Benchmark realny: `python scripts/benchmark_scanner_cache.py --commits 30 --files 200 --churn 0.05` → **5.5× speedup, 91.8% hit rate**
### Sprint 4 — Reuse Bibliotek + Watch Mode (2026-05-07) [partial]
Pierwsza realna integracja `[full]` extras. Patrz [ANALYSIS.md](ANALYSIS.md) Sprint 4.
#### Added
- **`rebuild watch` command** ([`watch_command.py`](rebuild/interfaces/commands/watch_command.py)) — long-running mode oparty o `wup.WupWatcher`:
  - File-watching, debouncing (default 2s), CPU throttling, test cooldowns delegowane do `wup`.
  - Custom `on_change` handler wywołuje `rebuild walk --dry-run --days 1` w subprocess z timeout 120s.
  - Skonfigurowane wykluczenia: `.git`, `.venv`, `node_modules`, `__pycache__`, `.rebuild`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`.
  - Watcher factory injection (`_watcher_factory` parameter) dla pełnego mockowania w testach.
  - `wup` jest **optional dependency** — `_require_wup()` raise'uje przyjazny `RuntimeError` z instrukcją instalacji.
- **`tests/test_watch_command.py`** — 12 testów: cala ścieżka happy-path, error handling (timeout, non-zero exit), graceful KeyboardInterrupt, custom on_change override, weryfikacja `WupConfig` struktury (project/watch/services).
- **Mutation testing infrastructure** (Sprint 4b):
  - **`[tool.mutmut]`** w [`pyproject.toml`](pyproject.toml) z `paths_to_mutate = "rebuild/domain/"`.
  - **[`scripts/run_mutation_tests.sh`](scripts/run_mutation_tests.sh)** — wrapper z baseline-check + Markdown report + threshold gate (default 75% mutation score).
  - **[`.github/workflows/mutation.yml`](.github/workflows/mutation.yml)** — nightly @ 03:00 UTC + `workflow_dispatch`. Non-blocking dla PRs (zbyt wolne dla feedback loop). Artifacts: `mutation-report-<run_id>` + `mutmut-cache-<run_id>` (incremental).
  - **[`docs/mutation_testing.md`](docs/mutation_testing.md)** — kompletny guide: rationale, lokalne uruchamianie, inspekcja survivor-ów, plany rozszerzeń (differential PR-aware mutation, parallel jobs).
#### Changed
- **`pyproject.toml`** — nowe `[project.optional-dependencies]`:
  - **`watch`** = `["wup>=0.2.21"]` (instalacja: `pip install 'rebuild[watch]'`)
  - **`api`** = `["fastapi>=0.115", "uvicorn[standard]>=0.30"]`
  - **`full`** zaktualizowany — dodano FastAPI/uvicorn, pinnięty `wup>=0.2.21`
  - **`dev`** dodano `mutmut>=2.5`
#### Deferred to Sprint 5+
- **`testql` integracja** — `testql 1.x` ma puste top-level eksporty; wymaga osobnej sesji eksploracji submodułów + jasnej decyzji jakich verb-ów potrzebujemy.
- **`regres` integracja** — pakiet eksportuje moduły CLI (`doctor`, `defscan`, `refactor`, `regres`), brak czystego Python API; integracja wymaga adaptera shell-runner albo czekania na API stabilizację.
#### Verification
- `ruff check rebuild/ scripts/benchmark_scanner_cache.py --select E,W,F --ignore E501` → **All checks passed**
- `pytest tests/test_watch_command.py` → 12 passed (z mockowanym wup; 12 = `_require_wup` × 2, `_build_default_wup_config` × 1, `_default_on_change` × 4, `watch_command` × 5)
- `pytest`: nadal 631 passed + 12 nowych = 643 passed, 3 preexisting failures (te same)
- `bash -n scripts/run_mutation_tests.sh` → syntax OK
- `python -c "import yaml; yaml.safe_load(open('.github/workflows/mutation.yml'))"` → YAML OK
- CLI registration: `rebuild watch --help` widoczne w `app.commands` (test: `from rebuild.interfaces.cli import app`)
### Sprint 5c — Coverage ≥80% + Dead-Code Removal (2026-05-08)
Realizacja TODO Phase 17 → "Test Coverage ≥80%". Patrz [TODO.md](TODO.md).
#### Added
- **`tests/test_coverage_sprint5c.py`** (76 testów) — pokrycie wcześniej
  martwych ścieżek w:
  - `domain/context.py` (0 → 100%) — dataclass `EndpointContext`.
  - `domain/mvp_protocol.py` (68% → ~98%) — wszystkie gałęzie routingu
    `MVPProtocolHandler` (unknown type, str→enum coercion, brakujące parametry,
    wyjątki w handlerach DSL/NLP, smoke `MVPServer.__init__`).
  - `application/services/tui_data_service.py` (25% → ~95%) — `load_day_results`
    (skip non-dirs, invalid dates, corrupt JSON), `endpoint_diff` (added/removed/
    status_changed), `health_bar` (3 progi), `calc_health`, `get_git_repo_toplevel`
    (3 ścieżki).
  - `application/services/test_service.py` (60% → ~98%) — pełny matrix
    `_classify_http_status`, dispatch HTTP verbów (GET/POST/PUT/PATCH/DELETE/OPTIONS),
    klasyfikacja błędów sieciowych, login z bearer-token i fallback.
  - `analysis/service_similarity.py` (49% → 100%) — analyzer + Jaccard-overlap +
    sortowanie wyników.
  - `interfaces/dashboard.py` (74% → 100%) — `_extract_avg_cc`, `get_cc_for_day`
    (4 ścieżki: missing toon, non-zero exit, invalid JSON, success), `generate_dashboard`
    z/bez repo.
  - `refactor/refactor_executor.py` (48% → 100%) — wszystkie gałęzie `execute_suggestion`
    + `_merge_duplicates` (empty files, real rewrite, OSError).
  - `interfaces/commands/helpers.py:serve_reports` (48% → 92%) — driving inner
    `SSEHandler.do_GET` przez stub-server, KeyboardInterrupt graceful shutdown.
  - `interfaces/commands/walk_command.py:_fire_notifications` + `_resolve_deploy_method`
    (62% → ~78%) — 3 ścieżki dla każdego helpera.
#### Removed
- **`rebuild/domain/events.py`** — martwy moduł (14 LOC) shadow'owany przez
  pakiet `rebuild/domain/events/` od Phase 14. `PipelineEvent` żyje
  w `events/domain_events.py` (re-eksport z `__init__.py`). Usunięcie eliminuje
  fałszywy 0% coverage entry i potencjalny pułapkę dla kontrybutorów.
#### Verification
- `pytest tests/test_coverage_sprint5c.py` → **76 passed**
- `pytest`: **905 passed** (poprzednio 829 → +76), 3 preexisting `TestCLISubprocessE2E`
  failures (środowiskowy `No module named rebuild`).
- **Coverage: 79% → 80%** (TOTAL 6925 stmts, 1393 missed; było 6939/1611 przed
  Sprintem 5c). Konkretne moduły osiągnęły 100%: `refactor_executor.py`,
  `service_similarity.py`, `dashboard.py`, `endpoint_trend_service.py`,
  `metrics.py`.
- `ruff check tests/test_coverage_sprint5c.py rebuild/ --select E,W,F --ignore E501`
  → **All checks passed**.
### Sprint 5b — Reporter Refactor + Endpoint-Trend Konsolidacja (2026-05-08)
Decompozycja 434-LOC `reporter.py` na fokus-moduły + finalna eliminacja
duplikatu `_endpoint_count_trend_by_day` ↔ `compute_endpoint_count_trend_labels`
(odroczone z Sprint 2). Patrz [TODO.md](TODO.md) → "Refactor `reporter.py`".
#### Added
- **`rebuild/application/services/endpoint_trend_service.py`** — single source
  of truth dla detekcji zmian liczby endpointów (analog do `regression_service`).
  - Public: `compute_endpoint_count_trend(results, threshold) -> List[EndpointTrendPoint]`
  - Adapter dict: `compute_endpoint_count_trend_dict(results, threshold) -> dict[day, label]`
  - Adapter list: `compute_endpoint_count_trend_labels(results, threshold) -> List[str]`
  - Stała: `DEFAULT_ENDPOINT_WARNING_PCT = 10.0`
  - Frozen dataclass `EndpointTrendPoint(day, total, delta, label, is_warning)`
- **`rebuild/application/services/reporting/_html_assets.py`** (29 LOC) —
  współdzielone `JS_HELPERS` + `CSS_VARS`.
- **`rebuild/application/services/reporting/day_html.py`** (168 LOC) — pure
  funkcje `render_day_html`, `render_endpoint_row(s)`, `render_deploy_section`,
  `render_deploy_log`, `render_deploy_category`. Każda jednostkowo testowalna,
  bez stanu klasy.
- **`rebuild/application/services/reporting/timeline_html.py`** (174 LOC) —
  `render_timeline_html(results, output_dir)` + `build_export_data(results)` +
  prywatny `_render_day_row` + `_trend_dicts` (delegujący do dwóch trend
  serwisów).
- **`rebuild/application/services/reporting/summary_export.py`** (84 LOC) —
  `write_csv` / `write_markdown` jako pure functions.
- **`tests/test_endpoint_trend_service.py`** (16 testów) — pełna pokrywalność
  publicznego API + dwóch adapterów + delegacji `helpers.py` i wewnętrznego
  `ReporterService._endpoint_count_trend_by_day`.
#### Changed
- **`rebuild/application/services/reporting/reporter.py`** — z 434 LOC do
  120 LOC (-72%). `ReporterService` jest teraz fasadą:
  - `save_day` → `render_day_html` + zapis JSON/YAML/TOON
  - `save_timeline_index` → `build_export_data` + `render_timeline_html`
  - `export_csv` / `export_markdown` → `write_csv` / `write_markdown`
  - `_endpoint_count_trend_by_day` → `compute_endpoint_count_trend_dict`
    (analogicznie jak `_health_trend_by_day` z Sprint 2)
  - Zachowane wszystkie publiczne metody i prywatne `_save_html_day`,
    `_endpoint_rows`, `_endpoint_row`, `_deploy_section`, `_results_to_export_data`
    jako thin shims dla backward-compat.
- **`rebuild/interfaces/commands/helpers.py:compute_endpoint_count_trend_labels`**
  → cienki adapter delegujący do `endpoint_trend_service.compute_endpoint_count_trend_labels`.
#### Verification
- `pytest tests/test_endpoint_trend_service.py` → **16 passed**
- `pytest tests/test_reporter_service.py tests/test_git_helpers_extra.py tests/test_coverage_phase16.py` → **139 passed** (zerowa regresja w testach trendu)
- `pytest`: **829 passed** (poprzednio 813 → +16 endpoint-trend), 3 preexisting `TestCLISubprocessE2E` failures (środowiskowy)
- `ruff check rebuild/ tests/test_endpoint_trend_service.py tests/test_metrics.py --select E,W,F --ignore E501` → **All checks passed**
- LOC count po refaktorze:
  - `reporter.py` 434 → 120 (fasada)
  - `day_html.py` 168 + `timeline_html.py` 174 + `summary_export.py` 84 + `_html_assets.py` 29 = 455 LOC w focus-modułach
  - `endpoint_trend_service.py` 134 LOC
### Sprint 5a — Prometheus /metrics Endpoint (2026-05-08)
Realizacja TODO Phase 17 → "Grafana Integration". Patrz [TODO.md](TODO.md) i [ANALYSIS.md](ANALYSIS.md) Sprint 5+.
#### Added
- **`rebuild/interfaces/api/metrics.py`** — Prometheus instrumentation dla `create_app()`:
  - `_require_prometheus()` — lazy import z czytelnym komunikatem `"Install with: pip install 'rebuild[api]'"`.
  - `setup_metrics(app, registry=None)` — rejestruje middleware + `GET /metrics` w prometheus text format.
  - **Metryki**:
    - `rebuild_http_requests_total{method,path,status}` (counter)
    - `rebuild_http_request_duration_seconds{method,path}` (histogram, buckets 5ms→5s)
    - `rebuild_walks_total` (counter) — walk dispatched
    - `rebuild_scan_cache_hits_total` / `rebuild_scan_cache_misses_total`
    - `rebuild_active_ws_connections` (gauge)
  - Middleware pomija samo `/metrics` (no feedback loop) i mierzy `time.perf_counter()` per-request.
  - Handle'y zapisane na `app.state.prom_*` dla introspection / dependency injection.
- **`tests/test_metrics.py`** — 9 testów: import guard, route registration, end-to-end format, middleware counter increment, `/metrics` skip, `app.state` introspection, `create_app` integration, health endpoint smoke. Każdy test używa świeżego `CollectorRegistry` (fixture `fresh_registry`) — brak monkey-patchowania prometheus internals.
#### Changed
- **`rebuild/interfaces/api/app.py:create_app`** — dodany parameter `metrics_registry=None` przekazywany do `setup_metrics()`. Domyślnie każdy app dostaje *własny* `CollectorRegistry` (zamiast globalnego `prom.REGISTRY`) co eliminuje `ValueError: Duplicated timeseries` przy wielokrotnym `create_app()` w testach / multi-app embedding. Globalny default pozostaje dostępny przez `create_app(metrics_registry=prometheus_client.REGISTRY)`.
- **`pyproject.toml`** — `[project.optional-dependencies] api` rozszerzone o `prometheus-client>=0.20`.
#### Verification
- `pytest tests/test_metrics.py` → **9 passed**
- `pytest tests/test_metrics.py tests/test_api_app.py tests/test_cqrs_arch.py` → **106 passed**
- `pytest`: 813 passed (po Sprint 4: 643 → +9 metrics + ostatnie testy z innych sesji), 3 preexisting `TestCLISubprocessE2E` failures (środowiskowy `No module named rebuild`).
- `ruff check rebuild/interfaces/api/{metrics,app}.py tests/test_metrics.py --select E,W,F --ignore E501` → **All checks passed** (po usunięciu unused `Optional` import).
#### Usage
```bash
pip install 'rebuild[api]'
uvicorn rebuild.interfaces.api.app:create_app --factory --host 0.0.0.0 --port 8000
curl http://localhost:8000/metrics
```
Konfiguracja Prometheus scrape:
```yaml
scrape_configs:
  - job_name: rebuild
    static_configs: [{targets: ['rebuild:8000']}]
    metrics_path: /metrics
```
### Sprint 4c — Analyze Services Bug Fixes (2026-05-07)
Drobne ale uciążliwe regresje znalezione przy uruchomieniu `rebuild analyze services`
na dużym repo (c2004 ≈ 88 podkatalogów). Fix po stronie upstream (silnik), bez workaroundów.
#### Fixed
- **`SyntaxWarning: invalid escape sequence`** w `ServiceGraphBuilder.build()`
  ([`rebuild/analysis/service_graph.py`](rebuild/analysis/service_graph.py)). Builder rekursywnie
  parsował **wszystkie** `*.py` w drzewie, w tym pliki w `.venv/`/`venv/` zawierające regex
  patterny bez prefiksu `r"..."` (`\S`, `\[`, `\:` w `matplotlib`, `dotenv`, etc.).
  → Dodany ten sam set wykluczeń, którego używa już `MultiRepoAnalyzer._iter_code_files`:
  `{".git", ".venv", "venv", "__pycache__", "node_modules", ".rebuild"}`.
- **Fałszywe self-loop cycles** w `detect_cycles()`. Gdy moduł `foo.py` współistnieje z
  pakietem `foo/` o tej samej nazwie (legalne w Pythonie — pakiet wygrywa w resolverze),
  `roles.py` z `from .roles import X` był rozwijany do `c2004.backend.api.routes.v3.roles`,
  identycznego z `node.name` → fałszywy self-cycle w outputcie. → `_analyze_file()` filtruje
  teraz `dep == node.name` zarówno dla `ast.Import` jak i `ast.ImportFrom`.
#### Verification
- `pytest tests/ -k "graph or services or analysis"` → **90 passed** (z `--tb=short -q`)
- `python3 -m rebuild analyze services /home/tom/github/maskservice/c2004 --export` →
  brak `SyntaxWarning`, brak fałszywego cyklu, czysty eksport `architecture.html`.
---

### Added
- feat(docs): deep code analysis engine with 3 supporting modules
- feat(docs): output formatting with 2 supporting modules
- ci: add org metadata sync trigger workflow
- feat(docs): CLI interface improvements

### Changed
- refactor(examples): configuration management system

### Fixed
- Regenerate app.doql.less with adopt fixes (entry points, env_vars, no empty pages).
- refactor: ruff check --fix + ruff format autofixes

### Docs
- docs: note merge of divergent origin/main history in CHANGELOG
- docs(docs): deep code analysis engine with 3 supporting modules
- docs(docs): changelog generation
- refactor(docs): configuration management system
- docs(docs): configuration management system
- refactor(docs): code analysis engine
- docs(docs): configuration management system
- refactor(docs): code analysis engine
- refactor(docs): intelligent code analysis pipeline
- refactor(docs): configuration management system
- refactor(docs): code analysis engine
- refactor(docs): intelligent code analysis pipeline

### Other
- refaktor

## [0.1.36] - 2026-06-29

### Docs
- Update README.md

## [0.1.35] - 2026-05-12

### Docs
- Update README.md
- Update docs/c2004.md

## [0.1.34] - 2026-05-08

### Docs
- Update README.md

## [0.1.33] - 2026-05-08

### Docs
- Update CHANGELOG.md
- Update README.md
- Update TODO.md

### Test
- Update tests/test_coverage_sprint5c.py

### Other
- Update rebuild/domain/events.py

## [0.1.32] - 2026-05-08

### Docs
- Update CHANGELOG.md
- Update README.md
- Update TODO.md

## [0.1.31] - 2026-05-08

### Docs
- Update CHANGELOG.md
- Update README.md
- Update SUMD.md
- Update SUMR.md
- Update TODO.md
- Update docs/README.md
- Update project/README.md
- Update project/context.md

### Test
- Update tests/test_endpoint_trend_service.py
- Update tests/test_metrics.py

### Other
- Update app.doql.less
- Update project/analysis.toon.yaml
- Update project/calls.mmd
- Update project/calls.toon.yaml
- Update project/calls.yaml
- Update project/compact_flow.mmd
- Update project/duplication.toon.yaml
- Update project/evolution.toon.yaml
- Update project/flow.mmd
- Update project/index.html
- ... and 13 more files

## [0.1.30] - 2026-05-07

### Docs
- Update CHANGELOG.md
- Update README.md
- Update TODO.md
- Update docs/mutation_testing.md

### Test
- Update tests/test_watch_command.py

### Other
- Update rebuild/analysis/service_graph.py
- Update rebuild/interfaces/cli.py
- Update rebuild/interfaces/commands/watch_command.py
- Update scripts/run_mutation_tests.sh

## [0.1.29] - 2026-05-07

### Docs
- Update CHANGELOG.md
- Update README.md

## [0.1.28] - 2026-05-07

### Docs
- Update README.md
- Update SUMD.md
- Update SUMR.md
- Update TODO.md
- Update docs/README.md
- Update docs/benchmarks.md
- Update project/README.md
- Update project/context.md

### Test
- Update tests/test_api_app.py
- Update tests/test_plugins.py
- Update tests/test_scanner_service.py

### Other
- Update app.doql.less
- Update project/analysis.toon.yaml
- Update project/calls.mmd
- Update project/calls.toon.yaml
- Update project/calls.yaml
- Update project/compact_flow.mmd
- Update project/duplication.toon.yaml
- Update project/evolution.toon.yaml
- Update project/flow.mmd
- Update project/index.html
- ... and 7 more files

## [0.1.27] - 2026-05-07

### Docs
- Update README.md
- Update examples/05-ci-integrations/README.md

### Test
- Update tests/test_scanner_service.py

### Other
- Update examples/05-ci-integrations/circleci.yml
- Update examples/05-ci-integrations/github-actions.yml
- Update examples/05-ci-integrations/gitlab-ci.yml
- Update rebuild/application/services/scanner_service.py

## [0.1.26] - 2026-05-07

### Docs
- Update ANALYSIS.md
- Update CHANGELOG.md
- Update README.md
- Update SUMD.md
- Update SUMR.md
- Update TODO.md
- Update docs/README.md
- Update project/README.md
- Update project/context.md

### Other
- Update .gitignore
- Update .pre-commit-config.yaml
- Update .rebuild_c2004_test/2026-04-30/results.json
- Update .rebuild_c2004_test/2026-04-30/results.toon
- Update .rebuild_c2004_test/2026-04-30/results.yaml
- Update .rebuild_c2004_test/history.json
- Update .rebuild_c2004_test/history.jsonl
- Update .rebuild_c2004_test/index.html
- Update .rebuild_c2004_test/walk_state.json
- Update .rebuild_ev/2026-05-01/commit.txt
- ... and 71 more files

## [0.1.25] - 2026-05-07

### Docs
- Update README.md
- Update SUMD.md
- Update SUMR.md

### Other
- Update app.doql.less
- Update project/map.toon.yaml

## [0.1.24] - 2026-05-07

### Docs
- Update CHANGELOG.md
- Update README.md
- Update SUMD.md
- Update TODO.md
- Update docs/README.md
- Update docs/architecture.md
- Update docs/c2004.md
- Update docs/case_study_c2004.md
- Update docs/getting-started/configuration.md
- Update docs/getting-started/installation.md
- ... and 12 more files

### Other
- Update .code2llm_cache/CHANGELOG_1778076057551732162_10277.pkl
- Update .code2llm_cache/README_1778073907205054095_118441.pkl
- Update .code2llm_cache/README_1778076055686234576_4285.pkl
- Update .code2llm_cache/__init___1778076055686826248_239.pkl
- Update .code2llm_cache/accelerated_pipeline_1778074802983432886_17641.pkl
- Update .code2llm_cache/app_1778075845753026155_1881.pkl
- Update .code2llm_cache/cli_1778074856579013858_25963.pkl
- Update .code2llm_cache/config_loader_1778074847536915897_6599.pkl
- Update .code2llm_cache/deploy_service_1778074822346642874_17643.pkl
- Update .code2llm_cache/duplication_engine_1778074797738375987_13246.pkl
- ... and 28 more files

## [0.1.23] - 2026-05-07

### Changed
- **Documentation overhaul**: Updated [README.md](README.md), [TODO.md](TODO.md), CHANGELOG.md with cross-links to all [docs/*](docs/) pages
- **SUMD.md regenerated**: Full project analysis — 3722 functions, 161 classes, 167 files, CC̄ = 3.9
- **Version sync**: All docs now reference v0.1.23 consistently

### Docs
- Updated [README.md](README.md) — documentation table, project status, SUMD stats, quick start
- Updated [TODO.md](TODO.md) — all phases marked complete, Phase 17 roadmap added, cross-links
- Updated [docs/architecture.md](docs/architecture.md) — v0.1.23, 634 tests, 72% coverage
- Updated [docs/index.md](docs/index.md) — current stats, notification hooks
- Updated [docs/getting-started/installation.md](docs/getting-started/installation.md) — version
- Updated [docs/reference/cli.md](docs/reference/cli.md) — version, notification hooks
- Updated [docs/c2004.md](docs/c2004.md) — completed items, version
- Updated [SUMD.md](SUMD.md), [docs/README.md](docs/README.md), project/ files

## [0.1.22] - 2026-05-02

### Changed
- Version bump to 0.1.22

## [0.1.21] - 2026-05-02

### Docs
- Update CHANGELOG.md
- Update README.md
- Update TODO.md

## [0.1.20] - 2026-05-02

### Fixed
- **PipelineEvent Import Fix**: Resolved `ImportError: cannot import name 'PipelineEvent' from 'rebuild.domain.events'` by moving `PipelineEvent` to `domain_events.py` as a legacy class, exporting it from `__init__.py`, and removing unnecessary imports from `pipeline.py` and `accelerated_pipeline.py` while keeping backward compatibility in `base_pipeline.py`.
- **Missing astor dependency**: Added `astor>=0.8` to dependencies for code generation in refactor executor.

### Changed
- refactoring
- refactoring
- refactoring
- refactoring

## [0.1.19] - 2026-05-01

### Docs
- Update README.md
- Update docs/architecture.md
- Update docs/usage.md

## [0.1.18] - 2026-05-01

### Docs
- Update README.md

## [0.1.17] - 2026-05-01

### Docs
- Update README.md

### Other
- Update infra-map.json
- Update rebuild/interfaces/cli.py
- Update rebuild/interfaces/commands/walk_command.py

## [0.1.16] - 2026-05-01

### Docs
- Update README.md
- Update examples/09-mvp-protocol/README.md

### Test
- Update tests/test_accelerator_extra.py
- Update tests/test_db_snapshot_extra.py
- Update tests/test_domain_infra.py
- Update tests/test_git_helpers_extra.py
- Update tests/test_interfaces_smoke.py
- Update tests/test_pipeline_extra.py
- Update tests/test_restore_override.py
- Update tests/test_smart_screenshot.py
- Update tests/test_worktree_db.py

### Other
- Update project/map.toon.yaml

## [0.1.15] - 2026-05-01

### Docs
- Update README.md

### Test
- Update tests/test_test_service.py

### Other
- Update project/duplication.toon.yaml
- Update rebuild/application/pipeline.py
- Update rebuild/application/services/deploy_service.py
- Update rebuild/application/services/scanner_service.py
- Update rebuild/application/services/test_service.py
- Update rebuild/domain/day_result.py
- Update rebuild/domain/endpoint.py
- Update rebuild/domain/models.py

## [0.1.14] - 2026-05-01

### Docs
- Update README.md
- Update docs/README.md

### Test
- Update tests/test_test_service.py

## [0.2.0] - 2026-05-01

### 🔥 Major: Full-Stack Testing & Intelligence Platform

**Auth & Testing:**
- **Auth Login**: Added `login_url` and `login_payload` for automatic token acquisition
- **Auth Headers**: Custom headers support via `auth:` config
- **Param Substitution**: `{param}` in OpenAPI paths replaced with values from `test_fixtures:`
- **Test Bodies**: Per-endpoint body configuration via `test_bodies:`
- **Response Time Tracking**: Measured and displayed in reports

**Reporting & Visualization:**
- **Failure Grouping**: Errors classified (auth, template, timeout, server, network)
- **Trend Charts**: Inline SVG health% trend visualization
- **Endpoint Diff**: Track added/removed endpoints between days
- **SSE Live Streaming**: Real-time event stream in dashboard (`/events`)
- **Modern UI**: Dark glassmorphism design with Outfit + JetBrains Mono fonts

**Deploy & Reliability:**
- **Deploy Retry**: Configurable retry with exponential backoff
- **Health Verbose**: Detailed curl output when health checks fail
- **Deploy Logs**: Full logs captured in `DayResult.deploy_log`
- **Replay Code Sync**: `docker cp` copies checkout to `/app` before restart
- **Code Overlay**: Handle read-only mounts via `/tmp/rebuild-overlay` + PYTHONPATH

**Manual Recovery:**
- **Manual Override**: `--patch-dir` to apply fixes to cloned repo before walk
- **Health Recovery**: Detect `rebuild-fix:<sha>` commits in clone for recovery
- **Git Diff Names**: `diff_names()` for smart test selection

**Accelerator Mode (10x):**
- **Sync Current State**: `sync_current_state()` for node_modules preservation
- **Git Worktree**: Shared clone with rsync overlay
- **Dockerfile Patcher**: Auto-patch for accelerator compatibility
- **DB Snapshots**: Fast database state restoration
- **Parallel Tests**: Dependency graph-based parallel execution
- **Smart Selection**: Git-diff based test selection

**Analysis & Intelligence:**
- **Semantic Embeddings**: `sentence-transformers` integration for conceptual similarity
- **Vector Search**: SQLite-backed vector index for rapid semantic lookup
- **Multi-Repo Analysis**: Cross-repo dependency and clone detection
- **Auto PR**: Automated PR creation with AI summaries
- **Evolution Viz**: D3.js code evolution playback
- **DSL**: Domain Specific Language for scripting
- **NLP**: Natural language command parsing

**Scanner Enhancements:**
- **FastAPI Routes**: AST-based route discovery from source code
- **Router Prefixes**: Automatic prefix extraction from APIRouter()
- **Template Paths**: Track original template vs resolved path

**CLI Commands:**
- `rebuild accelerator`: Ultra-fast walk mode
- `rebuild auto-pr`: Automated PR creation
- `rebuild evolution`: Code evolution visualization
- `rebuild dsl`: DSL command execution
- `rebuild nlp`: Natural language parsing
- `rebuild mvp`: MVP protocol server
- `rebuild analyze vector-build`: Build semantic index
- `rebuild analyze vector-query`: Semantic search
- `rebuild analyze multi-repo`: Cross-repo analysis

**Infrastructure:**
- **Event Service**: Real-time event bus for SSE streaming
- **Config Loader**: Unified `rebuild.yaml` loading with CLI merge
- **Patcher Service**: Manual override application
- **Override Service**: Patch directory application
- **PR Service**: GitHub/GitLab PR automation
- **Summary Service**: AI summary generation

**Fixes:**
- **Safe Clone**: `walk` never creates files in original repo (removed auto-init)
- **Clone Isolation**: `clone_for_walk()` creates `.rebuild/repo/` for safe checkouts
- **Checkout Force**: `git checkout --force` for uncommitted changes
- **History Format**: `history_service` handles new `results.json` dict format
- **Replay Health**: Replay mode only checks health, doesn't `compose up`
- **Reload by Name**: `docker restart <name>` without compose project dependency

**Dependencies:**
- Added `sentence-transformers>=2.7` optional dependency (semantic)
- Updated `full` optional dependency to include semantic

## [0.1.13] - 2026-05-01

### Docs
- Update README.md

### Other
- Update .rebuild_c2004_test/2026-04-30/results.json
- Update .rebuild_c2004_test/2026-04-30/results.toon
- Update .rebuild_c2004_test/2026-04-30/results.yaml
- Update .rebuild_c2004_test/history.json
- Update .rebuild_c2004_test/history.jsonl
- Update .rebuild_c2004_test/index.html
- Update .rebuild_c2004_test/walk_state.json
- Update architecture.html
- Update infra-map.json

## [0.1.12] - 2026-05-01

### Docs
- Update README.md
- Update docs/case_study_c2004.md
- Update docs/img/c2004_dashboard.png
- Update docs/img/c2004_duplication.png
- Update docs/img/c2004_graph.png
- Update docs/img/c2004_tasks.png

### Test
- Update tests/test_deploy_service.py
- Update tests/test_models.py
- Update tests/test_reporter_service.py

### Other
- Update architecture.html
- Update rebuild/application/pipeline.py
- Update rebuild/application/services/deploy_service.py
- Update rebuild/application/services/history_service.py
- Update rebuild/application/services/reporter_service.py
- Update rebuild/application/services/scanner_service.py
- Update rebuild/application/services/test_service.py
- Update rebuild/domain/day_result.py
- Update rebuild/domain/models.py
- Update rebuild/interfaces/cli.py
- ... and 1 more files

## [0.1.11] - 2026-05-01

### Docs
- Update CHANGELOG.md
- Update README.md
- Update TODO.md
- Update docs/usage.md

### Test
- Update tests/test_pipeline.py

### Other
- Update .rebuild_ev/2026-05-01/commit.txt
- Update .rebuild_ev/2026-05-01/endpoints.json
- Update .rebuild_ev/2026-05-01/results.json
- Update .rebuild_ev/history.jsonl
- Update .rebuild_ev/index.html
- Update .rebuild_inc/2026-05-01/commit.txt
- Update .rebuild_inc/2026-05-01/endpoints.json
- Update .rebuild_inc/2026-05-01/results.json
- Update .rebuild_inc/history.jsonl
- Update .rebuild_inc/index.html
- ... and 7 more files


## [0.1.10] - 2026-05-01
### 🔥 Major: Code Evolution Intelligence Engine
- **Intelligence Layer**: Added AST-based duplication detection, Service Dependency Graphs, and Git Truth Ranking.
- **Decision Engine**: Introduced `reactor` command group for automated Refactor Planning and Execution.
- **AI Integration**: Integrated **LiteLLM** (via OpenRouter) for AI-powered refactor summaries and automated PR generation.
- **Event Sourcing**: Implemented append-only `history.jsonl` to track all pipeline actions (Audit Log).
- **Architecture**: Refactored to a strict 5-layer design with **CQRS** (Commands/Queries) and **Infrastructure Adapters**.

### ⚡ Added
- `rebuild init`: Automated project bootstrapping with `rebuild.yaml` and `.env`.
- `rebuild analyze graph --export`: Interactive D3.js architecture visualization.
- `rebuild walk --incremental`: Performance optimization to skip processed commits.
- **Multi-Language Support**: Duplication detection now supports **JS/TS/JSX/TSX** files.

### 🛡️ Fixed & Improved
- **Docker Isolation**: Enhanced with unique project names (`-p`) and volume cleanup (`-v`).
- **Resilient Probing**: `HttpAdapter` with exponential backoff for health checks.
- **Unified CLI**: Simplified command structure with `analyze` and `refactor` subcommands.

## [0.1.9] - 2026-04-30
### Added
- Layered architecture: `interfaces/`, `application/`, `domain/`.
- `HistoryService` for results management.
- Standardized `Service` protocol for all pipeline steps.

## [0.1.0] - 2026-04-15
- Initial release as `rebuild` deployment tool.
[Unreleased]: https://github.com/semcod/resplit/compare/v0.1.23...HEAD
[0.1.23]: https://github.com/semcod/resplit/compare/v0.1.22...v0.1.23
[0.1.22]: https://github.com/semcod/resplit/compare/v0.1.21...v0.1.22
[0.1.21]: https://github.com/semcod/resplit/compare/v0.1.20...v0.1.21
[0.1.20]: https://github.com/semcod/resplit/compare/v0.1.19...v0.1.20
[0.1.19]: https://github.com/semcod/resplit/compare/v0.1.18...v0.1.19
[0.1.18]: https://github.com/semcod/resplit/compare/v0.1.17...v0.1.18
[0.1.17]: https://github.com/semcod/resplit/compare/v0.1.16...v0.1.17
[0.1.16]: https://github.com/semcod/resplit/compare/v0.1.15...v0.1.16
[0.1.15]: https://github.com/semcod/resplit/compare/v0.1.14...v0.1.15
[0.1.14]: https://github.com/semcod/resplit/compare/v0.1.13...v0.1.14
[0.1.13]: https://github.com/semcod/resplit/compare/v0.1.12...v0.1.13
[0.1.12]: https://github.com/semcod/resplit/compare/v0.1.11...v0.1.12
[0.1.11]: https://github.com/semcod/resplit/compare/v0.1.10...v0.1.11
[0.1.10]: https://github.com/semcod/resplit/compare/v0.1.9...v0.1.10
[0.1.9]: https://github.com/semcod/resplit/compare/v0.1.0...v0.1.9
[0.1.0]: https://github.com/semcod/resplit/releases/tag/v0.1.0
[0.1.37]: https://github.com/semcod/resplit/compare/v0.1.37...v0.1.37
[0.1.38]: https://github.com/semcod/resplit/compare/v0.1.38...v0.1.38
[0.1.39]: https://github.com/semcod/resplit/compare/v0.1.39...v0.1.39
[0.1.40]: https://github.com/semcod/resplit/compare/v0.1.40...v0.1.40
