from typing import List

import typer

valid_names = ["Peter", "Paul", "Rick", "Mike"]


def tab_complete_names(
    incomplete: str,  # text already typed; need to be `str`, _independent_ of param type!
    context: typer.Context,  # we can use the `context` to get pre-existing values
    # args: List[str],  # we could even get a list of all "raw" CLI parameters
) -> str:  # `Zsh`, `Fish` and `Powershell`: may yield `Tuple[str, str]` (with help)
    current_names = context.params.get("name") or []
    for name in valid_names:
        if name.startswith(incomplete) and name not in current_names:
            yield name


def main(
    name: List[str] = typer.Option(
        ["Richard"],
        help="The name to say hi to.",
        autocompletion=tab_complete_names,
    )
):
    for n in name:
        print(f"Hello {n}")


if __name__ == "__main__":
    typer.run(main)
