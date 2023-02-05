
from nextcord import Embed
from nextcord import Colour
import sys

sys.path.append("../")
from server_ids import *

class Courses_embed(Embed):
    def __init__(self, year1_courses: list[str], year2_courses: list[str], year3_courses: list[str]):
        title = "Enrolled Courses"
        super().__init__(colour=Colour.blue(), title=title)
        if len(year1_courses)>0:
            self.add_field(name="Year 1 Courses", value="")
            for course in year1_courses:
                self.add_field(
                    name="",
                    value=course,
                    inline=False
                )
        if len(year2_courses)>0:
            self.add_field(name="Year 2 Courses", value="")
            for course in year2_courses:
                self.add_field(
                    name="",
                    value=course,
                    inline=False
                )
        if len(year3_courses)>0:
            self.add_field(name="Year 3 Courses", value="")
            for course in year3_courses:
                self.add_field(
                    name="",
                    value=course,
                    inline=False
                )