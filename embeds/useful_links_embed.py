from nextcord import Embed
from nextcord import Colour
import sys

sys.path.append("../")
from server_ids import *


class Useful_links(Embed):
    def __init__(self):
        title = "Useful links"
        super().__init__(colour=Colour.blue(), title=title)
        self.add_field(
            name="The official BICS website (BICSHUB)",
            value=" https://bicshub.uni.lu/students",
            inline=False,
        )

        self.add_field(
            name=f"BSP Mini BMT",
            value=f" https://docs.google.com/presentation/d/1WOM1Ar2TMHOAnPMSWZBoIPSzV-DhqD8iMbubTAkZdxc/edit#slide=id.ge717729f34_1_0",
            inline=False,
        )

        self.add_field(
            name=f"BSP declaration",
            value=f" https://forms.office.com/Pages/ResponsePage.aspx?id=lZxaRJ0PU0mdsbxKRd0SIJLrg3822EtCpsSwGaQZf_9UOUlDVFc0SFBJWkoxNldEVE5UNEFHR1dTTC4u",
            inline=False,
        )

        self.add_field(
            name=f"BICS G-Drive",
            value=f" https://drive.google.com/drive/folders/19c6DncFbQeNdtWNftObjzDp9HBde5aKj?usp=sharing",
            inline=False,
        )

        self.add_field(
            name=f"Moodle",
            value=f" https://moodle.uni.lu/",
            inline=False,
        )
