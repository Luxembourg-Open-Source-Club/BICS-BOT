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
            if member.id in (241589375190827018, 332622290665603072):
                return f"Happy Birthday to the one and only {member.mention}!\n @everyone Wish the King 👑 a happy birthday\n Or 👻 NG 👻 will curse you until the end of times ☠️☠️☠️☠️"

            messages = [
                f"Happy Birthday, {member.mention}!\nEven if your programming skills are trash, we still like you <3",
                f"{member.mention}, another year in BiCS?\n Nah, you're just trolling you should have lost your will to live since you joined the program. Happy Birthday tho!",
                f"Still didn't finished BiCS {member.mention}?\n Sorry for that, anyway, Happy Birthday!",
                f"{member.mention}, on your special day, remember one thing - your BSP is not finished yet!\n Happy Birthday ^^ !",
                f"Cheers to the birthday legend, {member.mention}! 🎂🎉 May your day be filled with cake, joy, and as many 'just one more slice' moments as your heart desires! 🍰🎈😁",
                f"{member.mention}, you're officially one year more fabulous! 🎉🥂 Don't count the candles; just enjoy the glow they bring. Happy Birthday, superstar!",
                f"Happy Birthday, {member.mention}! 🎂🎉 On this special day, may your life be as fantastic as a software update that takes no time to install and brings you only great features!",
                f"Another trip around the sun and still looking as radiant as ever, {member.mention}! 🌞🎂 Here's to a birthday that shines just as bright as you do! 🎉🌟",
                f"Happy Birthday, {member.mention}! 🎂🎈 Time to party like you're 29 (again)! 🎉 Age is just a number, and you're nailing it!",
                f"{member.mention}, you're the real MVP of birthdays! 🎂🎉 May your day be filled with epic moments, awesome surprises, and lots of cake. Happy Birthday!"
            ]

            return random.choice(messages)

        guild_id = self.client.guilds[0].id
        guild = self.client.get_guild(guild_id)
        general_id = get_channel_id_by_name(guild=guild, name="general")

        file_name = "./bics_bot/config/birthdays.json"

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
