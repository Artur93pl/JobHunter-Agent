# Changelog

A summary of what shipped in this project, commit by commit. For detailed
day-to-day build notes, see [docs/DAILY_LOG.md](docs/DAILY_LOG.md).

## Day 1 — Hello world test, `.gitignore` for PyCharm/Python clutter
## Day 2 — CV loader module
## Day 3 — Job posting fetcher/loader
## Day 4 — Wired up the Claude API client
## Day 5 — README and requirements.txt
## Day 6 — First working fit-score prompt
## Day 7 — CLI v1: `score` command works end-to-end
## Day 8 — Tool-calling agent loop skeleton
## Day 9 — `fetch_job_posting` tool
## Day 10 — `read_cv` and `keyword_gap_analysis` tools
## Day 11 — `draft_cover_letter` tool, full pipeline tested
## Day 12 — Saved outputs, `analyze` CLI command, logging
- Follow-up fix: stopped tracking `outputs/` and `logs/` (should have been git-ignored from the start)
## Day 13 — CLI error handling and pytest test suite
## Day 14 — CI workflow, ruff linting, `pyproject.toml` packaging, PDF/DOCX CV support
- Follow-up fix: install the package with `pip install -e .` in CI so tests can import `src`
## Day 15 — Bug bash: test coverage for PDF/DOCX loading, friendly errors for bad files and network failures
## Day 16 — README rewrite, fixed CLI help text to match actual PDF/DOCX support

## Ship day — 20 Sep 2026
- Repository made public
- Linked from LinkedIn and CV