import nextcord
from nextcord import application_command, Interaction
from nextcord.ext import commands

from bics_bot.embeds.logger_embed import WARNING_LEVEL, LoggerEmbed

import re
import json


class BirthdayCmd(commands.Cog):
    """This class represents the command </birthday>

    The </bithday> command allows users to enter their birthday so
    the bot can remind people on the server about that user's birthday.

    Attributes:
        client: Required by the API, not directly utilized.
    """

    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        description="Receive birthday greetings from fellow BiCS students",
    )
    async def birthday(
        self,
        interaction: Interaction,
        birthday: str = nextcord.SlashOption(
            description="Your birthday in the format DD.MM.YYYY (e.g., 05.06.1990).",
            required=True
        ),
    ) -> None:
        
        user = interaction.user
        user_roles = user.roles

        if len(user_roles) == 1:
            # The user has no roles. So he must first use the /intro command
            msg = "You haven't yet introduced yourself! Make sure you use the **/intro** command first"
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
        )
            return
        
        valid_pattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$"
        # Check if entered birthday format is valid
        if re.match(valid_pattern, birthday) == None:
            msg = (
                "You entered an invalid birthday. Please follow the format **DD.MM.YYYY**"
            )
            await interaction.response.send_message(
                embed=LoggerEmbed("Warning", msg, WARNING_LEVEL),
                ephemeral=True,
            )
            return

        # Storing the user's birthday in JSON file
        if len(birthday) > 0:
            filename = "./bics_bot/config/birthdays.json"
            with open(filename, "r") as file:
                data = json.load(file)

            # Check if the user has already added their birthday before
            for _, ids in data.items():
                if user.id in ids:
                    # If the user ID is found for another existing birthday, remove it
                    ids.remove(user.id)
                    break

            if birthday in data:
                # If the new birthday already exists but the user ID doesn't, append the new user ID
                data[birthday].append(user.id)
            else:
                # If the new birthday is not in the data, create a new array with the user ID
                data[birthday] = [user.id]

            # Write the updated data back to the JSON file
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

        await interaction.response.send_message(
            embed=LoggerEmbed(
                "Birthday Added",
                f"Your birthday ({birthday}) has been added to your profile.",
            ),
            ephemeral=True,
        )

    
def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(BirthdayCmd(client))