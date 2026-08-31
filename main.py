from src.jobhunt_agent.agent import run_agent

answer = run_agent(
    "Read the CV at sample_data/cv_example.txt and the job posting at "
    "sample_data/job_example_2.txt. Tell me the skill gaps, then draft a "
    "tailored cover letter paragraph."
)
print(answer)