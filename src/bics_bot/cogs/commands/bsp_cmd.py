from nextcord import application_command, Interaction
from nextcord.ext import commands

from bics_bot.embeds.bsp_embed import BspEmbed


class BspCmd(commands.Cog):
    """This class represents the command </bsp>

    The </bsp> command will send a message back with a list of relevant links for BSP

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        description="List of useful links for BSP",
    )
    async def bsp(self, interaction: Interaction):
        """
        This method represents the </bsp> command which sends a message
        with a list of relevant links for BSP

        Args:
            interaction: Required by the API. Gives meta information about
              the interaction.
        """
        await interaction.response.send_message(
            embed=BspEmbed(), ephemeral=True
        )


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(BspCmd(client))
