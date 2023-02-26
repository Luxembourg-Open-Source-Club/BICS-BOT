import nextcord
from nextcord.ext import commands
from nextcord import application_command, Interaction

import csv
import time, datetime

from bics_bot.embeds.logger_embed import WARNING_LEVEL, LoggerEmbed
from bics_bot.config.server_ids import GUILD_BICS_ID, GUILD_BICS_CLONE_ID

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
        type: str = nextcord.SlashOption(description="The type of event.", required=True, choices={"Homework": "Homework", "Midterm": "Midterm", "Quiz": "Quiz", "Final": "Final"}),
        course: str = nextcord.SlashOption(description="For example; Linear Algebra 1", required=True),
        graded: bool = nextcord.SlashOption(description="Is this event graded?", required=True, choices={"True": True, "False": False}),
        deadline_date: str = nextcord.SlashOption(description="Date format: <DAY.MONTH.YEAR>. Example (June 5th, 2023): 05.06.2023", required=True),
        deadline_time: str = nextcord.SlashOption(description="Time format: <HOUR:MINUTE>. Use 24-hour clock. Examples: 09:30, 15:45, 00:00, 23:59", required=True),
        location: str = nextcord.SlashOption(description="Room of the event. For example: MSA 3.050", required=False)
    ) -> None:
        fields, rows = self.read_csv()
        year = self.get_user_year(interaction)
        rows.append([type, course, graded, deadline_date, deadline_time, location, year])
        self.write_csv(fields, rows)
        
        await interaction.response.send_message(
            embed=LoggerEmbed("Confirmation", f"Data added to calendar.\n\nType: {type}\nCourse: {course}\nGraded: {graded}\nDeadline Date: {deadline_date}\nDeadline Time: {deadline_time}\nLocation: {location}", WARNING_LEVEL),
            ephemeral=True,
        )
        return

    def read_csv(self):
        fields = []
        rows = []
        with open(CALENDAR_FILE_PATH, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)        
            for row in csvreader:
                rows.append(row)
        return (fields, rows)
    
    def write_csv(self, fields, rows) -> None:
        with open(CALENDAR_FILE_PATH, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
    
    def get_unixtime(self, deadline_date:str, deadline_time:str) -> int:
        deadline_date = deadline_date.split(".")
        deadline_time = deadline_time.split(":")
        d = datetime.datetime(int(deadline_date[2]), int(deadline_date[1]), int(deadline_date[0]), int(deadline_time[0]), int(deadline_time[1]))
        unixtime = int(time.mktime(d.timetuple()))
        return unixtime
    
    def get_user_year(self, interaction:Interaction) -> str:
        for role in interaction.user.roles:
            if role.name.startswith("Year"):
                return role.name

def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(CalendarCmd(client))
