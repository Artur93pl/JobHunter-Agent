import pytest

from src.jobhunt_agent.cv_loader import load_cv


def test_load_cv_reads_file_content(tmp_path):
    cv_file = tmp_path / "cv.txt"
    cv_file.write_text("Sample CV content", encoding="utf-8")

    assert load_cv(str(cv_file)) == "Sample CV content"


def test_load_cv_missing_file_raises_error():
    with pytest.raises(FileNotFoundError):
        load_cv("this_file_does_not_exist.txt")