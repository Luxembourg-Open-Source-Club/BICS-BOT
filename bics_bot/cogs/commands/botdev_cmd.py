import nextcord
from nextcord import application_command, Interaction
from nextcord.ext import commands

from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID
from bics_bot.embeds.logger_embed import LoggerEmbed
from bics_bot.embeds.logger_embed import WARNING_LEVEL


class BotDevCmd(commands.Cog):
    """This class represents the command </botdev>

    The </botdev> command allows users to either get or remove the role BotDev.
    It's main purpose is to give access to specific text channels for the
    development of the bot

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Get the role of BotDev",
    )
    async def botdev(self, interaction: Interaction):
        """
        This method represents the </botdev> command which allows users to
        either get or remove the role BotDev. It's main purpose is to give
        access to specific text channels for the development of the bot.

        Args:
            interaction: Required by the API. Gives meta information about
              the interaction.
        """
        user = interaction.user
        user_roles = user.roles
        server_roles = interaction.guild.roles

        # Retrive the Gamer role object
        role = nextcord.utils.get(server_roles, name="BotDev")

        if len(user_roles) == 1:
            # The user has no roles. So he must first use the /intro command
            msg = "You haven't yet introduced yourself! Make sure you use the **/intro** command first"
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
            )
        elif role in user_roles:
            # The user wants to remove the role
            msg = "The role **BotDev** has been removed"
            await user.remove_roles(role)
            await interaction.response.send_message(
                embed=LoggerEmbed("Role Status", msg),
                ephemeral=True,
            )
        else:
            # The user wants to have the role Gamer
            msg = "The role **BotDev** has been removed"
            await user.add_roles(role)
            await interaction.response.send_message(
                embed=LoggerEmbed("Role Status", msg),
                ephemeral=True,
            )


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(BotDevCmd(client))
