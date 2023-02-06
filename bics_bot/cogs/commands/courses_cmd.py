from nextcord.ext import commands
from nextcord import application_command
import nextcord

from bics_bot.dropdowns.course_selection_dropdown import DropdownView
from bics_bot.config.server_ids import GUILD_BICS_ID, ROLE_ADMIN_ID, ROLE_BOT_DEV_ID
from bics_bot.utils.channels_utils import retrieve_courses_text_channels_names


class CoursesCmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID],
        description="Courses Selection.",
    )
    async def courses(self, interaction: nextcord.Interaction):
        user = interaction.user
        guild = interaction.guild

        if len(user.roles) == 1:
            # Means the user only has the default @everyone role, and nothing else.
            await interaction.response.send_message(
                f"You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )
        else:
            if not user.get_role(ROLE_ADMIN_ID) and not user.get_role(ROLE_BOT_DEV_ID):
                await interaction.response.send_message(content="Sorry, this is not yet available for use :)", ephemeral=True)
            else:
                enrolled_courses = self.get_courses_enrolled(user, guild)
                view = DropdownView(enrolled_courses=enrolled_courses)
                disclaimer_message = """ATTENTION\n\nIf you do not make any new choices in a the dropdown menus, the courses that \"seem\" like they are chosen in that menu will be reset. If you do not want to lose access to those courses; go in that dropdown menu, and select, then unselect a course, so that your chosen courses are updated."""
                await interaction.response.send_message(content=disclaimer_message, view=view, ephemeral=True)

    def get_courses_enrolled(self, user: nextcord.Interaction.user, guild: nextcord.Guild) -> list[str]:
        enrolled = []
        channels = guild.text_channels
        for channel in channels:
            if channel.name in retrieve_courses_text_channels_names(guild) and user in channel.members:
                enrolled.append(channel.name)
        return enrolled


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(CoursesCmd(client))
