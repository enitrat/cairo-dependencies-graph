import sys
import os
import click
import traceback

from typing import List
from starkware.cairo.lang.version import __version__
from logic import generate_graph, print_version


@click.group()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def cli():
    pass

@click.command()
@click.option('--directory', '-d', help='Directory to analyze', required=True)
def dependencies_graph(directory: str):
    sys.exit(generate_graph(directory))


cli.add_command(dependencies_graph)


def main():
    cli()


if __name__ == "__main__":
    sys.exit(main())
