# BICS-BOT 🤖
The **BICS-BOT**'s source code can be found in this repository. Its primary goal is to automate the BICS Discord server tasks, and provide students with simple ways to interact with the server.

You can run `/help` on the server the bot is present, and see the capabilities of it.

## Table of Contents
- [Bot Deployment](#bot-deployment)
- [Commands Available](#commands-available)
    - [General Commands](#general-commands)
    - [Role Commands](#role-commands)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
    - [Conventions to Follow](#conventions-to-follow)

## Contribution
Please refer to the [contribution documentation](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT/blob/main/.github/CONTRIBUTING.md) for a complete guide on getting everything set up on your local machine.

## Commands Available
> All commands can be used in any channel as only the user that requests for one is able to see the bot messages.

### General Commands
- `/help`: This command is used to view the list of the available bot commands.
  
- `/useful_links`: This command is used to view a list of some links that might be useful for a BICS student, such as the BSP enrollment form.

- `/intro` (Only for new members): Allows a new member to get the **Student** role, to change your server useername to comply with the server format (Example: John Doe -> John D), and to introduce themselves. This command can only be used in the introduction channel (`#starting-up`).

- `/enroll`: This command is used for students who wish to get viewing permissions to the text channels of their courses.

- `/unenroll`: This command is used for students who wish to remove their viewing permissions to the text channels of the courses they are no longer taking.

- `/update`: This command is used to update the students current bachelor year. For example, if you are in year 1, then this command will update the year you are in to year 2.

- `/calendar_add`: This command is used to let a student enter their homework or exams into the calendar where the student can also add additional details.

- `/calendar_delete`: This command is used to let a student delete entries they have made from the calendar

- `/create_study_group`: This command is used to let students create private text and voice channel for their study groups.

### Role Commands

- `/gamer`: Gives or removes the **Gamer** role, which also gives access to the *#games* text channel to communicate with other gamers in the server.

- `/harem`: Gives or removes the **Harem** role, which also gives access to the *#harem* text channel to collect harem cards.

- `/botdev`: Gives or removes the **BotDev** role, which also gives access to the *#bot-dev-discussion* text channel.

### Conventions to Follow
- All the commands should be seen only by the user that has called the command. This can be achieved by using the `ephemeral=True` parameter when sending a message. 
In case the command is supposed to be seen by everyone then the parameter needs to be set to false.

- Class names should follow the `PascalCase` naming convention

- Everything else should follow the `snake_case` naming convention

- Use docstrings for your functions.
