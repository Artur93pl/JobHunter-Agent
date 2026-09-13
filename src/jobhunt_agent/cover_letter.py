# Draft a tailored cover letter paragraph using Claude, based on a CV and job posting.

from src.jobhunt_agent.llm_client import MODEL, get_client

PROMPT_TEMPLATE = """Write a single, tailored cover letter paragraph (3-5 sentences) \
for this candidate applying to this job. Be specific - reference real details from \
both the CV and the job posting. Avoid generic filler phrases like "I am excited to \
apply". Write in first person, as the candidate.

CV:
{cv_text}

JOB POSTING:
{job_text}
"""


def draft_cover_letter(cv_text: str, job_text: str) -> str:
    """Ask Claude to draft one tailored cover-letter paragraph."""
    client = get_client()
    prompt = PROMPT_TEMPLATE.format(cv_text=cv_text, job_text=job_text)

    response = client.messages.create(
        model=MODEL,
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text