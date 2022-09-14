from discord.ui import Item, Select
from json_loader import Loader

json_file_path = "./discord_channels.json"

channels_data_loader = Loader(json_file_path)

class Year1MenuSelect(Select):
    def __init__(self):
        # super().__init__(custom_id="year1_menu", "Choose the cours", 0, len(channels_data_loader.get_year_1_summer_courses())+len(channels_data_loader.get_year_1_winter_courses()), options, disabled, row)
