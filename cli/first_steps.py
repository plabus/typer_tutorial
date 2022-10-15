import typer


def main(
    # CLI argument --- is required by default, order matters when using more than one
    name: str,
    # CLI option --- with empty default
    surname: str = "",
    # CLI option (aka. flag) --- has `--` by default, order does _not_ matter
    formal: bool = False,
):
    """Great NAME, optionally including his/her SURNAME.

    If --formal is used, the greeting will be more formal.
    """
    if formal:
        if surname:
            print(f"Good day Mr. {surname}!")
        else:
            print("Good day, good Sir!")
    else:
        print(f"Hi {name} {surname}")


if __name__ == "__main__":
    typer.run(main)
