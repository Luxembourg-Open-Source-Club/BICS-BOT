from nextcord import Embed
from nextcord import Colour

from bics_bot.utils.file_manipulation import read_txt


class WelcomeEmbed(Embed):
    """
    Discord embed which contains a welcome message to a new user.
    """

    def __init__(self, user_name, server_name):
        title = "Welcome on board👋"
        super().__init__(colour=Colour.blue(), title=title)
        self.description = (
            f"Hey **{user_name}** and welcome to **{server_name}**, the **unofficial** BICS discord server!\n"
            + read_txt("./bics_bot/texts/welcome_embed.txt")
        )
