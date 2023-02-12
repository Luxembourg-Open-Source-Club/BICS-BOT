from nextcord import Embed
from nextcord import Colour

INFO_LEVEL = "INFO"
WARNING_LEVEL = "WARN"
ERROR_LEVEL = "ERROR"

level_colors = {
    "INFO": Colour.blue,
    "WARN": Colour.yellow,
    "ERROR": Colour.red,
}


class LoggerEmbed(Embed):
    """Discord embed that can be used to send information in form of a log"""

    def __init__(self, status, message, level=INFO_LEVEL):
        super().__init__(
            colour=level_colors[level], title=status, description=message
        )
