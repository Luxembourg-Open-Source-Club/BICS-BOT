import nextcord
from nextcord import application_command
from nextcord.ext import commands

from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID


class BotDevCmd(commands.Cog):
    """This class represents the command /botdev"""

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Get the role of BotDev",
    )
    async def botdev(self, interaction: nextcord.Interaction):
        user = interaction.user
        user_roles = user.roles
        # Retrive the Gamer role object
        role = nextcord.utils.get(interaction.guild.roles, name="BotDev")

        if len(user_roles) == 1:
            # The user has no roles. So he must first use the /intro command
            await interaction.response.send_message(
                f"You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )
        elif role in user_roles:
            # The user wants to remove the role
            await interaction.response.send_message(
                f"The role BotDev has been removed",
                ephemeral=True,
            )
            await user.remove_roles(role)
        else:
            # The user wants to have the role Gamer
            await user.add_roles(role)
            await interaction.response.send_message(
                f"You now have the BotDev role!",
                ephemeral=True,
            )


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(BotDevCmd(client))
