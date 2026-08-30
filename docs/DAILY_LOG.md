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


### Day 6 — 24 Aug 2026
Built fit_scorer.py: a single prompt that sends CV + job text to Claude and gets back a structured JSON fit score (0-100) plus 3 reasons.
Learned about prompt templates, asking for JSON-only output, and defensively stripping markdown code fences since models don't always follow formatting instructions perfectly.
First test: score 65 with specific, accurate reasoning about missing Git experience.


### Day 7 — 25 Aug 2026
Built cli.py with click: `python cli.py score --cv ... --job ...` now runs the whole pipeline end-to-end from the command line.
This is the MVP - a real, usable tool, not just a script I edit and re-run in PyCharm.
Hit a Windows quirk where plain `python` in PowerShell triggered the Microsoft Store stub instead of running the real interpreter - fixed by calling the full path directly.


### Day 8 — 26 Aug 2026
Built agent.py: the core tool-calling agent loop.
Claude can now request to run a Python tool mid-conversation, our code executes it and feeds the result back, and this repeats until Claude has a final answer.
Proved it works with a throwaway count_words tool - asked it to count words in a sentence and it called the tool and got the exact right answer (9), rather than guessing.
This is the foundation every remaining feature (fetch_job_posting, keyword_gap_analysis, draft_cover_letter) will plug into as real tools.


### Day 9 — 27 Aug 2026
Replaced the Day 8 demo tool with the first real one: fetch_job_posting, reusing job_loader.load_job() as the underlying function.
Also added a try/except around tool execution so network/file errors get reported back to Claude instead of crashing the program.
Tested by asking the agent to read a local job posting and summarize the tech stack mentioned - it correctly separated required vs "nice to have" skills.


### Day 10 — 30 Aug 2026
Added read_cv as a second real tool, wrapping cv_loader.load_cv() the same way fetch_job_posting wraps job_loader.
Confirmed the agent can call multiple tools in sequence within one conversation.
Added keyword_gap_analysis: a new tool (not just wrapping existing code) that compares CV text against job text using a curated list of common skill keywords, returning matched vs missing skills.
Tested by asking the agent to read both files and report the gap - it correctly chained all three tools (read_cv, fetch_job_posting, keyword_gap_analysis) in one go and produced a clear, well-organized answer with recommendations.
This is the first time the agent's genuine multi-step reasoning was visible, not just one tool call.