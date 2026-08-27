from src.jobhunt_agent.agent import run_agent

answer = run_agent(
    "How many words are in this sentence: 'The quick brown fox jumps over the lazy dog'?"
)
print(answer)