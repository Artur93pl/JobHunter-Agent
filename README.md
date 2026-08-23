# JobHunt Agent

A command-line AI agent (Python + Anthropic Claude API) that helps with job hunting: give it a CV and a job posting, and it scores your fit, finds keyword gaps, and drafts a tailored cover-letter paragraph — using Claude's tool-calling to work through the problem in actual agent steps, not one big prompt.

> Status: work in progress, built 19 Aug - 20 Sep 2026. See `ROADMAP.md` (coming later) and `docs/DAILY_LOG.md` for the day-by-day build notes.

## Why this project

I'm a Computing student aiming for a junior/entry-level Python role.
Rather than a tutorial project, I built something I actually use in my own job search, while learning API integration, agent/tool-calling design, and good software practices along the way.

## Getting started

```bash
git clone https://github.com/Artur93pl/JobHunter-Agent.git
cd JobHunter-Agent
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
cp .env.example .env           # then add your own ANTHROPIC_API_KEY
python main.py
```

## Tech stack

Python 3.12 · Anthropic Claude API (tool calling) · requests + BeautifulSoup · pytest (coming later)

## Project layout

```
src/jobhunt_agent/   application code (cv_loader, job_loader, llm_client, ...)
sample_data/         example CV/job files used for testing
docs/                daily build log
```