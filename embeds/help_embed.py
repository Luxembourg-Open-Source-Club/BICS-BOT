from nextcord import Embed
from nextcord import Colour


class Help_embed(Embed):
    def __init__(self):
        title = "Help"
        super().__init__(colour=Colour.blue(), title=title)
        self.add_field(
            name="/help",
            value=" * Shows all the possible commands of the bot",
            inline=False,
        )
