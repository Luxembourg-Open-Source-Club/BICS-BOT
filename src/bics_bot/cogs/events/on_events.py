from nextcord import Member
from nextcord.ext import commands, tasks

from bics_bot.embeds.welcome_embed import WelcomeEmbed

import json
import datetime

class OnEvents(commands.Cog):
    """This class contains the events that should be triggered."""

    def __init__(self, client):
        self.client = client
        self.birthday_check.start()

    @commands.Cog.listener()
    async def on_ready(self):
        """This method represents the event which gets triggered once the bot
        is fully active.
        """
        print("Bot is fully deployed and is now online!")

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        """This method represents the event which gets triggered once a new
        user joins the server.
        """
        server = await self.client.fetch_guild(member.guild.id)

        await member.send(embed=WelcomeEmbed(member.display_name, server.name))

    @tasks.loop(seconds=5.0)
    async def birthday_check(self):
        """This method represents the loop that checks if any members have
        a birthday on the current date.
        """
        filename = "./bics_bot/config/birthdays.json"
        with open(filename, "r") as file:
            data = json.load(file)

        current_date = datetime.date.today()
        today = current_date.strftime("%d.%m")

        for birthday in data.keys():
            birthday = birthday.split(".")[0:2]
            birthday = ".".join(birthday)
            if birthday == today:
                print("Happy birthday")


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(OnEvents(client))
