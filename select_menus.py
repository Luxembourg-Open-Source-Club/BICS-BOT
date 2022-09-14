import nextcord
from nextcord.ui import View, Select, Button
from json_loader import Loader

json_file_path = "./discord_channels.json"

channels_data_loader = Loader(json_file_path)


class ConfirmButton(Button):
    def __init__(self):
        super().__init__(label="Confirm")


class Year1MenuSelect(Select):
    def __init__(self):
        super().__init__(
            placeholder="Year 1 courses",
            max_values=len(self.get_options()),
            options=self.get_options(),
        )

    def get_options(self):
        options = []
        for value in channels_data_loader.get_year_1_winter_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 1 course")
            )

        for value in channels_data_loader.get_year_1_summer_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 2 course")
            )
        return options

    async def callback(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"You chose {self.values}")


class Year2MenuSelect(Select):
    def __init__(self):
        super().__init__(
            placeholder="Year 2 courses",
            max_values=len(self.get_options()),
            options=self.get_options(),
        )

    def get_options(self):
        options = []
        for value in channels_data_loader.get_year_2_winter_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 3 course")
            )

        for value in channels_data_loader.get_year_2_summer_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 4 course")
            )
        return options

    async def callback(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"You chose {self.values}")


class Year3MenuSelect(Select):
    def __init__(self):
        super().__init__(
            placeholder="Year 3 courses",
            max_values=len(self.get_options()),
            options=self.get_options(),
        )

    def get_options(self):
        options = []
        for value in channels_data_loader.get_year_3_winter_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 5 course")
            )

        for value in channels_data_loader.get_year_3_summer_courses():
            options.append(
                nextcord.SelectOption(label=value, description="Semester 6 course")
            )
        return options

    async def callback(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"You chose {self.values}")


class ChannelSelectionView(View):
    def __init__(self):
        super().__init__()
        self.add_item(Year1MenuSelect())
        self.add_item(Year2MenuSelect())
        self.add_item(Year3MenuSelect())
        self.add_item(ConfirmButton())
