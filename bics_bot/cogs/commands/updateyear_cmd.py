import nextcord
from nextcord.ext import commands
from nextcord import application_command

from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID, ROLE_YEAR1_ID, ROLE_YEAR2_ID, ROLE_YEAR3_ID, ROLE_ALUMNI_ID
class UpdateYearCmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID,
                   GUILD_BICS_CLONE_ID], description="Update your year from 1->2, etc."
    )
    async def update(self, interaction:nextcord.Interaction):
        user = interaction.user
        for role in user.roles:
            if role.name == "Incoming":
                await user.remove_roles(role)
                await user.add_roles(interaction.guild.get_role(ROLE_YEAR1_ID))
            elif role.name == "Year 1":
                await user.remove_roles(role)
                await user.add_roles(interaction.guild.get_role(ROLE_YEAR2_ID))
            elif role.name == "Year 2":
                await user.remove_roles(role)
                await user.add_roles(interaction.guild.get_role(ROLE_YEAR3_ID))
            elif role.name == "Year 3":
                await user.remove_roles(role)
                await user.add_roles(interaction.guild.get_role(ROLE_ALUMNI_ID))

def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(UpdateYearCmd(client))