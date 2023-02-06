import nextcord
from bics_bot.config.server_ids import *


def retrieve_courses_text_channels_names(guild: nextcord.Interaction.guild) -> list[str]:
    """Retrieves all the text channels names for the different courses.

        Args:
            guild: The guild from where to retrieve the text channels

        Rerturns:
            List with all courses text channels names        

"""
    ids = [CATEGORY_SEMESTER_1_ID, CATEGORY_SEMESTER_2_ID, CATEGORY_SEMESTER_3_ID,
           CATEGORY_SEMESTER_4_ID, CATEGORY_SEMESTER_5_ID, CATEGORY_SEMESTER_6_ID]
    categories = guild.by_category()
    text_channels = []
    for category in categories:
        if category[0].id in ids:
            for text_channel in category[1]:
                text_channels.append(text_channel.name)

    return text_channels


def retrieve_courses_text_channels_by_year(guild: nextcord.Interaction.guild) -> dict:
    """Retrieves all the text channels for the different courses.

        Args:
            guild: The guild from where to retrieve the text channels

        Rerturns:
            dictionary where the key is the year, as yearn and the value is a 
            list whith text channel names associated with the year.
    """
    ids = [CATEGORY_SEMESTER_1_ID, CATEGORY_SEMESTER_2_ID, CATEGORY_SEMESTER_3_ID,
           CATEGORY_SEMESTER_4_ID, CATEGORY_SEMESTER_5_ID, CATEGORY_SEMESTER_6_ID]
    categories = guild.by_category()
    text_channels = {}
    for category in categories:
        if category[0].id in ids:
            text_channels[f"year{category[0].name[-1]}"] = [
                text_channel.name for text_channel in category[1]]

    return text_channels
