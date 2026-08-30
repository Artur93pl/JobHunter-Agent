# Compare a CV against a job posting to find likely skill gaps.

# A curated list of common tech/soft skills to look for. Not exhaustive - good
# enough for a first pass. Could be made smarter (e.g. with real NLP) later.
SKILL_KEYWORDS = [
    "python", "java", "c#", "javascript", "sql", "mysql", "postgresql",
    "django", "flask", "fastapi", "git", "github", "docker", "aws",
    "rest", "api", "html", "css", "linux", "agile", "scrum",
    "testing", "pytest", "ci/cd",
]


def keyword_gap_analysis(cv_text: str, job_text: str) -> dict:
    """
    Compare a CV against a job posting and report which known skill keywords
    appear in the job posting but seem to be missing from the CV.

    Returns:
        A dict with "matched" (skills in both) and "missing" (skills mentioned
        in the job posting but not found in the CV).
    """
    cv_lower = cv_text.lower()
    job_lower = job_text.lower()

    mentioned_in_job = [kw for kw in SKILL_KEYWORDS if kw in job_lower]
    matched = [kw for kw in mentioned_in_job if kw in cv_lower]
    missing = [kw for kw in mentioned_in_job if kw not in cv_lower]

    return {"matched": matched, "missing": missing}