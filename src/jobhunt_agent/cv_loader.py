# Read a CV from a plain-text file and returns its content as a string

from pathlib import Path

def load_cv(path: str) -> str:
    """
       Read a CV file and return its text content.

       Args:
           path: path to a plain-text (.txt) CV file.

       Returns:
           The full text of the CV as a string.

       Raises:
           FileNotFoundError: if no file exists at the given path.
       """
    cv_path = Path(path)
    if not cv_path.exists():
        raise FileNotFoundError(f"No CV found at {path}")

    return cv_path.read_text(encoding="utf-8")
