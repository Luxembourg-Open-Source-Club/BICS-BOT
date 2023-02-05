import nextcord
from nextcord.ext import commands

from bics_bot.embeds.welcome_embed import WelcomeEmbed


class OnEvents(commands.Cog):
    """This class contains the events that should be triggered when they occur."""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """This event gets triggered once the bot is fully active."""
        print("Bot is online")

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        """This event gets triggered once some new users joins a guild where the bot is."""
        server_name = await self.client.fetch_guild(member.guild.id)
        server_name = server_name.name

        await member.send(embed=WelcomeEmbed(member.display_name, server_name))


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(OnEvents(client))
