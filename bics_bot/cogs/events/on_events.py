import nextcord
import sys
from nextcord.ext import commands

sys.path.append("../../")
from server_ids import *
from embeds.welcome_embed import Welcome_embed


class OnEvents(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        server_name = await self.client.fetch_guild(member.guild.id)
        server_name = server_name.name

        await member.send(embed=Welcome_embed(member.display_name, server_name))


def setup(client):
    client.add_cog(OnEvents(client))
