# The agent loop: lets Claude decide which tools to call and when.

from src.jobhunt_agent.cv_loader import load_cv
from src.jobhunt_agent.job_loader import load_job
from src.jobhunt_agent.keyword_gap import keyword_gap_analysis
from src.jobhunt_agent.llm_client import get_client, MODEL
from src.jobhunt_agent.cover_letter import draft_cover_letter
from src.jobhunt_agent.logging_config import setup_logging

logger = setup_logging()

# Maps a tool's name (as Claude refers to it) to the actual Python function that runs it.
AVAILABLE_TOOLS = {
    "fetch_job_posting": load_job,
    "read_cv": load_cv,
    "keyword_gap_analysis": keyword_gap_analysis,
    "draft_cover_letter": draft_cover_letter,
}

# Describes each tool to Claude: its name, what it does, and what input it expects.
TOOL_DEFINITIONS = [
    {
        "name": "fetch_job_posting",
        "description": (
            "Fetch the text of a job posting, given either a web URL or a local "
            "file path. Use this whenever you need to read a job posting's content."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "source": {
                    "type": "string",
                    "description": "A URL (http:// or https://) or a local file path.",
                }
            },
            "required": ["source"],
        },
    },
    {
        "name": "draft_cover_letter",
        "description": (
            "Draft a tailored cover letter paragraph for a candidate, based on "
            "their CV and a job posting. Use this once you have both texts and "
            "the user wants a cover letter."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "cv_text": {"type": "string", "description": "The full CV text."},
                "job_text": {"type": "string", "description": "The full job posting text."},
            },
            "required": ["cv_text", "job_text"],
        },
    },
    {
        "name": "read_cv",
        "description": "Read a CV from a local text file and return its content.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Local file path to a plain-text CV.",
                }
            },
            "required": ["path"],
        },
    },
    {
        "name": "keyword_gap_analysis",
        "description": (
            "Compare a CV's text against a job posting's text and report which "
            "common skill keywords appear in the job posting but seem to be "
            "missing from the CV. Use this after you have both texts."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "cv_text": {"type": "string", "description": "The full CV text."},
                "job_text": {"type": "string", "description": "The full job posting text."},
            },
            "required": ["cv_text", "job_text"],
        },
    },
]


def run_agent(user_message: str) -> str:
    """
    Send a message to Claude, letting it call tools as needed, and return its final answer.
    """
    client = get_client()
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=1000,
            tools=TOOL_DEFINITIONS,
            messages=messages,
        )

        if response.stop_reason != "tool_use":
            return response.content[0].text

        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                logger.info(f"Agent calling tool: {block.name} with input: {block.input}")
                tool_function = AVAILABLE_TOOLS[block.name]
                try:
                    result = tool_function(**block.input)
                except Exception as error:
                    logger.error(f"Tool {block.name} failed: {error}")
                    result = f"Error running tool: {error}"

                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result),
                    }
                )

        messages.append({"role": "user", "content": tool_results})