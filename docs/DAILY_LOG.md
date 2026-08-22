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