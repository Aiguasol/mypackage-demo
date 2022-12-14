from typing import Optional

import cowsay
import typer

from mypackage.config import SettingsModeEnum, settings

app = typer.Typer()

@app.command()
def greet(name: str = typer.Argument("person")):
    typer.echo(cowsay.cow(name))

@app.command()
def print_settings():
    color = typer.colors.BLUE
    bold = False

    for k, v in settings:
        if isinstance(v, list):
            typer.secho(f"{k}:", color=color, bold=bold)
            for e in v:
                typer.secho(f"\t{e}", color=color, bold=bold)
        else:
            typer.secho(f"{k}: {v}", color=color, bold=bold)


if __name__ == "__main__":
    app()
