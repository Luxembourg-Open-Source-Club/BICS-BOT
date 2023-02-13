# BICS-BOT 🤖
The **BICS bot's** source code may be found in this repository. Its primary goal is to automate the BICS server and provide users and students with a variety of ways to communicate with it.

The bot now supports text channel instructions including **help,** **role attribution**, and **enrolment/unenrolment** to courses.

## Table of Contents
- [Getting Started](#getting-started)
    - [Initial Setup](#initial-setup)
    - [Bot Deployment](#bot-deployment)
- [Commands Available](#commands-available)
    - [General Commands](#general-commands)
    - [Role Commands](#role-commands)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
    - [Steps to Contribute](#steps-to-contribute)
    - [Conventions to Follow](#conventions-to-follow)

## Getting Started
> This repo contains a python package **bics_bot** which is where all the logic is implemented. For this reason, you will need to install the package locally.
For this reason I advice you to install it using a python virtual environment.

### Initial Setup
1. Set up a python virtual environment (*ignore this command if you don't want to*)
    - `python3 -m env env`
1. Install the dependencies
    - `pip install -r requirements.txt`
1. Build the package
    - `python3 setup.py build`
1. Install the package
    - `python3 setup.py install`
1. Create a file .env in the root folder which contains the bot token as `TOKEN_BOT_CLONE=token`. To get the token, reach out to @Pedro. 

### Bot Deployment
In case you want to test what you have coded, you will need to deploy a bot. To do so, run `python main.py -c` from within the root directory of this repo. The `-c` specifies the program to launch the clone instead of the real bot.
Once the bot is running you should see a message `Bot is online`. 
Then, if you want to test a command that you have added, go to `#bot-dev-discussion` text channel in the BICS discord server. *(Note that you need to have the role `BotDev` to see this channel)*


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
**Any contributions are welcome!** 😉 If you desired to contribute, you can head to the issues tab and check if there are issues you want to 
address. In addition, you can also just leave issues as features requests, or bugs that you might have found.

### Steps to Contribute
1. Create your own bot. You can follow this (tutorial)[https://discord.com/developers/docs/getting-started] where you should go until *Adding scopres and permissions* section. When choosing the bot permissions, choose administrator.

1. Create the clone of the BICS discord server. The link for the template can be found in the **#bot-discussion** text channel in the pin messages.

1. Fork this repo.

1. If you are contributing to an issue make sure to notify that you will be working on that issue, to let others now that someone took that issue.

1. Create a branch where you will work on. The branch name should start with the type of change you want to do followed by a `/` and the description of the change. For example, say you want to add a new feature which adds a new command to the bot. Then the branch would look like `feature/new_command`. Another example would be if you want
to fix a but then the branch would be of the form `fix/...`

1. Once you have made your desired changes, you need to make sure that there are no bugs and everything works as expected. (Unless the changes do not affect the code itself, like documentation)

1. Create a pull request from your branch to the main branch of repo.

### Conventions to Follow
- All the commands should be seen only by the user that has called the command. This can be achieved by using the `ephemeral=True` parameter when sending a message. 
In case the command is supposed to be seen by everyone then the parameter needs to be set to false.

- Class names should follow the CamelCase naming convention

- Everything else than classes should follow the snacke_case naming convention

- The use of docstrings is encouraged to give a brief description of the functions to others 
