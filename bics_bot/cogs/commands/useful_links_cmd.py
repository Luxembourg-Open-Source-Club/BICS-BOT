from nextcord import application_command, Interaction
from nextcord.ext import commands

from bics_bot.embeds.useful_links_embed import UsefulLinksEmbed
from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID


class UsefulLinksCmd(commands.Cog):
    """This class represents the command </useful_links>

    The </useful_links> command will send a message back with a list of some of
    the most used links for BICS.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Links that might be useful",
    )
    async def useful_links(self, interaction: Interaction):
        """
        This method represents the </useful_links> command which sends a
        message with a list of some ofthe most used links for BICS.

        Args:
            interaction: Required by the API. Gives meta information about
              the interaction.
        """
        await interaction.response.send_message(
            embed=UsefulLinksEmbed(), ephemeral=True
        )


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(UsefulLinksCmd(client))
