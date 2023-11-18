import csv
from bics_bot.utils.channels_utils import get_unixtime, get_user_year
from bics_bot.config.server_ids import MESSAGE_CALENDAR_ID, CHANNEL_CALENDAR_ID
from bics_bot.embeds.logger_embed import LoggerEmbed

PATH_CALENDAR = "./bics_bot/data/calendar.csv"


class CalendarEntry:
    """
    This class allows to get calendar entries to put into or remove from the calendar.

    Attributes:
        type: type of event to add in calendar
        course: course related to the event
        graded: is it graded or not
        deadline_date: deadline_date of the event
        deadline_time: deadline_time of the event
        location: room of the event
        year: corresponding class year of the event
    """
    def __init__(
        self,
        type,
        course,
        graded,
        deadline_date,
        deadline_time,
        location,
        year,
    ) -> None:
        self.type = type
        self.course = course
        self.graded = graded
        self.deadline_date = deadline_date
        self.deadline_time = deadline_time
        self.location = location
        self.year = year

    def get_columns(self) -> str:
        """
        This method gets columns of the entry.
        """
        return [
            "type",
            "course",
            "graded",
            "deadline_date",
            "deadline_time",
            "location",
            "year",
        ]

    def as_list(self):
        """
        This method allows to get the columns of entry as a list.
        """
        return [
            self.type,
            self.course,
            self.graded,
            self.deadline_date,
            self.deadline_time,
            self.location,
        ]

    def __str__(self) -> str:
        """
        This method transforms the deadline_date and deadline_time into unix_time
        """
        unix_time = get_unixtime(self.deadline_date, self.deadline_time)
        return f"{self.course} **{self.type}** on <t:{unix_time}:F>"


class Calendar:
    """
    This class allows to enter or even delete entries into the calendar.
    """
    def __init__(self) -> None:
        self.entries: list(CalendarEntry) = []
        self.fields = [
            "type",
            "course",
            "graded",
            "deadline_date",
            "deadline_time",
            "location",
            "year",
        ]
        self._import_calendar()

    def retrieve_entries(self):
        """
        Retrieves entries.
        """
        return self.entries

    def add_entry(
        self,
        type,
        course,
        graded,
        deadline_date,
        deadline_time,
        location,
        year,
    ):
        """
        Adds entry to the list of entries we need.
        """
        self.entries.append(
            CalendarEntry(
                type,
                course,
                graded,
                deadline_date,
                deadline_time,
                location,
                year,
            )
        )

    def remove_entry(self, entry):
        """
        Removes entry from the list of entries we need.
        """
        for i, e in enumerate(self.entries):
            if e == entry:
                self.entries.pop(i)

    async def update_caledar_text_channel(self, interaction):
        """
        Updates the calendar text channel from the entries.

        Args:
            interaction: Gives meta information about the interaction.
        """
        channel = None
        if (
            get_user_year(interaction.user) == "Year 1"
            or get_user_year(interaction.user) == "Year 2"
            or get_user_year(interaction.user) == "Year 3"
        ):
            channel = interaction.guild.get_channel(CHANNEL_CALENDAR_ID)
        else:
            await interaction.response.send_message(
                embed=LoggerEmbed(
                    "Warning", "You can't do that.", WARNING_LEVEL
                ),
                ephemeral=True,
            )
            return

        message = await channel.fetch_message(MESSAGE_CALENDAR_ID)
        await message.edit(content=self.__str__())

    def _import_calendar(self):
        """Imports the calendar from a csv file"""
        with open(PATH_CALENDAR, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            _ = next(csvreader)
            for row in csvreader:
                self.entries.append(
                    CalendarEntry(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6] if len(row) == 7 else "",
                    )
                )

    def export_calendar(self):
        """Exports the current calendar to a csv file"""
        with open(PATH_CALENDAR, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.fields)
            for entry in self.entries:
                csvwriter.writerow(entry.as_list())

    def __str__(self) -> str:
        """
        Shows the calendar.
        """
        msg = "***__THE BICS CALENDAR__***\n"
        for entry in self.entries:
            msg += f"{entry}\n"
        return msg
