import nextcord
import json

from nextcord.interactions import Interaction
from bics_bot.embeds.courses_embed import LoggerEmbed

PATH = "./bics_bot/data/discord_channels.json"

with open(PATH) as f:
    text_channels = json.load(f)


class Year1CoursesDropdown(nextcord.ui.Select):
    def __init__(self, enrolled_courses: dict[str, bool], enroll: bool):
        self._options = self._get_options(enrolled_courses, enroll)

    def build(self):
        super().__init__(
            placeholder="Year 1",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, enrolled_courses: dict[str, bool], enroll: bool):
        if enroll:
            return self.enrolling(enrolled_courses)
        else:
            return self.unenrolling(enrolled_courses)

    def enrolling(self, enrolled_courses: dict[str, bool]):
        options = []
        for value in text_channels["courses"]["year1"]["winter"]:
            if value["name"] not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 1 course",
                        emoji="⛄",
                    )
                )
        for value in text_channels["courses"]["year1"]["summer"]:
            if value["name"] not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 2 course",
                        emoji="☀️",
                    )
                )
        return options

    def unenrolling(self, enrolled_courses: dict[str, bool]):
        options = []
        for value in text_channels["courses"]["year1"]["winter"]:
            if value["name"] in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 1 course",
                        emoji="⛄",
                    )
                )
        for value in text_channels["courses"]["year1"]["summer"]:
            if value["name"] in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 2 course",
                        emoji="☀️",
                    )
                )
        return options


class Year2CoursesDropdown(nextcord.ui.Select):
    def __init__(self, enrolled_courses: dict[str, bool], enroll: bool):
        self._options = self._get_options(enrolled_courses, enroll)

    def build(self):
        super().__init__(
            placeholder="Year 2",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, enrolled_courses: dict[str, bool], enroll: bool):
        if enroll:
            return self.enrolling(enrolled_courses)
        else:
            return self.unenrolling(enrolled_courses)

    def enrolling(self, enrolled_courses: dict[str, bool]):
        options = []
        for value in text_channels["courses"]["year2"]["winter"]:
            if value["name"] not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 3 course",
                        emoji="⛄",
                    )
                )
        for value in text_channels["courses"]["year2"]["summer"]:
            if value["name"] not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 4 course",
                        emoji="☀️",
                    )
                )
        return options

    def unenrolling(self, enrolled_courses: dict[str, bool]):
        options = []
        for value in text_channels["courses"]["year2"]["winter"]:
            if value["name"] in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 3 course",
                        emoji="⛄",
                    )
                )
        for value in text_channels["courses"]["year2"]["summer"]:
            if value["name"] in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 4 course",
                        emoji="☀️",
                    )
                )
        return options


class Year3CoursesDropdown(nextcord.ui.Select):
    def __init__(self, enrolled_courses: dict[str, bool], enroll: bool):
        self._options = self._get_options(enrolled_courses, enroll)

    def build(self):
        super().__init__(
            placeholder="Year 3",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, enrolled_courses: dict[str, bool], enroll: bool):
        if enroll:
            return self.enrolling(enrolled_courses)
        else:
            return self.unenrolling(enrolled_courses)

    def enrolling(self, enrolled_courses: dict[str, bool]):
        options = []
        for value in text_channels["courses"]["year3"]["winter"]:
            if value["name"] not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 5 course",
                        emoji="⛄",
                    )
                )
        for value in text_channels["courses"]["year3"]["summer"]:
            if value["name"] not in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 6 course",
                        emoji="☀️",
                    )
                )
        return options

    def unenrolling(self, enrolled_courses: dict[str, bool]):
        options = []
        for value in text_channels["courses"]["year3"]["winter"]:
            if value["name"] in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 5 course",
                        emoji="⛄",
                    )
                )
        for value in text_channels["courses"]["year3"]["summer"]:
            if value["name"] in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=value["name"],
                        description="Semester 6 course",
                        emoji="☀️",
                    )
                )
        return options


class CoursesDropdownView(nextcord.ui.View):
    def __init__(self, enrolled_courses: dict[str, bool], enroll):
        super().__init__(timeout=5000)
        self.year1_dropdown = Year1CoursesDropdown(enrolled_courses, enroll)
        self.year2_dropdown = Year2CoursesDropdown(enrolled_courses, enroll)
        self.year3_dropdown = Year3CoursesDropdown(enrolled_courses, enroll)
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
        if len(self.year1_dropdown._options) > 0:
            await self.give_course_permissions(
                self.year1_dropdown.values, interaction
            )
        if len(self.year2_dropdown._options) > 0:
            await self.give_course_permissions(
                self.year2_dropdown.values, interaction
            )
        if len(self.year3_dropdown._options) > 0:
            await self.give_course_permissions(
                self.year3_dropdown.values, interaction
            )

        embed = LoggerEmbed(
            f"{'Enrollment' if self.operation else 'Unenrollment'} Status",
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
        await interaction.response.send_message(
            "Canceled operation. No changes made.", ephemeral=True
        )
        self.stop()

    async def give_course_permissions(
        self, courses: dict[str], interaction: Interaction
    ):
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
        await text_channel.set_permissions(target=user, read_messages=True)

    async def unenroll_course(self, user, text_channel):
        await text_channel.set_permissions(target=user, overwrite=None)
