# The agent loop: lets Claude decide which tools to call and when.

from src.jobhunt_agent.llm_client import get_client, MODEL


def count_words(text: str) -> int:
    """A tiny demo tool - counts words in a string. Proves the tool-calling loop works."""
    return len(text.split())


# Maps a tool's name (as Claude refers to it) to the actual Python function that runs it.
AVAILABLE_TOOLS = {
    "count_words": count_words,
}

# Describes each tool to Claude: its name, what it does, and what input it expects.
# This is how Claude "knows" the tool exists and when it might be useful.
TOOL_DEFINITIONS = [
    {
        "name": "count_words",
        "description": "Count the number of words in a piece of text.",
        "input_schema": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The text to count words in.",
                }
            },
            "required": ["text"],
        },
    }
]


def run_agent(user_message: str) -> str:
    """
    Send a message to Claude, letting it call tools as needed, and return its final answer.

    This is the core agent loop: Claude can ask to run a tool, we run it and hand back
    the result, and this repeats until Claude has enough information to give a final answer.
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
            # Claude has a final answer - no more tools needed.
            return response.content[0].text

        # Claude wants to use one or more tools. Add its request to the conversation.
        messages.append({"role": "assistant", "content": response.content})

        # Run each requested tool and collect the results.
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                tool_function = AVAILABLE_TOOLS[block.name]
                result = tool_function(**block.input)
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result),
                    }
                )

        # Send the tool results back to Claude as a new message, and loop again.
        messages.append({"role": "user", "content": tool_results})