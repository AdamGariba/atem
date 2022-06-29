import click

from atem.services.service_watchlist import WatchList

class Context:
    def __init__(self):
        self.watchlist_handler = WatchList()

@click.command()
@click.pass_context
def cli(ctx):
    ctx.obj = Context()
    ctx.obj.watchlist_handler.getWatchList()
