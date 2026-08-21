from src.jobhunt_agent.cv_loader import load_cv
from src.jobhunt_agent.job_loader import load_job


cv_text = load_cv("sample_data/cv_example.txt")
job_text = load_job("sample_data/job_example.txt")

print(cv_text)
print("---")
print(job_text)