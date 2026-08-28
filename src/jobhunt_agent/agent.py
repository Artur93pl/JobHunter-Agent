# The agent loop: lets Claude decide which tools to call and when.

from src.jobhunt_agent.job_loader import load_job
from src.jobhunt_agent.llm_client import get_client, MODEL


# Maps a tool's name (as Claude refers to it) to the actual Python function that runs it.
AVAILABLE_TOOLS = {
    "fetch_job_posting": load_job,
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
    }
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
                tool_function = AVAILABLE_TOOLS[block.name]
                try:
                    result = tool_function(**block.input)
                except Exception as error:
                    # If the tool fails (bad URL, missing file, network issue),
                    # tell Claude what went wrong instead of crashing the whole program.
                    result = f"Error running tool: {error}"

                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result),
                    }
                )

        messages.append({"role": "user", "content": tool_results})