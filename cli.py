# Command-line interface for JobHunter Agent.

import click

from src.jobhunt_agent.cv_loader import load_cv
from src.jobhunt_agent.job_loader import load_job
from src.jobhunt_agent.fit_scorer import score_fit


@click.group()
def cli():
    """JobHunt Agent - AI-powered CV/job fit scoring."""
    pass


@cli.command()
@click.option("--cv", "cv_path", required=True, help="Path to your CV (.txt file).")
@click.option("--job", "job_path", required=True, help="Path to the job posting (.txt file or URL).")
def score(cv_path, job_path):
    """Score how well your CV fits a job posting."""
    cv_text = load_cv(cv_path)
    job_text = load_job(job_path)

    click.echo("Scoring your fit for this role...")
    result = score_fit(cv_text, job_text)

    click.echo(f"\nFit score: {result['score']}/100\n")
    click.echo("Reasons:")
    for reason in result["reasons"]:
        click.echo(f"  - {reason}")


if __name__ == "__main__":
    cli()