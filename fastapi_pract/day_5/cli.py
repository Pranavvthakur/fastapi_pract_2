# cli.py
import typer

app = typer.Typer()

@app.command()

def hello(name: str = typer.Option(..., "--name", "-n", help="Your name")):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    app()
