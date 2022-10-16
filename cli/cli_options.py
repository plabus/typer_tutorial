from typing import Any, Dict, Optional

from rich import print
import typer

__version__ = "0.0.1"

custom_kwargs: Dict[str, Any] = {
    "rich_help_panel": "Greeting Options",
}


def version_callback(display_version: bool):
    if display_version:
        print(f"cli_options: version {__version__}")
        # Make sure to "raise" an `Exit()` exception here, to terminate the program
        raise typer.Exit()


def validate_lastname(
    # typer specific parameters (order, name, and appearance does not matter)
    context: typer.Context,  # access to underlying `click.Context`
    param: typer.CallbackParam,  # parameter dict of the caller
    # the actual parameter; need to be returned
    lastname: str,
) -> None:
    # Needed in order not to break shell completion
    if context.resilient_parsing:
        return

    # Get a dict with all key-value pairs associated with `Option`/`Argument`
    print(param.to_info_dict())

    if lastname == "Foo":
        print("You're kidding, right?!")
    return lastname


def main(
    name: str = typer.Argument(..., show_default=False),
    lastname: str = typer.Option(
        # Required vs optional:
        ...,  # `...` as first parameter makes `typer.Option` a required CLI option
        # Custom long and short names:
        "--surname",  # alternative CLI option name
        "--lastname",  # ...or even several aliases
        "-l",  # short (combinable) option alias
        "-last",  # ...or even multiple
        # Documentation:
        help="The lastname of the user",
        show_default=False,
        # Prompt for missing values:
        prompt="Please enter your lastname",  # prompt for missing value (bool/str)
        confirmation_prompt=True,  # confirm the value entered in first prompt
        hide_input=True,  # hide input (e.g. for a password)
        # Using callbacks (e.g. for validation):
        callback=validate_lastname,
        # Passing custom `kwargs`:
        **custom_kwargs,
    ),
    formal: bool = typer.Option(
        False, help="Greet in a formal way", show_default=False, **custom_kwargs
    ),
    # Version: use a callback to display version of CLI
    display_version: Optional[bool] = typer.Option(
        False,
        "--version",
        "-V",
        help="Display the current version of the program",
        callback=version_callback,
        is_eager=True,  # make sure to process this _before_ any other parameters
    ),
) -> None:
    if formal:
        if lastname:
            print(f"Good day Mr. {lastname}!")
        else:
            print("Hello good sir!")
    else:
        print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
