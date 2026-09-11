# Save agent output to a timestamped markdown file.

from datetime import datetime
from pathlib import Path


def save_output(content: str, prefix: str = "result") -> str:
    """Save text content to a timestamped markdown file under outputs/. Returns the path."""
    outputs_dir = Path("outputs")
    outputs_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = outputs_dir / f"{prefix}_{timestamp}.md"
    filepath.write_text(content, encoding="utf-8")
    return str(filepath)