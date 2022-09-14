import json

PATH = "./discord_channels.json"

with open(PATH) as f:
    json_file = json.load(f)


def get_year_1_winter_courses():
    return json_file["courses"]["year1"]["winter"]


def get_year_1_summer_courses():
    return json_file["courses"]["year1"]["summer"]


def get_year_2_winter_courses():
    return json_file["courses"]["year2"]["winter"]


def get_year_2_summer_courses():
    return json_file["courses"]["year2"]["summer"]


def get_year_3_winter_courses():
    return json_file["courses"]["year3"]["winter"]


def get_year_3_summer_courses():
    return json_file["courses"]["year3"]["summer"]


def get_chill_channels():
    return json_file["chill"]
