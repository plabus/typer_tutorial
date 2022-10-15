from inspect import cleandoc

import typer
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.table import Table

data = {
    "name": "Peter",
    "age": 35,
    "items": [{"name": "towel"}, {"name": "plumbus"}],
    "active": True,
    "affiliation": None,
}


def main():
    # printing complex data structures
    print("Printing structured data:")
    print(data)
    print()

    # printing with color, blink and emojis (here to `stderr`)
    print("Printing colored messages")
    error_console = Console(stderr=True)
    error_console.print(
        "[bold red]Maintenance in progress[/] [blink]:wrench::wrench::wrench:[/]"
    )
    print()

    # print a table to `Console` object
    print("Printing a table with rich:")
    table = Table("Name", "Item", "Age")
    table.add_row("Peter", "Portal Gun", "35")
    table.add_row("Rick", "Plumbus", "83")
    console = Console()
    console.print(table)
    print()

    # user prompts
    affiliation = Prompt.ask("What is your affiliation?")
    print(f"Your affiliation is {affiliation}")

    # markdown
    # can print any markdown on console with `python -m rich.markdown <file>`
    markdown_example = """\
        # This is an h1

        Rich can do a pretty *decent* job of rendering markdown.

        1. This is a list item
        2. This is another list item"""
    markdown = Markdown(cleandoc(markdown_example))
    console.print(markdown)


if __name__ == "__main__":
    typer.run(main)
