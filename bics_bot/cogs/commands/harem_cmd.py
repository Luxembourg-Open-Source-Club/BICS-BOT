import nextcord
import sys
from nextcord import application_command
from nextcord.ext import commands

sys.path.append("../../")
from server_ids import *
from embeds.help_embed import Help_embed


class HaremCmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[BICS_GUILD_ID, BICS_CLONE_GUILD_ID],
        description="Get the role of harem",
    )
    async def gamer(self, interaction: nextcord.Interaction):
        user = interaction.user
        user_roles = user.roles
        role = nextcord.utils.get(interaction.guild.roles, name="Harem")

        if len(user_roles) == 1:
            # - Means the user already has at least one role
            await interaction.response.send_message(
                f"You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )
        elif role in user_roles:
            await interaction.response.send_message(
                f"The role Harem has been removed",
                ephemeral=True,
            )
            await user.remove_roles(role)
        else:
            await user.add_roles(role)
            await interaction.response.send_message(
                f"You now have the Harem role!",
                ephemeral=True,
            )


def setup(client):
    client.add_cog(HaremCmd(client))