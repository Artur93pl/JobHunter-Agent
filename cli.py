# Command-line interface for JobHunter Agent.

import click

from src.jobhunt_agent.agent import run_agent
from src.jobhunt_agent.cv_loader import load_cv
from src.jobhunt_agent.fit_scorer import score_fit
from src.jobhunt_agent.job_loader import load_job
from src.jobhunt_agent.output_writer import save_output


@click.group()
def cli():
    """JobHunt Agent - AI-powered CV/job fit scoring."""


@cli.command()
@click.option("--cv", required=True, help="Path to your CV (.txt, .pdf, or .docx file).")
@click.option("--job", "job_path", required=True, help="Path to the job posting (.txt file or URL).")
def score(cv_path, job_path):
    """Score how well your CV fits a job posting."""
    try:
        cv_text = load_cv(cv_path)
        job_text = load_job(job_path)
        click.echo("Scoring your fit for this role...")
        result = score_fit(cv_text, job_text)
    except Exception as error:
        raise click.ClickException(str(error))

    click.echo(f"\nFit score: {result['score']}/100\n")
    click.echo("Reasons:")
    for reason in result["reasons"]:
        click.echo(f"  - {reason}")

@cli.command()
@click.option("--cv", required=True, help="Path to your CV (.txt, .pdf, or .docx file).")
@click.option("--job", "job_path", required=True, help="Path to the job posting (.txt file or URL).")
def analyze(cv_path, job_path):
    """Run the full AI agent: skill gap analysis + tailored cover letter, saved to a file."""
    try:
        message = (
            f"Read the CV at {cv_path} and the job posting at {job_path}. "
            "Tell me the skill gaps, then draft a tailored cover letter paragraph."
        )
        click.echo("Running the agent - this may take a few seconds...")
        result = run_agent(message)
    except Exception as error:
        raise click.ClickException(str(error))


    click.echo("\n" + result + "\n")

    saved_path = save_output(result, prefix="analysis")
    click.echo(f"Saved full result to: {saved_path}")



if __name__ == "__main__":
    cli()