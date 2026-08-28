from src.jobhunt_agent.agent import run_agent

answer = run_agent(
    "Fetch the job posting at sample_data/job_example.txt and tell me what "
    "programming languages or frameworks it mentions."
)
print(answer)