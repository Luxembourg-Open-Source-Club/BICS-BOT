from nextcord.ext import commands
from nextcord import application_command
import nextcord

from bics_bot.dropdowns.course_selection_dropdown import CoursesDropdownView
from bics_bot.config.server_ids import (
    GUILD_BICS_ID,
    ROLE_ADMIN_ID,
    ROLE_BOT_DEV_ID,
    ROLE_YEAR3_ID,
)
from bics_bot.embeds.courses_embed import CoursesEmbed
from bics_bot.utils.channels_utils import retrieve_courses_text_channels_names
from bics_bot.utils.file_manipulation import read_txt


class CoursesCmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID],
        description="Courses Selection.",
    )
    async def enroll(self, interaction: nextcord.Interaction):
        user = interaction.user
        guild = interaction.guild
        print(user.roles)

        if len(user.roles) == 1:
            # Means the user only has the default @everyone role, and nothing else.
            await interaction.response.send_message(
                f"You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )
        else:
            enrolled_courses = self.get_courses_enrolled(user, guild)
            view = CoursesDropdownView(enrolled_courses, True)
            await interaction.response.send_message(
                embed=CoursesEmbed(
                    "Enrollment Process",
                    read_txt("./bics_bot/texts/enrollment.txt"),
                ),
                view=view,
                ephemeral=True,
            )

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID],
        description="Courses Selection.",
    )
    async def unenroll(self, interaction: nextcord.Interaction):
        user = interaction.user
        guild = interaction.guild

        if len(user.roles) == 1:
            # Means the user only has the default @everyone role, and nothing else.
            await interaction.response.send_message(
                f"You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )
        else:
            enrolled_courses = self.get_courses_enrolled(user, guild)
            view = CoursesDropdownView(enrolled_courses, False)
            await interaction.response.send_message(
                embed=CoursesEmbed(
                    "Unenrollment Process",
                    read_txt("./bics_bot/texts/unrollment.txt"),
                ),
                view=view,
                ephemeral=True,
            )

    def get_courses_enrolled(
        self, user: nextcord.Interaction.user, guild: nextcord.Guild
    ) -> list[str]:
        enrolled = []
        channels = guild.text_channels
        for channel in channels:
            if (
                channel.name in retrieve_courses_text_channels_names(guild)
                and user in channel.members
            ):
                enrolled.append(channel.name)
        return enrolled


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(CoursesCmd(client))
