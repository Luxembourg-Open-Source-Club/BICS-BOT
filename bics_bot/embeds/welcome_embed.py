from nextcord import Embed
from nextcord import Colour


class WelcomeEmbed(Embed):
    """
    Discord embed which contains a welcome message to a new user.
    """

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
                To do so, use the **/intro** command and enter you **name**, **surname** and **year**. (In case you are and erasmus student or a global exchange student choose erasmus as the year)\n
                **2.** Take a look at **#🧭nav-guide**. It contains some relevant descriptions of the currently available channels.\n
                **3.** Enjoy🙃
        """
