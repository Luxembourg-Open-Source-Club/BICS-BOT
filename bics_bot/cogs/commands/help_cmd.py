from nextcord import application_command, Interaction
from nextcord.ext import commands

from bics_bot.embeds.help_embed import HelpEmbed
from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID


class HelpCmd(commands.Cog):
    """This class represents the command </help>

    The </help> command will send a message back with a list of the bot's
    available commands.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="List of available commands for the bics bot",
    )
    async def help(self, interaction: Interaction):
        """
        This method represents the </help> command which sends a message
        with a list of the bot's available commands.

        Args:
            interaction: Required by the API. Gives meta information about
              the interaction.
        """
        await interaction.response.send_message(
            embed=HelpEmbed(), ephemeral=True
        )


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(HelpCmd(client))
