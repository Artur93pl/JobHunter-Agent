from src.jobhunt_agent.keyword_gap import keyword_gap_analysis


def test_keyword_gap_finds_matched_and_missing_skills():
    cv_text = "Experienced in Python and SQL."
    job_text = "We need Python, Git, and Docker experience."

    result = keyword_gap_analysis(cv_text, job_text)

    assert "python" in result["matched"]
    assert "git" in result["missing"]
    assert "docker" in result["missing"]