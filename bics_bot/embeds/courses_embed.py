
from nextcord import Embed
from nextcord import Colour
import sys

sys.path.append("../")
from server_ids import *

class Courses_embed(Embed):
    def __init__(self, enrolled_courses: list[str]):
        title = "Enrolled Courses"
        super().__init__(colour=Colour.blue(), title=title)
        for course in enrolled_courses:
            self.add_field(
                name=course,
                inline=False
            )
