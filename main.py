import os
from pickle import EMPTY_DICT
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands


def setup_logging():
    import logging

    logger = logging.getLogger("nextcord")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename="./logs/bot_logs.log", encoding="utf-8", mode="w"
    )
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)


load_dotenv()
setup_logging()

# - Loading intents
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot_description = "THE BICS BOT. To be completed"

bot = commands.Bot(command_prefix="!", description=bot_description, intents=intents)


@bot.event
async def on_ready():
    print(f"The BOT is now ready!")


@bot.event
async def on_member_join(member: nextcord.Member):
    print(f"{member} has joined the server")
    embed = nextcord.Embed(color=nextcord.Color.blue())
    embed.title = "Welcome👋"
    embed.description = f"""Hey **@{member.display_name}** and welcome to **BICS Student Server**, the **official BICS** discord server!\n
    In this server you will be able to find other BICS students, discuss course related material and much more!"""
    getting_started_value = """
        **1.** In order to get granted the full server access, you will need to get a role. To do so, head to **#💡starting-up** channel and present yourself with your name and what year you will be in. **Feel free to ping an @Admin!** \n
        **2.** Change your server name to your **real** name (ex: first name + first letter of last name). This way anyone can identify you easily 😉.\n
        **3.** Take a look at **#🧭nav-guide**. It contains some relevant descriptions of the channels.\n
        **4.** Enjoy🙃
    """
    embed.add_field(name="Getting Started", value=getting_started_value, inline=False)
    embed.add_field(
        name="The Official BICS Website", value="https://bicshub.uni.lu/", inline=False
    )

    await member.send(embed=embed)


bot.run(os.getenv("BOT_TOKEN"))
