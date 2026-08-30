from src.jobhunt_agent.agent import run_agent

answer = run_agent(
    "Read the CV at sample_data/cv_example.txt and the job posting at "
    "sample_data/job_example.txt, then tell me which skills the job "
    "requires that seem to be missing from the CV."
)
print(answer)