# BICS-BOT 🤖
The **BICS bot's** source code may be found in this repository. Its primary goal is to automate the BICS Discord server and provide users and students with a variety of ways to interact with it.

The bot now supports text channel instructions including **help,** **role attribution**, and **enrolment/unenrolment** to courses.

## Table of Contents
- [Bot Deployment](#bot-deployment)
- [Commands Available](#commands-available)
    - [General Commands](#general-commands)
    - [Role Commands](#role-commands)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
    - [Conventions to Follow](#conventions-to-follow)

## Bot Deployment
Please refer to the **Testing Environment Setup** and **Development Environment Setup** sections in the [contribution documentation](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT/blob/main/.github/CONTRIBUTING.md).


## Commands Available
> All commands can be used in any channel as only the user that requests for one is able to see the bot messages.

### General Commands
- `/help`: This command is used to view the list of the available bot commands.
  
- `/useful_links`: This command is used to view a list of some links that might be useful for a BICS student, such as the BSP enrolment form.

- `/intro` (Only for new members): Allows a new member to get role and to introduce themselves. This command can only be used in the introduction channel (`#starting-up`).

- `/enroll`: This command is used for students who wish to get viewing permissions to the text channels of their courses.

- `/unenroll`: This command is used for students who wish to remove their viewing permissions to the text channels of the courses they are no longer taking.

- `/update`: This command is used to update the students year. For example, if you are in year 1, then this command will update the year to 2

### Role Commands

- `/gamer`: Gives the **Gamer** role, which also gives access to the *#games* text channel to communicate with other gamers in the server.

- `/harem`: Gives the **Harem** role, which also gives access to the *#harem* text channel to collect harem cards.

- `/botdev`: Gives the **BotDev** role, which also gives access to the *#bot-dev-discussion* text channel.


## Dependencies
- `nextcord`: python discord API
- `python-dotenv`: used to retrieve environment variables

## Contributing

Please refer to the [contribution documentation](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT/blob/main/.github/CONTRIBUTING.md).

### Conventions to Follow
- All the commands should be seen only by the user that has called the command. This can be achieved by using the `ephemeral=True` parameter when sending a message. 
In case the command is supposed to be seen by everyone then the parameter needs to be set to false.

- Class names should follow the PascalCase naming convention

- Everything else should follow the snake_case naming convention

- The use of docstrings is encouraged to give a brief description of the functions to others 
