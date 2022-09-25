import nextcord
from nextcord.ext import commands


class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(HelpCommand(client))
