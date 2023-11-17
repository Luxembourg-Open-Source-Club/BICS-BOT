import nextcord

from nextcord.interactions import Interaction
from bics_bot.embeds.logger_embed import LoggerEmbed
from bics_bot.utils.channels_utils import (
    retrieve_courses_text_channels,
    unfilter_course_name,
)


class Year1CoursesDropdown(nextcord.ui.Select):
    """
    This class allows a dropdown of courses of year 1.
    It allows user to select one or multiple courses from year 1 to enroll in.

    Attributes:
        enrolled_courses: A dictionary of courses to enroll or unenroll in
        enroll: A boolean to determine the enrolment
        text_channels: Text channels of courses
    """
    def __init__(
        self,
        enrolled_courses: dict[str, bool],
        enroll: bool,
        text_channels,
    ):
        self.text_channels = text_channels
        self._options = self._get_options(enrolled_courses, enroll)

    def build(self):
        super().__init__(
            placeholder="Year 1",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, enrolled_courses: dict[str, bool], enroll: bool):
        """
        This method allows  to get the option (enroll or unenroll) from 
        a student.

        Args:
            enrolled_courses: A dictionary of courses to enroll or unenroll in
            enroll: A boolean to determine the enrolment
        """
        if enroll:
            return self.enrolling(enrolled_courses)
        else:
            return self.unenrolling(enrolled_courses)

    def enrolling(self, enrolled_courses: dict[str, bool]):
        """
        This method allows the enrolment process. 

        Args:
            enrolled_courses: A dictionary of courses to enroll or unenroll in
        """
        options = []
        for value in self.text_channels["year1"]["winter"]:
            if unfilter_course_name(value) not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 1 course",
                        emoji="⛄",
                    )
                )
        for value in self.text_channels["year1"]["summer"]:
            if unfilter_course_name(value) not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 2 course",
                        emoji="☀️",
                    )
                )
        return options

    def unenrolling(self, enrolled_courses: dict[str, bool]):
        """
        This method allows the unenrolment process. 

        Args:
            enrolled_courses: A dictionary of courses to enroll or unenroll in
        """
        options = []
        for value in self.text_channels["year1"]["winter"]:
            if unfilter_course_name(value) in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 1 course",
                        emoji="⛄",
                    )
                )
        for value in self.text_channels["year1"]["summer"]:
            if unfilter_course_name(value) in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 2 course",
                        emoji="☀️",
                    )
                )
        return options


class Year2CoursesDropdown(nextcord.ui.Select):
    """
    This class allows a dropdown of courses of year 2.
    It allows user to select one or multiple courses from year 2 to enroll in.

    Attributes:
        enrolled_courses: A dictionary of courses to enroll or unenroll in
        enroll: A boolean to determine the enrolment
        text_channels: Text channels of courses
    """
    def __init__(
        self,
        enrolled_courses: dict[str, bool],
        enroll: bool,
        text_channels,
    ):
        self.text_channels = text_channels
        self._options = self._get_options(enrolled_courses, enroll)

    def build(self):
        super().__init__(
            placeholder="Year 2",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, enrolled_courses: dict[str, bool], enroll: bool):
        """
        This method allows  to get the option (enroll or unenroll) from 
        a student.

        Args:
            enrolled_courses: A dictionary of courses to enroll or unenroll in
            enroll: A boolean to determine the enrolment
        """
        if enroll:
            return self.enrolling(enrolled_courses)
        else:
            return self.unenrolling(enrolled_courses)

    def enrolling(self, enrolled_courses: dict[str, bool]):
        """
        This method allows the enrolment process. 

        Args:
            enrolled_courses: A dictionary of courses to enroll or unenroll in
        """
        options = []
        for value in self.text_channels["year2"]["winter"]:
            if unfilter_course_name(value) not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 3 course",
                        emoji="⛄",
                    )
                )
        for value in self.text_channels["year2"]["summer"]:
            if unfilter_course_name(value) not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 4 course",
                        emoji="☀️",
                    )
                )
        return options

    def unenrolling(self, enrolled_courses: dict[str, bool]):
        """
        This method allows the enrolment process. 

        Args:
            enrolled_courses: A dictionary of courses to enroll or unenroll in
        """
        options = []
        for value in self.text_channels["year2"]["winter"]:
            if unfilter_course_name(value) in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 3 course",
                        emoji="⛄",
                    )
                )
        for value in self.text_channels["year2"]["summer"]:
            if unfilter_course_name(value) in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 4 course",
                        emoji="☀️",
                    )
                )
        return options


class Year3CoursesDropdown(nextcord.ui.Select):
    """
    This class allows a dropdown of courses of year 3.
    It allows user to select one or multiple courses from year 3 to enroll in.

    Attributes:
        enrolled_courses: A dictionary of courses to enroll or unenroll in
        enroll: A boolean to determine the enrolment
        text_channels: Text channels of courses
    """
    def __init__(
        self,
        enrolled_courses: dict[str, bool],
        enroll: bool,
        text_channels: Interaction.guild,
    ):
        self.text_channels = text_channels
        self._options = self._get_options(enrolled_courses, enroll)

    def build(self):
        super().__init__(
            placeholder="Year 3",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, enrolled_courses: dict[str, bool], enroll: bool):
        """
        This method allows  to get the option (enroll or unenroll) from 
        a student.

        Args:
            enrolled_courses: A dictionary of courses to enroll or unenroll in
            enroll: A boolean to determine the enrolment
        """ 
        if enroll:
            return self.enrolling(enrolled_courses)
        else:
            return self.unenrolling(enrolled_courses)

    def enrolling(self, enrolled_courses: dict[str, bool]):
        """
        This method allows the enrolment process. 

        Args:
            enrolled_courses: A dictionary of courses to enroll or unenroll in
        """
        options = []
        for value in self.text_channels["year3"]["winter"]:
            if unfilter_course_name(value) not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 5 course",
                        emoji="⛄",
                    )
                )
        for value in self.text_channels["year3"]["summer"]:
            if unfilter_course_name(value) not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 6 course",
                        emoji="☀️",
                    )
                )
        return options

    def unenrolling(self, enrolled_courses: dict[str, bool]):
        """
        This method allows the enrolment process. 

        Args:
            enrolled_courses: A dictionary of courses to enroll or unenroll in
        """
        options = []
        for value in self.text_channels["year3"]["winter"]:
            if unfilter_course_name(value) in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 5 course",
                        emoji="⛄",
                    )
                )
        for value in self.text_channels["year3"]["summer"]:
            if unfilter_course_name(value) in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value,
                        description="Semester 6 course",
                        emoji="☀️",
                    )
                )
        return options


class CoursesDropdownView(nextcord.ui.View):
    """
    This class allows to view all dropdown courses.

    Attributes:
        enrolled_courses: A dictionary of courses to enroll or unenroll in
        enroll: A boolean to determine the enrolment
        text_channels: Text channels of courses
    """
    def __init__(
        self,
        enrolled_courses: dict[str, bool],
        enroll,
        guild: Interaction.guild,
    ):
        super().__init__(timeout=5000)
        self.text_channels = retrieve_courses_text_channels(guild)
        self.year1_dropdown = Year1CoursesDropdown(
            enrolled_courses, enroll, self.text_channels
        )
        self.year2_dropdown = Year2CoursesDropdown(
            enrolled_courses, enroll, self.text_channels
        )
        self.year3_dropdown = Year3CoursesDropdown(
            enrolled_courses, enroll, self.text_channels
        )
        if len(self.year1_dropdown._options) > 0:
            self.year1_dropdown.build()
            self.add_item(self.year1_dropdown)
        if len(self.year2_dropdown._options) > 0:
            self.year2_dropdown.build()
            self.add_item(self.year2_dropdown)
        if len(self.year3_dropdown._options) > 0:
            self.year3_dropdown.build()
            self.add_item(self.year3_dropdown)
        self.enrolled_courses = enrolled_courses
        self.operation = enroll

    @nextcord.ui.button(
        label="Confirm", style=nextcord.ButtonStyle.green, row=3
    )
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        """
        This method allows to confirm courses selected in the dropdown.

        Args:
            button: The confirm button
            interaction: The interaction with the button
        """
        if len(self.year1_dropdown._options) > 0:
            await self.give_course_permissions(
                [unfilter_course_name(v) for v in self.year1_dropdown.values],
                interaction,
            )
        if len(self.year2_dropdown._options) > 0:
            await self.give_course_permissions(
                [unfilter_course_name(v) for v in self.year2_dropdown.values],
                interaction,
            )
        if len(self.year3_dropdown._options) > 0:
            await self.give_course_permissions(
                [unfilter_course_name(v) for v in self.year3_dropdown.values],
                interaction,
            )

        embed = LoggerEmbed(
            f"You have been successfully {'**enrolled**' if self.operation else '**unenrolled**'} from the selected courses!",
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        self.stop()

    @nextcord.ui.button(
        label="Cancel",
        style=nextcord.ButtonStyle.red,
        row=3,
        custom_id="cancel-btn",
    )
    async def cancel_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        """
        This method allows to cancel the enrolment in selected courses.

        Args:
            button: The cancel button
            interaction: The interaction with the button
        """
        await interaction.response.send_message(
            "Canceled operation. No changes made.", ephemeral=True
        )
        self.stop()

    async def give_course_permissions(
        self, courses: dict[str], interaction: Interaction
    ):
        """
        This method set permissions for students according to their respective enrolled in courses.

        Args:
            courses: A dictionnary of courses channels
            interaction: Required by the API. Gives meta information about the interaction
        """
        for text_channel in interaction.guild.text_channels:
            if text_channel.name in courses:
                if (
                    self.operation
                    and text_channel.name not in self.enrolled_courses
                ):
                    await self.enroll_course(interaction.user, text_channel)
                elif text_channel.name in self.enrolled_courses:
                    await self.unenroll_course(interaction.user, text_channel)

    async def enroll_course(self, user, text_channel):
        """
        This method is used in give_course_permissions to give access to the right text channels

        Args:
            user: The user that enrolled
            tex_channel: The text_channel of a course
        """
        await text_channel.set_permissions(target=user, read_messages=True)

    async def unenroll_course(self, user, text_channel):
        """
        This method is used in give_course_permissions to revoke access to the right text channels

        Args:
            user: The user that unenrolled
            tex_channel: The text_channel of a course
        """
        await text_channel.set_permissions(target=user, overwrite=None)
