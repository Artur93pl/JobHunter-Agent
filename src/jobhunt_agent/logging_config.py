# Central logging configuration for the JobHunt Agent.

import logging
from pathlib import Path


def setup_logging() -> logging.Logger:
    """Configure logging to both console and a log file, and return the logger."""
    Path("logs").mkdir(exist_ok=True)

    logger = logging.getLogger("jobhunt_agent")
    logger.setLevel(logging.INFO)

    if not logger.handlers:  # avoid duplicate log lines if this ever runs twice
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        file_handler = logging.FileHandler("logs/jobhunt_agent.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger