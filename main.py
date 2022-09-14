from typing import List
import nextcord
from nextcord.ext import commands
from course_selection import DropdownView

TOKEN = "MTAxOTMzMDAwMTI5MzgxMTcyMg.GvqXBX.xgY_EZJhXyWhnbaevfu2MYD4Qsw4XuBXra6PEQ"

description = "BICS bot that manages the access to courses channels."

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------------")


@bot.slash_command()
async def enrol(interaction: nextcord.Interaction):
    view = DropdownView()
    await interaction.send("Select the courses!", view=view, ephemeral=True)


bot.run(TOKEN)
