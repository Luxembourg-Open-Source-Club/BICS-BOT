import nextcord
from nextcord import application_command, Interaction
from nextcord.ext import commands

from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID


class GamerCmd(commands.Cog):
    """This class represents the command </gamer>

    The </gamer> command allows users to either get or remove the role Gamer.
    It's main purpose is to give access to the games text channel.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Get the role of Gamer",
    )
    async def gamer(self, interaction: Interaction):
        """
        This method represents the </game> command which allows users to
        either get or remove the role Gamer. It's main purpose is to give
        access to the games text channel.

        Args:
            interaction: Required by the API. Gives meta information about
              the interaction.
        """
        user = interaction.user
        user_roles = user.roles
        server_roles = interaction.guild.roles

        # Retrive the Gamer role object
        role = nextcord.utils.get(server_roles, name="Gamer")

        if len(user_roles) == 1:
            # The user has no roles. So he must first use the /intro command
            await interaction.response.send_message(
                "You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )
        elif role in user_roles:
            # The user wants to remove the role
            await interaction.response.send_message(
                "The role Gamer has been removed",
                ephemeral=True,
            )
            await user.remove_roles(role)
        else:
            # The user wants to have the role Gamer
            await user.add_roles(role)
            await interaction.response.send_message(
                "You now have the Gamer role!",
                ephemeral=True,
            )


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(GamerCmd(client))
