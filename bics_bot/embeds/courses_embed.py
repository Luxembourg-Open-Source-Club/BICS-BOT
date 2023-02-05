
from nextcord import Embed
from nextcord import Colour
import sys

sys.path.append("../")
from server_ids import *

class Courses_embed(Embed):
    def __init__(self, courses: list[str]):
        super().__init__(colour=Colour.blue(), title="Enrolled Courses")
        if len(courses[0])>0:
            self.add_field(name="Year 1 Courses", value="")
            for course in courses[0]:
                self.add_field(
                    name="",
                    value=course,
                    inline=False
                )
        if len(courses[1])>0:
            self.add_field(name="Year 2 Courses", value="")
            for course in courses[1]:
                self.add_field(
                    name="",
                    value=course,
                    inline=False
                )
        if len(courses[2])>0:
            self.add_field(name="Year 3 Courses", value="")
            for course in courses[2]:
                self.add_field(
                    name="",
                    value=course,
                    inline=False
                )