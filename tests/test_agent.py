from unittest.mock import MagicMock, patch

from src.jobhunt_agent.agent import run_agent


@patch("src.jobhunt_agent.agent.get_client")
def test_run_agent_returns_final_text_when_no_tool_needed(mock_get_client):
    mock_response = MagicMock()
    mock_response.stop_reason = "end_turn"
    mock_response.content = [MagicMock(text="Mocked answer")]

    mock_client = MagicMock()
    mock_client.messages.create.return_value = mock_response
    mock_get_client.return_value = mock_client

    result = run_agent("Any question")

    assert result == "Mocked answer"