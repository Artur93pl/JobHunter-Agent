# Score how well a CV fits a job posting, using a single Claude prompt.

import json

from src.jobhunt_agent.llm_client import get_client, MODEL

PROMPT_TEMPLATE = """You are helping a job seeker understand how well their CV matches a job posting.

CV:
{cv_text}

JOB POSTING:
{job_text}

Compare the CV against the job posting and respond with ONLY a JSON object \
(no other text, no markdown code fences) in exactly this shape:

{{
  "score": <integer 0-100, how well the CV fits this job>,
  "reasons": ["<reason 1>", "<reason 2>", "<reason 3>"]
}}
"""


def score_fit(cv_text: str, job_text: str) -> dict:
    """
    Ask Claude to score how well a CV fits a job posting.

    Returns:
        A dict with keys "score" (int, 0-100) and "reasons" (list of 3 strings).
    """
    client = get_client()
    prompt = PROMPT_TEMPLATE.format(cv_text=cv_text, job_text=job_text)

    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    raw_text = response.content[0].text.strip()

    # Claude sometimes wraps JSON in ```json ... ``` even when told not to -
    # strip that off if present, so json.loads() doesn't choke on it.
    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
        raw_text = raw_text.strip()

    return json.loads(raw_text)