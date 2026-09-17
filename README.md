# JobHunt Agent

A command-line AI agent that helps job seekers understand how well their CV
matches a job posting, and drafts a tailored cover letter — built with the
Claude API.

## Why I built this

I'm a final-year BSc Computing student moving into software development
after several years in hospitality. I wanted a portfolio project that was more than
a tutorial follow-along: something with a CLI, real error handling, tests, a
CI pipeline, and packaging — the kind of things a junior developer job
actually expects, not just "a script that works on my machine."

## Features

- **Fit scoring** — compares a CV against a job posting and returns a
  score out of 100 with reasons, using the Claude API.
- **Agentic analysis** — a tool-calling agent that can fetch a job posting
  from a URL, read a CV, run a keyword gap analysis, and draft a cover
  letter, deciding for itself which tools to call and in what order.
- **Multiple CV formats** — reads `.txt`, `.pdf`, and `.docx` CVs.
- **Job postings from anywhere** — pass a local text file or a live URL.
- **Friendly errors** — bad file paths, corrupted files, and unreachable
  URLs all produce clear messages instead of raw Python tracebacks.
- **Tested and linted** — pytest test suite, ruff linting, and a GitHub
  Actions CI pipeline that runs the tests on every push.
- **Installable as a real command** — `pip install -e .` gives you a
  `jobhunt` command, not just a script to run with `python`.

## How it works

`cli.py` is the entry point (built with [Click](https://click.palletsprojects.com)).
The `score` command does a single-shot comparison between a CV and a job
posting. The `analyze` command hands control to an agent (`src/jobhunt_agent/agent.py`)
that runs a tool-calling loop against the Claude API: Claude decides which
of four tools to call (`fetch_job_posting`, `read_cv`, `keyword_gap_analysis`,
`draft_cover_letter`), the results are fed back into the conversation, and
this repeats until Claude has enough information to respond.

## Installation

```bash
git clone https://github.com/Artur93pl/JobHunter-Agent.git
cd JobHunter-Agent
pip install -e .
```

Copy `.env.example` to `.env` and add your own Anthropic API key:


## Usage

Score a CV against a job posting:

```bash
jobhunt score --cv path/to/cv.pdf --job path/to/job_posting.txt
```

Run the full agent (fetches a live job posting, runs a skill-gap analysis, and drafts a tailored cover letter, saved to a file):

```bash
jobhunt analyze --cv path/to/cv.pdf --job https://example.com/job-posting
```

## Running tests

```bash
pytest
ruff check .
```

## Tech stack

- Python 3.12
- [Anthropic Claude API](https://docs.claude.com) — fit scoring, cover letter drafting, agentic tool use
- Click — CLI framework
- pypdf / python-docx — CV parsing
- requests / BeautifulSoup — job posting fetching
- pytest — testing
- ruff — linting
- GitHub Actions — CI

## Project structure

JobHunter-Agent/
├── cli.py # CLI entry point
├── src/jobhunt_agent/
│ ├── agent.py # tool-calling agent loop
│ ├── cv_loader.py # reads .txt / .pdf / .docx CVs
│ ├── job_loader.py # reads job postings from file or URL
│ ├── fit_scorer.py # single-shot CV/job fit scoring
│ ├── keyword_gap.py # skill keyword matching
│ ├── cover_letter.py # cover letter drafting
│ ├── llm_client.py # Claude API client setup
│ ├── output_writer.py # saves agent output to file
│ └── logging_config.py # logging setup
├── tests/ # pytest test suite
├── sample_data/ # example CVs and job postings
└── .github/workflows/tests.yml # CI pipeline


## Status

Built as a portfolio project over 15 coding sessions, each one pushed to
GitHub (some sessions covered more ground than others). See
[docs/DAILY_LOG.md](docs/DAILY_LOG.md) for a day-by-day build log, and
[CHANGELOG.md](CHANGELOG.md) for a summary of what shipped when.

## Demo

<video src="docs/demo.mp4" controls width="700"></video>