import random
# from typing import Optional  # use if argument can be `None`

import typer


def get_default_name():
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])


def main(
    name: str = typer.Argument(
        # ...,  # `...` makes it required
        # None,  # makes it optional, but "without default"
        "Peter",  # setting a default
        # get_default_name,  # a default getter (mind the fct pointer)
        envvar="CLI_ENV_VAR",  # assign priority: default < env var < user
        show_envvar=True,  # whether to show in help or not
        help="The name of the user",  # argument help message
        show_default=True,  # either `True`/`False` or customize with string
        metavar="[USERNAME]",  # what to show in `Usage`
        rich_help_panel="Optional Arguments",  # customize the panel name
        hidden=False,  # set `True` to hide argument in help
    ),
):
    if name is None:
        print("Hello world!")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
