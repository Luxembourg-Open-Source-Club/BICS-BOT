from nextcord import Member
from nextcord.ext import commands, tasks
import asyncio
import datetime

from bics_bot.embeds.welcome_embed import WelcomeEmbed


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
        self.check_birthday.start()

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        """This method represents the event which gets triggered once a new
        user joins the server.
        """
        server = await self.client.fetch_guild(member.guild.id)

        await member.send(embed=WelcomeEmbed(member.display_name, server.name))

    @tasks.loop(time=datetime.time(15, 3, tzinfo=datetime.timezone.utc))
    async def check_birthday(self):
        """This method represents the event which gets triggered once a new
        user joins the server.
        """
        channel = self.client.get_channel(1162419330277986354)
        date = datetime.datetime.now()
        print("Sending message")
        print(date)

        await channel.send("Hello World!")


def setup(client):
    """Function used to setup nextcord cogs"""
    client.add_cog(OnEvents(client))
