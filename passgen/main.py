import re
import secrets
import string

import typer

app = typer.Typer()


def check_length(value: int):
    if value <= 6:
        typer.confirm(
            "You are generating a short password. Are you sure about this?", abort=True
        )
    return value


@app.command()
def generate(
    length: int = typer.Option(16, callback=check_length),
    letters: bool = True,
    numbers: bool = True,
    symbols: bool = True,
    similar: bool = False,
):
    """
    Generate a secure password.
    """

    alpha: str = ""
    remove: str = ""

    if letters:
        alpha += string.ascii_letters
    if numbers:
        alpha += string.digits
    if symbols:
        alpha += string.punctuation
        remove += "\"'`|"
    if not similar:
        remove += "B8G6I1l0OQDS5Z2"

    alpha = re.sub(f"[{remove}]", "", alpha)  # Remove unwanted characters

    password = "".join(secrets.choice(alpha) for _ in range(length))
    typer.echo(password)


if __name__ == "__main__":
    app()
