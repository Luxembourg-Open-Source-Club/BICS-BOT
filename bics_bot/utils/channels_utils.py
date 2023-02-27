from nextcord import Interaction
from bics_bot.config.server_ids import (
    CATEGORY_SEMESTER_1_ID,
    CATEGORY_SEMESTER_2_ID,
    CATEGORY_SEMESTER_3_ID,
    CATEGORY_SEMESTER_4_ID,
    CATEGORY_SEMESTER_5_ID,
    CATEGORY_SEMESTER_6_ID,
    CHANNEL_CALENDAR_ID,
    MESSAGE_CALENDAR_ID,
    CHANNEL_CALENDAR_YEAR_1_ID,
    CHANNEL_CALENDAR_YEAR_2_ID,
    CHANNEL_CALENDAR_YEAR_3_ID,
    MESSAGE_CALENDAR_YEAR_3_ID,
)
from bics_bot.embeds.logger_embed import WARNING_LEVEL, LoggerEmbed
import csv, datetime, time

CALENDAR_FILE_PATH = "./bics_bot/data/calendar.csv"


def retrieve_courses_text_channels_names(
    guild: Interaction.guild,
) -> list[str]:
    """Retrieves all the text channels names for the different courses.

    Args:
        guild: The guild from where to retrieve the text channels

    Rerturns:
        List with all courses text channels names
    """
    ids = [
        CATEGORY_SEMESTER_1_ID,
        CATEGORY_SEMESTER_2_ID,
        CATEGORY_SEMESTER_3_ID,
        CATEGORY_SEMESTER_4_ID,
        CATEGORY_SEMESTER_5_ID,
        CATEGORY_SEMESTER_6_ID,
    ]
    categories = guild.by_category()
    text_channels = []
    for category in categories:
        if category[0].id in ids:
            for text_channel in category[1]:
                text_channels.append(text_channel.name)

    return text_channels


def read_csv():
    fields = []
    rows = []
    with open(CALENDAR_FILE_PATH, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return (fields, rows)


def get_user_year(user) -> str:
    for role in user.roles:
        if role.name.startswith("Year"):
            return role.name


def get_unixtime(deadline_date: str, deadline_time: str) -> int:
    deadline_date = deadline_date.split(".")
    deadline_time = deadline_time.split(":")
    d = datetime.datetime(
        int(deadline_date[2]),
        int(deadline_date[1]),
        int(deadline_date[0]),
        int(deadline_time[0]),
        int(deadline_time[1]),
    )
    unixtime = int(time.mktime(d.timetuple()))
    return unixtime


def retrieve_courses_text_channels_by_year(
    guild: Interaction.guild,
) -> dict:
    """Retrieves all the text channels for the different courses.

    Args:
        guild: The guild from where to retrieve the text channels

    Rerturns:
        dictionary where the key is the year, as yearn and the value is a
        list whith text channel names associated with the year.
    """
    ids = [
        CATEGORY_SEMESTER_1_ID,
        CATEGORY_SEMESTER_2_ID,
        CATEGORY_SEMESTER_3_ID,
        CATEGORY_SEMESTER_4_ID,
        CATEGORY_SEMESTER_5_ID,
        CATEGORY_SEMESTER_6_ID,
    ]
    categories = guild.by_category()
    text_channels = {"year1": [], "year2": [], "year3": []}
    for category in categories:
        if category[0].id in ids:
            if (category[0].name[-1]) == "1" or category[0].name[-1] == "2":
                text_channels["year1"] += [
                    text_channel.name for text_channel in category[1]
                ]
            if (category[0].name[-1]) == "3" or category[0].name[-1] == "4":
                text_channels["year2"] += [
                    text_channel.name for text_channel in category[1]
                ]
            if (category[0].name[-1]) == "5" or category[0].name[-1] == "6":
                text_channels["year3"] += [
                    text_channel.name for text_channel in category[1]
                ]

    return text_channels


def retrieve_courses_text_channels(
    guild: Interaction.guild,
) -> dict:
    """Retrieves all the text channels for the different courses.

    Args:
        guild: The guild from where to retrieve the text channels

    Rerturns:
        dictionary where the key is the year, as yearn and the value is a
        list whith text channel names associated with the year.
    """
    ids = [
        CATEGORY_SEMESTER_1_ID,
        CATEGORY_SEMESTER_2_ID,
        CATEGORY_SEMESTER_3_ID,
        CATEGORY_SEMESTER_4_ID,
        CATEGORY_SEMESTER_5_ID,
        CATEGORY_SEMESTER_6_ID,
    ]
    categories = guild.by_category()
    text_channels = {"year1": {}, "year2": {}, "year3": {}}
    for category in categories:
        if category[0].id in ids:
            if (category[0].name[-1]) == "1" or category[0].name[-1] == "2":
                if int(category[0].name[-1]) % 2 == 0:
                    text_channels["year1"]["summer"] = [
                        filter_course_name(text_channel.name)
                        for text_channel in category[1]
                    ]
                else:
                    text_channels["year1"]["winter"] = [
                        filter_course_name(text_channel.name)
                        for text_channel in category[1]
                    ]
            elif (category[0].name[-1]) == "3" or category[0].name[-1] == "4":
                if int(category[0].name[-1]) % 2 == 0:
                    text_channels["year2"]["summer"] = [
                        filter_course_name(text_channel.name)
                        for text_channel in category[1]
                    ]
                else:
                    text_channels["year2"]["winter"] = [
                        filter_course_name(text_channel.name)
                        for text_channel in category[1]
                    ]
            else:
                if int(category[0].name[-1]) % 2 == 0:
                    text_channels["year3"]["summer"] = [
                        filter_course_name(text_channel.name)
                        for text_channel in category[1]
                    ]
                else:
                    text_channels["year3"]["winter"] = [
                        filter_course_name(text_channel.name)
                        for text_channel in category[1]
                    ]

    return text_channels


def filter_course_name(text):
    return " ".join([t.capitalize() for t in text.split("-")])


def unfilter_course_name(text):
    return "-".join(text.lower().split(" "))
