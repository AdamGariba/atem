import click

import config

@click.command()
def cli():
    click.echo(config.QUOTE_API)