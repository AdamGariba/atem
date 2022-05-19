import click


import atem.config as config
from services.service_quote import Quote

q = Quote()


@click.command()
def cli():
    click.echo(q.random_quote())