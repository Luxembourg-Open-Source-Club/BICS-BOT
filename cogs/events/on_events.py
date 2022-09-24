import nextcord
from nextcord.ext import commands


class OnCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")


def setup(client):
    client.add_cog(OnCommands(client))
