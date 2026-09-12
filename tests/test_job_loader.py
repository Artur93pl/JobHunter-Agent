import pytest

from src.jobhunt_agent.job_loader import load_job


def test_load_job_reads_local_file(tmp_path):
    job_file = tmp_path / "job.txt"
    job_file.write_text("Sample job posting", encoding="utf-8")

    assert load_job(str(job_file)) == "Sample job posting"


def test_load_job_missing_file_raises_error():
    with pytest.raises(FileNotFoundError):
        load_job("this_file_does_not_exist.txt")