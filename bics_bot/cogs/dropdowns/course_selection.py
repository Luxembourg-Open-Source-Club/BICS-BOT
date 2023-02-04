from nextcord.ext import commands
from nextcord import SelectOption, application_command
import nextcord
from nextcord.ui import Select, View

BICS_GUILD_ID = 753535223798562886
BICS_CLONE_GUILD_ID = 1014558774532509777

courses_list = [
    "Web Development 1",
    "BSP 1",
    "Analysis For Applications",
    "Discrete Mathematics 1",
    "Programming Fundamentals 1",
    "Linear Algebra 1",

    "Theoretical Computer Science 1",
    "Computer Infrastructures",
    "Network and Communications",
    "Programming Fundamentals 2",
    "Linear Algebra 2",

    "Discrete Mathematics 2",
    "Programming Fundamentals 3",
    "Information Management 1",
    "Algorithms and Complexity",
    "Security 1",

    "Online Course 4",
    "Programming Languages",
    "Intelligent Systems 1",
    "Information Management",
    "Theoretical Computer Science 2",
    "Online Course 5",

    "Web Development 2",
    "Software Engineering 1",
    "Natural Language Processing",
    "Human Computer Interaction",
    "Computational Science 2",
    "Computational Science 1",

    "Online Course 6",
    "User Centered Design",
    "Intelligent Systems 2",
    "Computational Science 3",
    "Data Science for Humanities",
    "Security 2",
    "Software Engineering 2"
]

courses_dict = {
    "Web Development 1": "#887777232129507408",
    "BSP 1": "#753552513692860426",
    "Analysis For Applications": "#753552381743988787",
    "Discrete Mathematics 1": "#753552413360783371",
    "Programming Fundamentals 1": "#753552472852660274",
    "Linear Algebra 1": "#753552440615370762",

    "Theoretical Computer Science 1": "#808338690056519750",
    "Computer Infrastructures": "#808339964941041664",
    "Network and Communications": "#808339920287432714",
    "Programming Fundamentals 2": "#808338944705298473",
    "Linear Algebra 2": "#808339998398742528",

    "Discrete Mathematics 2": "#888144768587161600",
    "Programming Fundamentals 3": "#888144574768361553",
    "Information Management 1": "#888144526034751549",
    "Algorithms and Complexity": "#888144413497380895",
    "Security 1": "#888144273395056720",

    "Online Course 4": "#943453536350502913",
    "Programming Languages": "#943453508319969341",
    "Intelligent Systems 1": "#939222983132712991",
    "Information Management": "#939222959065792532",
    "Theoretical Computer Science 2": "#939222927918923816",
    "Online Course 5": "#1024024091751100466",

    "Web Development 2": "#985958042669559928",
    "Software Engineering 1": "#985957970246508577",
    "Natural Language Processing": "#985957640268042290",
    "Human Computer Interaction": "#985957576279724182",
    "Computational Science 2": "#985957424190095390",
    "Computational Science 1": "#985957321446424586",

    "Online Course 6": "#1024024040748372018",
    "User Centered Design": "#985958699573059685",
    "Intelligent Systems 2": "#985958634573930546",
    "Computational Science 3": "#985958555800727582",
    "Data Science for Humanities": "#985958503111872614",
    "Security 2": "#985958450162970624",
    "Software Engineering 2": "#985958402620534795",
}


class DropdownView(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_command.slash_command(
        guild_ids=[BICS_GUILD_ID, BICS_CLONE_GUILD_ID],
        description="Courses Selection.",
    )
    async def courses(self, interaction: nextcord.Interaction):
        user = interaction.user
        user_roles = user.roles
        print("LEN", len(courses_list))

        if len(user_roles) == 1:
            # - Means the user already has at least one role
            await interaction.response.send_message(
                f"You haven't yet introduced yourself! Make sure you use the **/intro** command first",
                ephemeral=True,
            )
        else:
            options_ = []
            for course in courses_list:
                options_.append(SelectOption(label=course))
            menu = Select(options=options_,
                          max_values=len(courses_list))
            view = View()
            view.add_item(menu)
            await interaction.response.send_message(view=view)


def setup(client):
    client.add_cog(DropdownView(client))
