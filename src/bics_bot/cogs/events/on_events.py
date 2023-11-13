from nextcord import Member
from nextcord.ext import commands, tasks

from bics_bot.embeds.welcome_embed import WelcomeEmbed
from bics_bot.utils.server_utilities import get_member_by_id, get_channel_id_by_name

import json
import datetime
import random

class OnEvents(commands.Cog):
    """This class contains the events that should be triggered."""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """This method represents the event which gets triggered once the bot
        is fully active.
        """
        print("Bot is fully deployed and is now online!")
        self.birthday_check.start()

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        """This method represents the event which gets triggered once a new
        user joins the server.
        """
        server = await self.client.fetch_guild(member.guild.id)

        await member.send(embed=WelcomeEmbed(member.display_name, server.name))

    @tasks.loop(time=datetime.time(hour=7, minute=0, tzinfo=datetime.timezone(datetime.timedelta(hours=1), name="CEST")))
    async def birthday_check(self):
        """This method represents the loop that checks if any members have
        a birthday on the current date.
        """
        def birthday_message(member):
            """This method reads a random birthday message from a text file
            and returns in a proper format with replaced placeholders.
            """
            file_name = "./bics_bot/texts/birthday_messages.txt"

            with open(file_name, "r") as file:
                if member.id in (241589375190827018, 332622290665603072):
                    message = file.readline()
                else:
                    messages = file.readlines()[1:]
                    message = random.choice(messages)

            message = message.replace(r"\n", "\n").format(member = member.mention)

            return message

        guild_id = self.client.guilds[0].id
        guild = self.client.get_guild(guild_id)
        general_id = get_channel_id_by_name(guild=guild, name="general")

        file_name = "../db/birthdays.json"

        # Check if the JSON file exists
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        current_date = datetime.date.today()
        today = current_date.strftime("%d.%m")

        for birthday, ids in data.items():
            birthday_formatted = birthday.split(".")[0:2]
            birthday_formatted = ".".join(birthday_formatted)
            if birthday_formatted == today:
                for id in ids:
                    member = get_member_by_id(guild=guild, id=id)
                    await self.client.get_channel(general_id).send(birthday_message(member))


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(OnEvents(client))
