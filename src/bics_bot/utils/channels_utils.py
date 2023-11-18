from nextcord import Interaction
import csv
import datetime
import time
from bics_bot.utils.server_utilities import retrieve_server_ids

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
    server_config = retrieve_server_ids(guild)
    ids = [
        server_config["categories"]["semester-1"],
        server_config["categories"]["semester-2"],
        server_config["categories"]["semester-3"],
        server_config["categories"]["semester-4"],
        server_config["categories"]["semester-5"],
        server_config["categories"]["semester-6"],
    ]
    categories = guild.by_category()
    text_channels = []
    for category in categories:
        if category[0].id in ids:
            for text_channel in category[1]:
                text_channels.append(text_channel.name)

    return text_channels


def read_csv():
    """
    Reads the csv file to order informations.
    """
    fields = []
    rows = []
    with open(CALENDAR_FILE_PATH, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return (fields, rows)


def get_user_year(user) -> str:
    """
    Get the string describing the year of the user.

    Args:
        user: The user
    Returns:
        string describing year of user
    """
    for role in user.roles:
        if role.name.startswith("Year"):
            return role.name


def get_unixtime(deadline_date: str, deadline_time: str) -> int:
    """
    Get unix time from deadline date and time.

    Args:
        deadline_date: The deadline date.
        deadline_time: The deadline time to add to the calendar.
    Returns:
        integer describing unix time
    """
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
    server_config = retrieve_server_ids(guild)
    ids = [
        server_config["categories"]["semester-1"],
        server_config["categories"]["semester-2"],
        server_config["categories"]["semester-3"],
        server_config["categories"]["semester-4"],
        server_config["categories"]["semester-5"],
        server_config["categories"]["semester-6"],
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
    server_config = retrieve_server_ids(guild)
    ids = [
        server_config["categories"]["semester-1"],
        server_config["categories"]["semester-2"],
        server_config["categories"]["semester-3"],
        server_config["categories"]["semester-4"],
        server_config["categories"]["semester-5"],
        server_config["categories"]["semester-6"],
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
    """
    Filters course name to ignore case.
    """
    return " ".join([t.capitalize() for t in text.split("-")])


def unfilter_course_name(text):
    """
    Unfilter course name
    """
    return "-".join(text.lower().split(" "))
