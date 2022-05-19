import os

import click

cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename[4:-3])
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"atem.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli



@click.command(cls=ComplexCLI)
def cli():
    """Hello! I am Atem!"""
    pass