import nextcord
import json
from bics_bot.embeds.courses_embed import CoursesSelectionEmbed
from bics_bot.config.server_ids import *
from bics_bot.utils.channels_utils import retrieve_courses_text_channels_by_year

PATH = "./bics_bot/data/discord_channels.json"

with open(PATH) as f:
    text_channels = json.load(f)


class DropdownItem1(nextcord.ui.Select):
    def __init__(self, enrolled_courses):
        super().__init__(
            placeholder="Year 1",
            min_values=0,
            max_values=len(self._get_options(enrolled_courses)),
            options=self._get_options(enrolled_courses),
        )

    def _get_options(self, enrolled_courses):
        options = []
        enrolled = False
        for value in text_channels["courses"]["year1"]["winter"]:
            if value["name"] in enrolled_courses:
                enrolled = True
            else:
                enrolled = False
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 1 course", emoji="⛄", default=enrolled
                )
            )
        for value in text_channels["courses"]["year1"]["summer"]:
            if value["name"] in enrolled_courses:
                enrolled = True
            else:
                enrolled = False
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 2 course", emoji="☀️", default=enrolled
                )
            )
        return options


class DropdownItem2(nextcord.ui.Select):
    def __init__(self, enrolled_courses):
        super().__init__(
            placeholder="Year 2",
            min_values=0,
            max_values=len(self._get_options(enrolled_courses)),
            options=self._get_options(enrolled_courses),
        )

    def _get_options(self, enrolled_courses):
        options = []
        enrolled = False
        for value in text_channels["courses"]["year2"]["winter"]:
            if value["name"] in enrolled_courses:
                enrolled = True
            else:
                enrolled = False
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 3 course", emoji="⛄", default=enrolled
                )
            )
        for value in text_channels["courses"]["year2"]["summer"]:
            if value["name"] in enrolled_courses:
                enrolled = True
            else:
                enrolled = False
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 4 course", emoji="☀️", default=enrolled
                )
            )
        return options


class DropdownItem3(nextcord.ui.Select):
    def __init__(self, enrolled_courses):
        self.chosen_options = []
        super().__init__(
            placeholder="Year 3",
            min_values=0,
            max_values=len(self._get_options(enrolled_courses)),
            options=self._get_options(enrolled_courses),
        )

    def _get_options(self, enrolled_courses):
        options = []
        enrolled = False
        for value in text_channels["courses"]["year3"]["winter"]:
            if value["name"] in enrolled_courses:
                enrolled = True
            else:
                enrolled = False
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 5 course", emoji="⛄", default=enrolled
                )
            )
        for value in text_channels["courses"]["year3"]["summer"]:
            if value["name"] in enrolled_courses:
                enrolled = True
            else:
                enrolled = False
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 6 course", emoji="☀️", default=enrolled
                )
            )
        return options


class DropdownView(nextcord.ui.View):
    def __init__(self, enrolled_courses: list[str]):
        super().__init__(timeout=5000)
        self.item1 = DropdownItem1(enrolled_courses)
        self.item2 = DropdownItem2(enrolled_courses)
        self.item3 = DropdownItem3(enrolled_courses)
        self.add_item(self.item1)
        self.add_item(self.item2)
        self.add_item(self.item3)
        self.enrolled_courses = enrolled_courses

    async def process_course(self, selected_courses, prev_selection, interaction):
        print(f"Selected courses: {selected_courses}")
        print(f"Previous selections: {prev_selection}")
        if selected_courses == []:
            # It either means that the  user wants to unroll from courses or
            # no changes were made
            if not prev_selection == []:
                # User has removed every course selected -> unroll for every course
                print("Courses to be processed")
                print(prev_selection)
                await self.give_course_permissions(prev_selection, interaction.user, interaction.guild)
                print("-------------------------")
        else:
            courses_to_handle = []
            # Only consider the courses that were changed
            for course in selected_courses:
                if course not in prev_selection:
                    courses_to_handle.append(course)

            # Consider the courses that were unchecked by the user -> unroll
            for course in prev_selection:
                if course not in selected_courses:
                    courses_to_handle.append(course)

            print("Courses to be processed")
            print(courses_to_handle)
            await self.give_course_permissions(courses_to_handle, interaction.user, interaction.guild)
            print("-------------------------")

    def separate_prev_selected_courses(self, prev_selection, courses_text_channels):
        courses = {"year1": [], "year2": [], "year3": []}

        for course in courses_text_channels["year1"]:
            if course in prev_selection:
                courses["year1"].append(course)
        for course in courses_text_channels["year2"]:
            if course in prev_selection:
                courses["year2"].append(course)
        for course in courses_text_channels["year3"]:
            if course in prev_selection:
                courses["year3"].append(course)
        return courses

    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.green, row=3)
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        courses_text_channels = retrieve_courses_text_channels_by_year(
            interaction.guild)
        year1_selected_courses = self.item1.values
        year2_selected_courses = self.item2.values
        year3_selected_courses = self.item3.values
        prev_selection = self.separate_prev_selected_courses(
            self.enrolled_courses, courses_text_channels)

        print("Starting processing")
        print("Year 1")
        await self.process_course(year1_selected_courses,
                                  prev_selection["year1"], interaction)
        print("-----------")
        print("Year 2")
        await self.process_course(year2_selected_courses,
                                  prev_selection["year2"], interaction)
        print("-----------")
        print("Year 3")
        await self.process_course(year3_selected_courses,
                                  prev_selection["year3"], interaction)

        print("End process")
        print("================================================================")
        embed = CoursesSelectionEmbed(
            [year1_selected_courses, year2_selected_courses, year3_selected_courses])
        # await self.give_course_permissions(courses, interaction.user, interaction.guild)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        self.stop()

    @nextcord.ui.button(
        label="Cancel", style=nextcord.ButtonStyle.red, row=3, custom_id="cancel-btn"
    )
    async def cancel_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        await interaction.response.send_message("Canceled operation. No changes made.", ephemeral=True)
        self.stop()

    async def give_course_permissions(self, courses: dict[str], user: nextcord.Interaction.user, guild: nextcord.Guild):
        for text_channel in guild.text_channels:
            if text_channel.name in courses:
                if not text_channel.permissions_for(user).read_messages:
                    print(f"enroll {text_channel}")
                    await text_channel.set_permissions(target=user, read_messages=True,
                                                       send_messages=True)
                else:
                    print(f"unenroll {text_channel}")
                    await text_channel.set_permissions(target=user, read_messages=False,
                                                       send_messages=False)

    def is_course_channel(self, category_id):  # from left to right: sem6-1
        category_ids = [CATEGORY_SEMESTER_1_ID, CATEGORY_SEMESTER_2_ID, CATEGORY_SEMESTER_3_ID,
                        CATEGORY_SEMESTER_4_ID, CATEGORY_SEMESTER_5_ID, CATEGORY_SEMESTER_6_ID]
        return category_id in category_ids

    def is_enrollable(self, courses: dict[str], channel: nextcord.TextChannel, user: nextcord.Interaction.user):
        return channel.name in courses and not channel.permissions_for(user).read_messages
