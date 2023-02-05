import nextcord
from nextcord import application_command
from nextcord.ext import commands

from bics_bot.embeds.useful_links_embed import Useful_links
from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID


class UsefulLinksCmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Links that might be useful",
    )
    async def useful_links(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(embed=Useful_links(), ephemeral=True)


def setup(client):
    client.add_cog(UsefulLinksCmd(client))
