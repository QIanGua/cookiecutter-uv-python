"""Command line interface for {{ cookiecutter.project_name }}."""

import typer

app = typer.Typer()


@app.command()
def main():
    """{{ cookiecutter.project_name }} - {{ cookiecutter.project_description }}"""
    typer.echo("Hello from {{ cookiecutter.project_name }}!")


if __name__ == "__main__":
    app()
