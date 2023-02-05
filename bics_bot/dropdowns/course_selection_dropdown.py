import sys
import nextcord
import json
sys.path.append("../../")
from server_ids import *
from embeds.courses_embed import Courses_embed

PATH = "./data/discord_channels.json"

with open(PATH) as f:
    text_channels = json.load(f)

class DropdownItem1(nextcord.ui.Select):
    chosen_options = []

    def __init__(self, enrolled_courses):
        super().__init__(
            placeholder="Year 1",
            min_values=0,
            max_values=len(self._get_options(enrolled_courses)),
            options=self._get_options(enrolled_courses),
        )

    def _get_options(self, enrolled_courses):
        options = []
        for value in text_channels["courses"]["year1"]["winter"]:
            enrolled = value["name"] in enrolled_courses
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 1 course", emoji="⛄", default=enrolled
                )
            )

        for value in text_channels["courses"]["year1"]["summer"]:
            enrolled = value["name"] in enrolled_courses
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 2 course", emoji="☀️", default=enrolled
                )
            )
        return options

    async def callback(self, interaction: nextcord.Interaction):
        self.chosen_options = self.values


class DropdownItem2(nextcord.ui.Select):
    chosen_options = []

    def __init__(self, enrolled_courses):
        super().__init__(
            placeholder="Year 2",
            min_values=0,
            max_values=len(self._get_options(enrolled_courses)),
            options=self._get_options(enrolled_courses),
        )

    def _get_options(self, enrolled_courses):
        options = []
        for value in text_channels["courses"]["year2"]["winter"]:
            enrolled = value["name"] in enrolled_courses
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 3 course", emoji="⛄", default=enrolled
                )
            )

        for value in text_channels["courses"]["year2"]["summer"]:
            enrolled = value["name"] in enrolled_courses
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 4 course", emoji="☀️", default=enrolled
                )
            )
        return options

    async def callback(self, interaction: nextcord.Interaction):
        self.chosen_options = self.values


class DropdownItem3(nextcord.ui.Select):
    chosen_options = []

    def __init__(self, enrolled_courses):
        super().__init__(
            placeholder="Year 3",
            min_values=0,
            max_values=len(self._get_options(enrolled_courses)),
            options=self._get_options(enrolled_courses),
        )

    def _get_options(self, enrolled_courses):
        options = []
        for value in text_channels["courses"]["year3"]["winter"]:
            enrolled = value["name"] in enrolled_courses
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 5 course", emoji="⛄", default=enrolled
                )
            )

        for value in text_channels["courses"]["year3"]["summer"]:
            enrolled = value["name"] in enrolled_courses
            options.append(
                nextcord.SelectOption(
                    label=value["name"], description="Semester 6 course", emoji="☀️", default=enrolled
                )
            )
        return options

    async def callback(self, interaction: nextcord.Interaction):
        self.chosen_options = self.values


class DropdownView(nextcord.ui.View):
    def __init__(self, enrolled_courses:list[str]):
        super().__init__()
        self.item1 = DropdownItem1(enrolled_courses)
        self.item2 = DropdownItem2(enrolled_courses)
        self.item3 = DropdownItem3(enrolled_courses)
        self.add_item(self.item1)
        self.add_item(self.item2)
        self.add_item(self.item3)

    # ------------------------------------------------------------------------
    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.green, row=3)
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        embed = Courses_embed(self.item1.values, self.item2.values, self.item3.values)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        self.stop()

    # ------------------------------------------------------------------------
    @nextcord.ui.button(
        label="Cancel", style=nextcord.ButtonStyle.red, row=3, custom_id="cancel-btn"
    )
    async def cancel_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        embed = Courses_embed(self.item1.values, self.item2.values, self.item3.values)
        await interaction.response.send_message("Canceled. Below are your current courses:", embed=embed, ephemeral=True)
        self.stop()