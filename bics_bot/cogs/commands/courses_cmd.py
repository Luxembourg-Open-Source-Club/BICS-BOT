import nextcord
from nextcord.ext import commands
from nextcord import application_command, Interaction, Guild

from bics_bot.dropdowns.course_selection_dropdown import CoursesDropdownView
from bics_bot.embeds.logger_embed import WARNING_LEVEL, LoggerEmbed
from bics_bot.utils.channels_utils import retrieve_courses_text_channels_names
from bics_bot.utils.file_manipulation import read_txt
from bics_bot.config.server_ids import GUILD_BICS_ID


class CoursesCmd(commands.Cog):
    """
    This class represents the commands </enroll> and </unenroll>.

    The </enroll> command is used for students who wish to get viewing
    permissions to the text channels of their courses.

    The </unenroll> command is used for students who wish to remove their
    viewing permissions to the text channels of the courses they are no
    longer taking.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID],
        description="Enrollment to courses text channels",
    )
    async def enroll(self, interaction: Interaction) -> None:
        """
        The </enroll> command is used for students who wish to get viewing
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

        if len(user.roles) == 1:
            # The user has no roles. So he must first use the /intro command
            msg = (
                "You haven't yet introduced yourself! Make sure you use the **/intro** command first",
            )
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
            )
            return

        if nextcord.utils.get(user.roles, "Incoming"):
            # The user has the incoming role and thus not allowed to enroll
            msg = ("You are not allowed to enroll to courses yet!",)
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
            )
            return

        enrolled_courses = self.get_courses_enrolled(user, guild)
        view = CoursesDropdownView(enrolled_courses, True)
        await interaction.response.send_message(
            embed=LoggerEmbed(
                "Enrollment Status",
                read_txt("./bics_bot/texts/enrollment.txt"),
            ),
            view=view,
            ephemeral=True,
        )

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID],
        description="Courses Selection.",
    )
    async def unenroll(self, interaction: Interaction) -> None:
        """
        The </unenroll> command is used for students who wish to remove their
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
            # The user has no roles. So he must first use the /intro command
            msg = (
                "You haven't yet introduced yourself! Make sure you use the **/intro** command first",
            )
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
            )
            return

        if nextcord.utils.get(user.roles, "Incoming"):
            # The user has the incoming role and thus not allowed to enroll
            msg = ("You are not allowed to enroll to courses yet!",)
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
            )
            return

        enrolled_courses = self.get_courses_enrolled(user, guild)
        view = CoursesDropdownView(enrolled_courses, False)
        await interaction.response.send_message(
            embed=LoggerEmbed(
                "Unenrollment Status",
                read_txt("./bics_bot/texts/unenrollment.txt"),
            ),
            view=view,
            ephemeral=True,
        )

    def get_courses_enrolled(
        self, user: Interaction.user, guild: Guild
    ) -> dict[str, bool]:
        """Retrieves the courses a student is enrolled to.

        Technically, it returns the courses that the student can view it by
        any means necessary (member level permission, role level permission,
        admin rights).

        Args:
            user: the user who is doing the </enroll> or <unenroll> request.
            guild: the server object, containing information on text channels
              necessary for this opeation

        Returns:
            dictionary where the keys are the courses the student can see
        """
        enrolled: dict[str, bool] = {}
        channels = guild.text_channels
        courses_channels = retrieve_courses_text_channels_names(guild)

        for channel in channels:
            if channel.name in courses_channels and user in channel.members:
                enrolled[channel.name] = True
        return enrolled


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(CoursesCmd(client))
