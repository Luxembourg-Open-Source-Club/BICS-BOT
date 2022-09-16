from nextcord import Embed
from nextcord import Colour
import sys

sys.path.append("../")
from server_ids import *


class Help_embed(Embed):
    def __init__(self):
        title = "Help"
        super().__init__(colour=Colour.blue(), title=title)
        self.add_field(
            name="/help",
            value=" - Shows all the possible commands of the bot",
            inline=False,
        )
        self.add_field(
            name=f"/intro ",
            value=f""" - *Only works in <#{INTRO_CHANNEL_ID}>*\n - Enter this command in order to get a role and introduce yourself.""",
            inline=False,
        )
