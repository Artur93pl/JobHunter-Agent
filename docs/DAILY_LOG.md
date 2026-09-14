# Daily Log

### Day 1 — 19 Aug 2026
Set up PyCharm project, git repo (private on GitHub), .gitignore, and a working hello-world script. 
Learned the create → stage → commit → push flow using both PyCharm UI and Git Bash.

### Day 2 — 20 Aug 2026
Built cv_loader.py: reads a plain-text CV file and returns its contents, with a clear error if the file doesn't exist. 
Tested manually via main.py against a sample CV. 
Learned about pathlib.
Path and why functions need arguments (hit a TypeError by forgetting to pass one — good lesson).


### Day 3 — 21 Aug 2026
Built job_loader.py: reads a job posting from either a local text file or a live URL (using requests + BeautifulSoup to strip HTML down to plain text).
Tested with a local sample file.
Hit a silly bug — named the test file job_example.text instead of .txt — good reminder to double-check filenames when debugging "file not found" errors.


### Day 4 — 22 Aug 2026
Wired up the Anthropic Claude API: created llm_client.py with get_client() and a say_hello() test call.
Set up .env (real key, git-ignored) and .env.example (placeholder, safe to commit). 
First successful live API call - got "Hello!" back from Claude. 
Learned about free trial credits and per-token pricing (Haiku 4.5: $1/$5 per million input/output tokens - genuinely cheap for this project's scale).


### Day 5 — 24 Aug 2026
Built fit_scorer.py: a single prompt that sends CV + job text to Claude and gets back a structured JSON fit score (0-100) plus 3 reasons.
Learned about prompt templates, asking for JSON-only output, and defensively stripping markdown code fences since models don't always follow formatting instructions perfectly.
First test: score 65 with specific, accurate reasoning about missing Git experience.


### Day 6 — 25 Aug 2026
Built cli.py with click: `python cli.py score --cv ... --job ...` now runs the whole pipeline end-to-end from the command line.
This is the MVP - a real, usable tool, not just a script I edit and re-run in PyCharm.
Hit a Windows quirk where plain `python` in PowerShell triggered the Microsoft Store stub instead of running the real interpreter - fixed by calling the full path directly.


### Day 7 — 26 Aug 2026
Built agent.py: the core tool-calling agent loop.
Claude can now request to run a Python tool mid-conversation, our code executes it and feeds the result back, and this repeats until Claude has a final answer.
Proved it works with a throwaway count_words tool - asked it to count words in a sentence and it called the tool and got the exact right answer (9), rather than guessing.
This is the foundation every remaining feature (fetch_job_posting, keyword_gap_analysis, draft_cover_letter) will plug into as real tools.


### Day 8 — 27 Aug 2026
Replaced the Day 8 demo tool with the first real one: fetch_job_posting, reusing job_loader.load_job() as the underlying function.
Also added a try/except around tool execution so network/file errors get reported back to Claude instead of crashing the program.
Tested by asking the agent to read a local job posting and summarize the tech stack mentioned - it correctly separated required vs "nice to have" skills.


### Day 9 — 30 Aug 2026
Added read_cv as a second real tool, wrapping cv_loader.load_cv() the same way fetch_job_posting wraps job_loader.
Confirmed the agent can call multiple tools in sequence within one conversation.
Added keyword_gap_analysis: a new tool (not just wrapping existing code) that compares CV text against job text using a curated list of common skill keywords, returning matched vs missing skills.
Tested by asking the agent to read both files and report the gap - it correctly chained all three tools (read_cv, fetch_job_posting, keyword_gap_analysis) in one go and produced a clear, well-organized answer with recommendations.
This is the first time the agent's genuine multistep reasoning was visible, not just one tool call.


### Day 10 - 31 Aug 2026
Added the fourth and final planned tool, draft_cover_letter, which internally makes its own Claude call - a tool can itself be an AI-powered step, not just plain logic (like keyword_gap_analysis) or a file/URL wrapper (like the first two tools).
Manually tested the full four-tool pipeline (read_cv, fetch_job_posting, keyword_gap_analysis, draft_cover_letter) against a brand-new job posting (Graduate Software Engineer) the code had never seen, to check for real bugs rather than just re-running the same fixtures. Result: clean pass, no bugs found - correct skill gaps identified (Git, Docker, AWS, REST APIs, testing, CI/CD) and a genuinely tailored, specific cover letter paragraph produced.
All four tools chaining together in one agent conversation, decided entirely by Claude.


### Day 11 — 11 Sep 2026 
Added output_writer.py (saves agent results to timestamped markdown files under outputs/) and logging_config.py (logs to both console and logs/jobhunt_agent.log).
Wired logging into agent.py so every tool call gets recorded.
Added a real `analyze` CLI command that runs the full 4-tool agent and saves the result - closing a gap where the CLI only ever exposed the old single-shot scorer, not the actual agent.
Hit one bug: forgot to paste the new command into cli.py the first time, got "No such command 'analyze'" - fixed by adding it properly below the score command.
Confirmed both outputs/ and logs/ folders get created automatically and are git-ignored (may contain personal CV/job data).


### Day 12 — 12 Sep 2026
Added error handling to the CLI: score and analyze commands now catch exceptions and raise click.ClickException, giving clean "Error: ..." messages instead of raw Python tracebacks.
Set up pytest and wrote 6 tests: happy-path and missing-file cases for cv_loader and job_loader, a correctness check for keyword_gap_analysis, and a mocked test for the agent loop (using unittest.mock.patch to fake the Claude API client, so the test runs free and instantly rather than making a real paid call).
All 6 tests pass.

### Day 13 — 13 Sep 2026
Added a GitHub Actions workflow so tests run automatically on every push.
Set up `ruff` for linting, learned the recurring Windows PATH issue firsthand (console scripts installed by pip aren't automatically on PATH) and fixed it properly by adding Python's Scripts folder to my system PATH, instead of routing around it each time.
Packaged the project with `pyproject.toml` so it installs as a real command (`jobhunt score ...`) via `pip install -e .`. Finally extended the CV loader to read `.pdf` and `.docx` files (via `pypdf` and `python-docx`), not just plain text, since real CVs come in those formats.
Next: bug bash and edge-case fixes across the whole project.

### Day 14 — 14 Sep 2026
Run a bug bash across the project: added missing test coverage for the PDF/DOCX CV loading, then deliberately tried to break the CLI with bad inputs.
Found and fixed two real bugs — a mislabeled file (e.g. a PDF renamed to .txt) crashed with a raw Python encoding error instead of a clear message, and a broken job-posting URL leaked internal `requests` library internals to the user.
Both now raise clean, human-readable errors while still preserving the technical detail for debugging.
Learned that "the code works" and "the code fails gracefully" are different bars, and that deliberately trying to break your own tool surfaces real issues automated tests can miss.
Next: README rewrite and a demo recording.