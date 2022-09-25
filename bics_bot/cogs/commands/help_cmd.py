import nextcord
import sys
from nextcord import application_command
from nextcord.ext import commands

sys.path.append("../../")
from server_ids import *
from embeds.help_embed import Help_embed


class HelpCmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[BICS_GUILD_ID, BICS_CLONE_GUILD_ID], description="Introduce yourself"
    )
    async def help(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(embed=Help_embed(), ephemeral=True)


def setup(client):
    client.add_cog(HelpCmd(client))
