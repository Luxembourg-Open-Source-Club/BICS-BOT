from nextcord import Embed
from nextcord import Colour


class Welcome_embed(Embed):
    def __init__(self, user_name, server_name):
        title = "Welcome on board👋"
        description = f"""Hey **@{user_name}** and welcome to **{server_name}**, the **official BICS** discord server!\n
            In this server you will be able to find other BICS students, discuss course related material and much more!"""
        super().__init__(colour=Colour.blue(), title=title, description=description)
        self.add_field(
            name="Getting started", value=self.getting_started_field(), inline=False
        )
        self.add_field(
            name="The Official BICS Website",
            value="https://bicshub.uni.lu/",
            inline=False,
        )

    def getting_started_field(self):
        return """
                **1.** In order to get granted the full server access, you will need to get a role.
                To do so, head to **#💡starting-up** channel and present yourself with your name and what year you will be in. **Feel free to ping an @Admin!** \n
                **2.** Change your server name to your **real** name (ex: first name + first letter of last name). This way anyone can identify you easily 😉.\n
                **3.** Take a look at **#🧭nav-guide**. It contains some relevant descriptions of the channels.\n
                **4.** Enjoy🙃
        """
