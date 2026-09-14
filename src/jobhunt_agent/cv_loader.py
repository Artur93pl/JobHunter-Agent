# Read a CV from a plain-text file and returns its content as a string

from pathlib import Path

from docx import Document
from pypdf import PdfReader


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

    suffix = cv_path.suffix.lower()

    if suffix == ".pdf":
        reader = PdfReader(cv_path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if suffix == ".docx":
        document = Document(cv_path)
        return "\n".join(paragraph.text for paragraph in document.paragraphs)
    try:
        return cv_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise ValueError(
            f"Could not read {path} as a text file. If this is a PDF or Word "
            "document, make sure it has a .pdf or .docx extension."
        ) from error
