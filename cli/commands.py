import typer
from rich.console import Console
from rich.markdown import Markdown

__version__ = "0.1.5"

app = typer.Typer(
    # help="Little CLI app to learn typer",
    rich_markup_mode="markdown",  # "rich" for rich's Markup Language
    epilog="Made with :heart: in **Typer**",
)
app_name = "CLI app"


def markdown_print(obj: str) -> None:
    console = Console()
    obj = Markdown(obj)
    console.print(obj)


def print_version(do_print_version: bool) -> None:
    if do_print_version:
        print(f"{app_name} version {__version__}")
        raise typer.Exit()


@app.callback(
    invoke_without_command=False,  # if `True` call even without specifying a command
)
def app_main(
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        callback=print_version,
        is_eager=True,
    ),
) -> None:
    """Little CLI app to learn typer.

    It has several commands already:

    * create

    * delete

    ...and more :heart:!
    """


@app.command("create")
def create_command(username: str = typer.Argument("Peter Labus")):
    """**Create** a user `username` for the DB... :sparkles:

    * create a new user

    * print to console
    """
    print("Creating user: Peter Labus")


@app.command(help="Overwrite delete docstring.")
def delete():
    """**Delete** a user in the DB.

    This will delete a fixed user.
    """
    print("Deleting user: Peter Labus")


@app.command(deprecated=True)
def delete_all():
    """**Delete _all_** users in the DB."""
    markdown_print("Deleting _all_ users")


@app.command(
    # Use what parsing additional (unknown) arguments/options
    context_settings={"ignore_unknown_options": True, "allow_extra_args": True},
)
def extra(
    ctx: typer.Context,
    an_option: str = typer.Option("", "--op"),
):
    if an_option:
        print(an_option)
    for arg in ctx.args:  # list of raw strings for both options and arguments
        print(arg)


@app.command(rich_help_panel="Configuration")
def config():
    pass


@app.command(rich_help_panel="Configuration")
def path_to_config_file():
    pass


if __name__ == "__main__":
    app()
