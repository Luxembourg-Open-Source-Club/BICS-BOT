from nextcord import Embed
from nextcord import Colour

from bics_bot.utils.file_manipulation import read_txt


class HelpEmbed(Embed):
    """
    Discord embed that shows the bot's available commands.
    """

    def __init__(self):
        title = "Available bot commands"
        super().__init__(colour=Colour.blue(), title=title)
        self.description = read_txt("./bics_bot/texts/help_embed.txt")
