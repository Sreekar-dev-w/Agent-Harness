import typer
from rich.console import Console

app = typer.Typer(
    name="localpilot",
    help="A local-first AI coding agent.",
    no_args_is_help=True,
)

console = Console()


@app.command()
def version():
    from localpilot import __version__
    console.print(f"[cyan]LOCALPILOT[/cyan] v{__version__}")


@app.command()
def doctor():
    console.print("[bold cyan]LOCALPILOT SYSTEM CHECK[/bold cyan]")
    console.print("[green]Python package initialized.[/green]")
    console.print("[yellow]Ollama integration: pending[/yellow]")
    console.print("[yellow]Model integration: pending[/yellow]")
