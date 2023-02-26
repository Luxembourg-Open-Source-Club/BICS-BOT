import nextcord
import csv

from nextcord.interactions import Interaction
from bics_bot.embeds.logger_embed import LoggerEmbed, WARNING_LEVEL
from bics_bot.utils.channels_utils import calendar_auto_update, retrieve_courses_text_channels_names

CALENDAR_FILE_PATH = "./bics_bot/data/calendar.csv"

class EventsDropdown(nextcord.ui.Select):
    def __init__(self, user, guild, rows):
        self.option_to_row = {}
        self._options = self._get_options(user, guild, rows)

    def build(self):
        super().__init__(
            placeholder="Choose events to be deleted",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, user, guild, rows):
        options = []
        enrolled_courses = self.get_courses_enrolled(user, guild)
        for row in rows:
            if row[1] in enrolled_courses:
                options.append(
                    nextcord.SelectOption(
                        label=f"{row[1]} {row[0]} on {row[3]} at {row[4]}"
                    )
                )
                self.option_to_row[str(nextcord.SelectOption(label=f"{row[1]} {row[0]} on {row[3]} at {row[4]}"))] = row
        return options
    
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
            if channel.name in courses_channels_names and user in channel.members:
                enrolled[channel.topic] = True
        return enrolled

    def get_user_year(self, user) -> str:
        for role in user.roles:
            if role.name.startswith("Year"):
                return role.name
    

class CalendarView(nextcord.ui.View):
    def __init__(self, user, guild, rows):
        super().__init__(timeout=5000)
        self.events = EventsDropdown(user, guild, rows)
        if len(self.events._options) > 0:
            self.events.build()
            self.add_item(self.events)
        

    @nextcord.ui.button(
        label="Confirm", style=nextcord.ButtonStyle.green, row=3
    )
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        fields, rows = self.read_csv()
        for row in self.events.values:
            if self.events.option_to_row[row] in rows:
                rows.remove(self.events.option_to_row[row])

        print("before writing")
        self.write_csv(fields, rows)
        await calendar_auto_update(interaction)

        msg = ""
        for row in self.events.values:
            row = self.events.option_to_row[row]
            msg += "The following events are deleted:\n\n"
            msg += f" > {row[1]} {row[0]} on {row[3]} at {row[4]}\n"

        await interaction.response.send_message(
            embed=LoggerEmbed("Confirmation", msg, WARNING_LEVEL),
            ephemeral=True,
        )
        
    @nextcord.ui.button(
        label="Cancel",
        style=nextcord.ButtonStyle.red,
        row=3
    )
    async def cancel_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        await interaction.response.send_message(
            "Canceled operation. No changes made.", ephemeral=True
        )
        self.stop()

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

    def get_user_year(self, user) -> str:
        for role in user.roles:
            if role.name.startswith("Year"):
                return role.name