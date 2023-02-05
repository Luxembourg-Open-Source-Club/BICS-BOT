import nextcord
from nextcord import application_command
from nextcord.ext import commands

from bics_bot.embeds.help_embed import HelpEmbed
from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID


class HelpCmd(commands.Cog):
    """This class represents the command /help"""

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="List of available commands for the bics bot",
    )
    async def help(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(embed=HelpEmbed(), ephemeral=True)


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(HelpCmd(client))
