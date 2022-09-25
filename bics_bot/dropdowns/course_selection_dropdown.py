import nextcord
import json

PATH = "./discord_channels.json"

with open(PATH) as f:
    json_file = json.load(f)


def get_year_1_winter_courses():
    return json_file["courses"]["year1"]["winter"]


def get_year_1_summer_courses():
    return json_file["courses"]["year1"]["summer"]


def get_year_2_winter_courses():
    return json_file["courses"]["year2"]["winter"]


def get_year_2_summer_courses():
    return json_file["courses"]["year2"]["summer"]


def get_year_3_winter_courses():
    return json_file["courses"]["year3"]["winter"]


def get_year_3_summer_courses():
    return json_file["courses"]["year3"]["summer"]


def get_chill_channels():
    return json_file["chill"]


class DropdownItem1(nextcord.ui.Select):
    chosen_options = []

    def __init__(self):
        super().__init__(
            placeholder="Year 1",
            min_values=0,
            max_values=len(self._get_options()),
            options=self._get_options(),
        )

    def _get_options(self):
        options = []
        for value in get_year_1_winter_courses():
            options.append(
                nextcord.SelectOption(
                    label=value, description="Semester 1 course", emoji="⛄"
                )
            )

        for value in get_year_1_summer_courses():
            options.append(
                nextcord.SelectOption(
                    label=value, description="Semester 2 course", emoji="☀️"
                )
            )
        return options

    async def callback(self, interaction: nextcord.Interaction):
        self.chosen_options = self.values


class DropdownItem2(nextcord.ui.Select):
    chosen_options = []

    def __init__(self):
        super().__init__(
            placeholder="Year 2",
            min_values=0,
            max_values=len(self._get_options()),
            options=self._get_options(),
        )

    def _get_options(self):
        options = []
        for value in get_year_2_winter_courses():
            options.append(
                nextcord.SelectOption(
                    label=value, description="Semester 3 course", emoji="⛄"
                )
            )

        for value in get_year_2_summer_courses():
            options.append(
                nextcord.SelectOption(
                    label=value, description="Semester 4 course", emoji="☀️"
                )
            )
        return options

    async def callback(self, interaction: nextcord.Interaction):
        self.chosen_options = self.values


class DropdownItem3(nextcord.ui.Select):
    chosen_options = []

    def __init__(self):
        super().__init__(
            placeholder="Year 3",
            min_values=0,
            max_values=len(self._get_options()),
            options=self._get_options(),
        )

    def _get_options(self):
        options = []
        for value in get_year_3_winter_courses():
            options.append(
                nextcord.SelectOption(
                    label=value, description="Semester 5 course", emoji="⛄"
                )
            )

        for value in get_year_3_summer_courses():
            options.append(
                nextcord.SelectOption(
                    label=value, description="Semester 6 course", emoji="☀️"
                )
            )
        return options

    async def callback(self, interaction: nextcord.Interaction):
        self.chosen_options = self.values


class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.item1 = DropdownItem1()
        self.item2 = DropdownItem2()
        self.item3 = DropdownItem3()
        self.add_item(self.item1)
        self.add_item(self.item2)
        self.add_item(self.item3)

    # ------------------------------------------------------------------------
    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.green, row=3)
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        embed = nextcord.Embed(title="Selected Courses Summary")
        value1 = ""
        value2 = ""
        value3 = ""
        for opt in self.item1.chosen_options:
            value1 += f"- {opt}\n"
        for opt in self.item2.chosen_options:
            value2 += f"- {opt}\n"
        for opt in self.item3.chosen_options:
            value3 += f"- {opt}\n"

        if not value1 == "":
            embed.add_field(name="Year 1 Courses", value=value1, inline=False)
        if not value2 == "":
            embed.add_field(name="Year 2 Courses", value=value2, inline=False)
        if not value3 == "":
            embed.add_field(name="Year 3 Courses", value=value3, inline=False)

        await interaction.response.send_message(ephemeral=True, embed=embed)
        self.stop()

    # ------------------------------------------------------------------------
    @nextcord.ui.button(
        label="Cancel", style=nextcord.ButtonStyle.red, row=3, custom_id="cancel-btn"
    )
    async def cancel_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):

        await interaction.response.send_message("Canceled", ephemeral=True, view=self)
        self.stop()
