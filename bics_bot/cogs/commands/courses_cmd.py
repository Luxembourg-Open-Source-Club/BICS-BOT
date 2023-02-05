from nextcord.ext import commands
from nextcord import application_command
import nextcord
import json
from bics_bot.dropdowns.course_selection_dropdown import DropdownView
from bics_bot.config.server_ids import GUILD_BICS_ID

with open("./bics_bot/data/discord_channels.json") as f:
    text_channels = json.load(f)

courses_list = []
for year in text_channels["courses"].values():
    for sem in year.values():
        for course in sem:
            courses_list.append(course["name"])


class CoursesCmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID],
        description="Courses Selection.",
    )
    async def courses(self, interaction: nextcord.Interaction):
        user = interaction.user
        guild = interaction.guild

        if len(user.roles) == 1:
            # Means the user only has the default @everyone role, and nothing else.
            await interaction.response.send_message(
                f"You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )
        else:
            enrolled_courses = self.get_courses_enrolled(user, guild)
            view = DropdownView(enrolled_courses=enrolled_courses)
            disclaimer_message = """ATTENTION\n\nIf you do not make any new choices in a the dropdown menus, the courses that \"seem\" like they are chosen in that menu will be reset. If you do not want to lose access to those courses; go in that dropdown menu, and select, then unselect a course, so that your chosen courses are updated."""
            await interaction.response.send_message(content=disclaimer_message, view=view, ephemeral=True)

    def get_courses_enrolled(self, user: nextcord.Interaction.user, guild: nextcord.Guild):
        enrolled = []
        channels = guild.text_channels
        for channel in channels:
            if channel.name not in courses_list:
                continue
            if user in channel.members:
                enrolled.append(channel.name)
        return enrolled


def setup(client):
    client.add_cog(CoursesCmd(client))
