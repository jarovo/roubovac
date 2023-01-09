"""Console script for roubovac."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("roubovac")
    click.echo("=" * len("roubovac"))
    click.echo("Autografting git patches on top of the branch.")


if __name__ == "__main__":
    main()  # pragma: no cover
