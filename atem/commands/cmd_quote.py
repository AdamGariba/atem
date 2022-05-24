import re
import click

from atem.services.service_quote import Quote

class Context:
    def __init__(self):
        self.quoteHandler = Quote()

@click.command()
@click.pass_context
def cli(ctx):
    ctx.obj = Context()
    result = ctx.obj.quoteHandler.randomQuote()
    click.echo(f'\"{result["quote"]}\"')
    click.echo(f'- {result["author"]}')