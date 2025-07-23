import typer
import click
import click_repl
from auth import authenticate_user
from vault import add_password, get_password, delete_password, edit_service, list_services

# Initialize Typer app
app = typer.Typer(help="Password Manager CLI - manage your passwords securely")

# CLI commands for managing passwords: add, get, delete, edit, list services, show commands, and start interactive REPL


@app.command("add", help="Add credentials (username and password) for a service.")
def add(service: str, username: str, password: str):
    add_password(service, username, password)


@app.command("get", help="Retrieve credentials for a service.")
def get(service: str):
    get_password(service)


@app.command("delete", help="Delete credentials for a service.")
def delete(service: str):
    delete_password(service)


@app.command("edit", help="Edit credentials (username and/or password) for a service.")
def edit(service: str, username: str = None, password: str = None):
    edit_service(service, username, password)


@app.command("services", help="List all the stored credentials")
def services():
    list_services()


@app.command("commands", help="List all commands with short descriptions.")
def commands():
    typer.echo("Available commands:")
    for cmd in app.registered_commands:
        if cmd.name in ("repl", "commands"):
            continue
        typer.echo(f"  {cmd.name} - {cmd.help}")
    typer.echo("Type '<command> --help' for more info.")


@app.command("repl", help="Interactive cli for the password manager")
def myrepl():
    cli = typer.main.get_command(app)
    ctx = click.Context(cli)
    click_repl.repl(ctx)


if __name__ == '__main__':
    # Authentication with master password
    if not authenticate_user():
        typer.echo("Authentication failed.")
        raise typer.Exit(code=1)
    app()
