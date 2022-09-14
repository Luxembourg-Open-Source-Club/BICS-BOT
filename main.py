import nextcord
from nextcord.ext import commands
import select_menus

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


@bot.command()
async def enrol(ctx):
    view = select_menus.ChannelSelectionView()
    await ctx.send(
        "Please make the selection of the courses you desired to access", view=view
    )


bot.run(TOKEN)
