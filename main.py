from src.jobhunt_agent.cv_loader import load_cv
from src.jobhunt_agent.job_loader import load_job
from src.jobhunt_agent.fit_scorer import score_fit

cv_text = load_cv("sample_data/cv_example.txt")
job_text = load_job("sample_data/job_example.txt")

result = score_fit(cv_text, job_text)
print(result)