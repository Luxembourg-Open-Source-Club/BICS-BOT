from nextcord import Embed
from nextcord import Colour

from bics_bot.utils.file_manipulation import read_txt


class BspEmbed(Embed):
    """
    Discord embed that shows a list of useful links for BSP.
    """

    def __init__(self):
        title = "Useful BSP links"
        super().__init__(colour=Colour.blue(), title=title)
        self.description = read_txt("./bics_bot/texts/bsp_embed.txt")
