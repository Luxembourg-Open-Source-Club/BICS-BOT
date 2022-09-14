import nextcord
from nextcord.ui import View, Select, Button, view
from json_loader import Loader

json_file_path = "./discord_channels.json"

channels_data_loader = Loader(json_file_path)


def _get_options(year):
    options = []
    if year == 1:
        for value in channels_data_loader.get_year_1_winter_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 1 course")
            )

        for value in channels_data_loader.get_year_1_summer_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 2 course")
            )
    elif year == 2:
        for value in channels_data_loader.get_year_2_winter_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 3 course")
            )

        for value in channels_data_loader.get_year_2_summer_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 4 course")
            )
    else:
        for value in channels_data_loader.get_year_3_winter_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 1 course")
            )
        for value in channels_data_loader.get_year_3_summer_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 6 course")
            )

    return options


class CourseSelectionView(View):
    options = []

    @nextcord.ui.select(
        placeholder="Year 1 courses",
        max_values=len(_get_options(1)),
        options=_get_options(1),
    )
    async def callback_year1(
        self, select: nextcord.SelectMenu, interaction: nextcord.Interaction
    ):

        # await interaction.response.send_message(f"You chose {select.values}")
        pass

    @nextcord.ui.select(
        placeholder="Year 2 courses",
        max_values=len(_get_options(2)),
        options=_get_options(2),
    )
    async def callback_year2(
        self, select: nextcord.SelectMenu, interaction: nextcord.Interaction
    ):

        self.options.append(select.values)

    @nextcord.ui.select(
        placeholder="Year 3 courses",
        max_values=len(_get_options(3)),
        options=_get_options(3),
    )
    async def callback_year3(
        self, select: nextcord.SelectMenu, interaction: nextcord.Interaction
    ):

        self.options.append(select.values)

    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.green)
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        print(self.options)
        await interaction.response.send_message("Confirmed", ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
    async def cancel_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        print(self.options)
        await interaction.response.send_message("Canceled", ephemeral=True)
        self.value = False
        self.stop()
