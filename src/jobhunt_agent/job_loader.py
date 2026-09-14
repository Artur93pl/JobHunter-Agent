# Loads a job posting either from local text file or a live URL.

from pathlib import Path

import requests
from bs4 import BeautifulSoup


def load_job(source: str) -> str:
    """
    Load a job posting from either a URL or a local text file.

    Args:
        source: an http(s) URL, or a path to a local .txt file.

    Returns:
        The job posting text, cleaned up.

    Raises:
        FileNotFoundError: if source looks like a local path but doesn't exist.
        requests.HTTPError: if fetching the URL fails.
    """
    if source.startswith(("http://", "https://")):
        try:
            response = requests.get(source, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            raise ValueError(f"Could not fetch job posting from {source}: {error}") from error
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return "\n".join(lines)

    job_path = Path(source)
    if not job_path.exists():
        raise FileNotFoundError(f"No job posting found at: {source}")
    return job_path.read_text(encoding="utf-8")
