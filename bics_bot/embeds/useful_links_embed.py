from nextcord import Embed
from nextcord import Colour

from bics_bot.utils.file_manipulation import read_txt


class UsefulLinksEmbed(Embed):
    """
    Discord embed that contains useful links for the BICS.
    """

    def __init__(self):
        title = "Useful links"
        super().__init__(colour=Colour.blue(), title=title)
        self.description = read_txt("./bics_bot/texts/useful_links_embed.txt")
