import nextcord
import csv

from nextcord.interactions import Interaction
from bics_bot.embeds.logger_embed import LoggerEmbed, WARNING_LEVEL

CALENDAR_FILE_PATH = "./bics_bot/data/calendar.csv"

class EventsDropdown(nextcord.ui.Select):
    def __init__(self, user, rows):
        self.option_to_row = {}
        self._options = self._get_options(user, rows)

    def build(self):
        super().__init__(
            placeholder="Choose events to be deleted",
            min_values=0,
            max_values=len(self._options),
            options=self._options,
        )

    def _get_options(self, user, rows):
        options = []
        for row in rows:
            if row[-1] == self.get_user_year(user):
                options.append(
                    nextcord.SelectOption(
                        label=f"{row[1]} {row[0]} on {row[3]} at {row[4]}"
                    )
                )
                self.option_to_row[str(nextcord.SelectOption(label=f"{row[1]} {row[0]} on {row[3]} at {row[4]}"))] = row
        return options

    def get_user_year(self, user) -> str:
        for role in user.roles:
            if role.name.startswith("Year"):
                return role.name
    

class CalendarView(nextcord.ui.View):
    def __init__(self, user, fields, rows):
        super().__init__(timeout=5000)
        self.events = EventsDropdown(user, rows)
        self.fields = fields,
        self.rows: list = rows
        if len(self.events._options) > 0:
            self.events.build()
            self.add_item(self.events)
        

    @nextcord.ui.button(
        label="Confirm", style=nextcord.ButtonStyle.green, row=3
    )
    async def confirm_callback(
        self, button: nextcord.Button, interaction: nextcord.Interaction
    ):
        for row in self.events.values:
            if self.events.option_to_row[row] in self.rows:
                self.rows.remove(self.events.option_to_row[row])

        self.write_csv(self.fields, self.rows)

        msg = ""
        for row in self.events.values:
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
    
    def write_csv(self, fields, rows) -> None:
        with open(CALENDAR_FILE_PATH, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)