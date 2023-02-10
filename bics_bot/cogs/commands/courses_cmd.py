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
    """
    This class represents the commands `/enroll` and `/unenroll`.
    
    The `/enroll` command is used for students who wish to get viewing 
    permissions to the text channels of their courses.

    The `/unenroll` command is used for students who wish to remove their 
    viewing permissions to the text channels of the courses they are no 
    longer taking.

    Attributes:
        client: Required by the API, not directly utilized.
    """
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID],
        description="Courses Selection.",
    )
    async def enroll(self, interaction: nextcord.Interaction) -> None:
        """
        The `/enroll` command is used for students who wish to get viewing 
        permissions to the text channels of their courses.

        This method will:
            
            1. Retrieve the courses the student is already enrolled to.
            
            2. Display a dropdown menu where they can make choices.
        
        Args:
            interaction: Required by the API. Gives meta information about 
              the interaction.
        Returns:
            None
        """
        user = interaction.user
        guild = interaction.guild
        print(user.roles)

        if len(user.roles) == 1:
            # Means the user only has the default @everyone role, and nothing else.
            await interaction.response.send_message(
                f"You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )
            return

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
    async def unenroll(self, interaction: nextcord.Interaction) -> None:
        """
        The `/unenroll` command is used for students who wish to remove their 
        viewing permissions to the text channels of the courses they are no 
        longer taking.

        This method will:
            
            1. Retrieve the courses the student is already enrolled to.
            2. Display a dropdown menu where they can make choices.
        
        Args:
            interaction: Required by the API. Gives meta information about 
              the interaction.
        Returns:
            None
        """
        user = interaction.user
        guild = interaction.guild

        if len(user.roles) == 1:
            # Means the user only has the default @everyone role, and nothing else.
            await interaction.response.send_message(
                f"You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )

        enrolled_courses = self.get_courses_enrolled(user, guild)
        view = CoursesDropdownView(enrolled_courses, False)
        await interaction.response.send_message(
            embed=CoursesEmbed(
                "Unenrollment Process",
                read_txt("./bics_bot/texts/unenrollment.txt"),
            ),
            view=view,
            ephemeral=True,
        )

    def get_courses_enrolled(
        self, user: nextcord.Interaction.user, guild: nextcord.Guild
    ) -> dict[str, bool]:
        """
        Retrieves the courses a student is enrolled to.
        
        Technically; will return the courses that the student can view it by 
        any means necessary (member level permission, role level permission, 
        admin rights).

        Args:
            user: the user who is doing the `/enroll` or `unenroll` request.
            guild: the server object, containing information on text channels 
              necessary for this opeation

        Returns:
            enrolled: a dictionary where the keys are the courses the 
              student can see
        """
        enrolled:dict[str, bool] = {}
        channels = guild.text_channels
        for channel in channels:
            if (
                channel.name in retrieve_courses_text_channels_names(guild)
                and user in channel.members
            ):
                enrolled[channel.name] = True
        return enrolled


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(CoursesCmd(client))
