from nextcord import Embed
from nextcord import Colour
from enum import Enum


class LogLevel(Enum):
    INFO = "Information"
    WARNING = "Warning"
    ERROR = "Error"


level_colors = {
    "Information": Colour.green(),
    "Warning": Colour.yellow(),
    "Error": Colour.red(),
}


class LoggerEmbed(Embed):
    """Discord embed that can be used to send information in form of a log"""

    def __init__(self, message, level=LogLevel.INFO):
        super().__init__(
            colour=level_colors[level.value],
            title=level.value,
            description=message,
        )
