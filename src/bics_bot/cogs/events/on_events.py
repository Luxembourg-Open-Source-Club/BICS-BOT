from nextcord import Member, guild
from nextcord.ext import commands, tasks
import nextcord
from bics_bot.embeds.welcome_embed import WelcomeEmbed
from bics_bot.utils.server_utilities import get_member_by_id
from bics_bot.config.server_ids import GUILD_BICS_ID

import json
import datetime

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

        guild_id = self.client.guilds[0].id
        guild = self.client.get_guild(guild_id)
        #member = get_member_by_id(guild=guild, id=)
        for birthday in data.keys():
            birthday_f = birthday.split(".")[0:2]
            birthday_f = ".".join(birthday_f)
            if str(birthday_f) == str(today):
                id = data[birthday][0]
                print(id)
                print(guild.members)
                member = get_member_by_id(guild=guild, id=id)
                print(f"Happy birthday, {member.display_name}")


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(OnEvents(client))
