import json

with open("./discord_channels.json") as f:
    json_file = json.load(f)


class Loader:
    def __init__(self, path):
        json_file = json.load(open(path))

    def get_year_1_winter_courses(self):
        return json_file["courses"]["year1"]["winter"]

    def get_year_1_summer_courses(self):
        return json_file["courses"]["year1"]["summer"]

    def get_year_2_winter_courses(self):
        return json_file["courses"]["year2"]["winter"]

    def get_year_2_summer_courses(self):
        return json_file["courses"]["year2"]["summer"]

    def get_year_3_winter_courses(self):
        return json_file["courses"]["year3"]["winter"]

    def get_year_4_summer_courses(self):
        return json_file["courses"]["year3"]["summer"]

    def get_chill_channels(self):
        return json_file["chill"]
