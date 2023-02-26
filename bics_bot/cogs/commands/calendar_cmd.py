import nextcord
from nextcord.ext import commands
from nextcord import application_command, Interaction

import csv
import time
from datetime import datetime

from bics_bot.utils.channels_utils import (
    retrieve_courses_text_channels_names,
    calendar_auto_update,
)
from bics_bot.embeds.logger_embed import WARNING_LEVEL, LoggerEmbed
from bics_bot.config.server_ids import (
    GUILD_BICS_ID,
    GUILD_BICS_CLONE_ID,
    CHANNEL_CALENDAR_YEAR_1_ID,
    CHANNEL_CALENDAR_YEAR_2_ID,
    CHANNEL_CALENDAR_YEAR_3_ID,
    MESSAGE_CALENDAR_YEAR_3_ID,
)
from bics_bot.dropdowns.calendar_dropdown import CalendarView

CALENDAR_FILE_PATH = "./bics_bot/data/calendar.csv"


class CalendarCmd(commands.Cog):
    """This class represents the commands to interact with the calendar system.

    </calendar_add> will let students enter a HW or an exam into the calendar
        system with various details about the assignment/exam for their year.

    </calendar_delete> will let students remove multiple entries from the
        calendar from their year.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Allow students to enter a HW/exam into the calendar with info such as deadline.",
    )
    async def calendar_add(
        self,
        interaction: Interaction,
<<<<<<< HEAD
        type: str = nextcord.SlashOption(description="The type of event.", required=True, choices={"Homework": "Homework", "Midterm": "Midterm", "Quiz": "Quiz", "Final": "Final"}),
        course: str = nextcord.SlashOption(description="For example; Linear Algebra 1", required=True),
        graded: bool = nextcord.SlashOption(description="Is this event graded?", required=True, choices={"True": True, "False": False}),
        deadline_date: str = nextcord.SlashOption(description="Date format: <DAY.MONTH.YEAR>. Example (June 5th, 2023): 05.06.2023", required=True),
        deadline_time: str = nextcord.SlashOption(description="Time format: <HOUR:MINUTE>. Use 24-hour clock. Examples: 09:30, 15:45, 00:00, 23:59", required=True),
        location: str = nextcord.SlashOption(description="Room of the event. For example: MSA 3.050", required=False)
    ) -> None:                
=======
        type: str = nextcord.SlashOption(
            description="The type of event.",
            required=True,
            choices={
                "Homework": "Homework",
                "Midterm": "Midterm",
                "Quiz": "Quiz",
                "Final": "Final",
            },
        ),
        course: str = nextcord.SlashOption(
            description="For example; Linear Algebra 1", required=True
        ),
        graded: bool = nextcord.SlashOption(
            description="Is this event graded?",
            required=True,
            choices={"True": True, "False": False},
        ),
        deadline_date: str = nextcord.SlashOption(
            description="Date format: <DAY.MONTH.YEAR>. Example (June 5th, 2023): 05.06.2023",
            required=True,
        ),
        deadline_time: str = nextcord.SlashOption(
            description="Time format: <HOUR:MINUTE>. Use 24-hour clock. Examples: 09:30, 15:45, 00:00, 23:59",
            required=True,
        ),
        location: str = nextcord.SlashOption(
            description="Room of the event. For example: MSA 3.050",
            required=False,
        ),
    ) -> None:
>>>>>>> 4c833767cebc8ad41fbdbc78a7a0d289ba961932
        fields, rows = self.read_csv()
        year = self.get_user_year(interaction.user)
        rows.append(
            [
                type,
                course,
                graded,
                deadline_date,
                deadline_time,
                location,
                year,
            ]
        )
        self.write_csv(fields, rows)
        await calendar_auto_update(interaction)

        await interaction.response.send_message(
            embed=LoggerEmbed(
                "Confirmation",
                f"Data added to calendar.\n\nType: {type}\nCourse: {course}\nGraded: {graded}\nDeadline Date: {deadline_date}\nDeadline Time: {deadline_time}\nLocation: {location}",
                WARNING_LEVEL,
            ),
            ephemeral=True,
        )

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Allow students to remove a HW/exam from the calendar.",
    )
    async def calendar_delete(self, interaction: Interaction) -> None:
        fields, rows = self.read_csv()

        print("before constructing")
        view = CalendarView(interaction.user, interaction.guild, rows)
        print("after constructing")
        await interaction.response.send_message(
            view=view,
            ephemeral=True,
        )
        print("after displaying")

    @application_command.slash_command(
        guild_ids=[GUILD_BICS_ID, GUILD_BICS_CLONE_ID],
        description="Allow students to view their own calendar.",
    )
    async def calendar_view(self, interaction: Interaction) -> None:
        enrolled_courses = self.get_courses_enrolled(
            interaction.user,
            interaction.guild,
        )
        fields, rows = self.read_csv()
        msg = ""
        for row in rows:
            if row[1] in enrolled_courses:
                unixtime = self.get_unixtime(row[3], row[4])
                msg += (
                    f" > **{row[0]}** for *{row[1]}* on <t:{unixtime}:F>\n\n"
                )
        if msg == "":
            await interaction.response.send_message(
                content="No deadlines for you. Enjoy your free time :)",
                ephemeral=True,
            )
            return
        await interaction.response.send_message(content=msg, ephemeral=True)

    def get_courses_enrolled(
        self, user: Interaction.user, guild: Interaction.guild
    ) -> dict[str, bool]:
        """Retrieves the courses a student is enrolled to.

        Technically, it returns the courses that the student can view it by
        any means necessary (member level permission, role level permission,
        admin rights).

        Args:
            user: the user who is doing the </enroll> or <unenroll> request.
            guild: the server object, containing information on text channels
              necessary for this opeation

        Returns:
            dictionary where the keys are the courses the student can see
        """
        enrolled: dict[str, bool] = {}
        channels = guild.text_channels
        courses_channels_names = retrieve_courses_text_channels_names(guild)

        for channel in channels:
            if (
                channel.name in courses_channels_names
                and user in channel.members
            ):
                enrolled[channel.topic] = True
        return enrolled

    def read_csv(self):
        fields = []
        rows = []
        with open(CALENDAR_FILE_PATH, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
        return (fields, rows)

    def write_csv(self, fields, rows) -> None:
        with open(CALENDAR_FILE_PATH, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)

    def get_unixtime(self, deadline_date: str, deadline_time: str) -> int:
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

    def get_user_year(self, user) -> str:
        for role in user.roles:
            if role.name.startswith("Year"):
                return role.name


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(CalendarCmd(client))
