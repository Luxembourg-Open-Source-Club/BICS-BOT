import nextcord
import sys
from nextcord import application_command
from nextcord.ext import commands

sys.path.append("../../")
from server_ids import *
from embeds.useful_links_embed import Useful_links


class UsefulLinksCmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[BICS_GUILD_ID, BICS_CLONE_GUILD_ID],
        description="Links that might be useful",
    )
    async def useful_links(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(embed=Useful_links(), ephemeral=True)


def setup(client):
    client.add_cog(UsefulLinksCmd(client))
