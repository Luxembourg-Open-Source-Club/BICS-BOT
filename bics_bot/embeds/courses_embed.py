from nextcord import Embed
from nextcord import Colour


class CoursesEmbed(Embed):
    """
    Discord embed that is sent showing the user the courses he has chosen.
    """

    def __init__(self, status, message):
        super().__init__(colour=Colour.blue(), title=status)
        self.description = message
