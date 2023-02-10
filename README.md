# BICS-BOT
This repo contains the source code of the **BICS bot**. It's main purpose is to automate the server and to give the users/students different ways
to interact with the server as well.

## Table of Contents
- [Getting Started](#getting-started)
- [Commands Available](#commands-available)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
    - [Steps to Contribute](#steps-to-contribute)

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
1. Create a file .env in the root folder which contains the bot token as `BOT_TOKEN=token`. This token you can get from the bot you create.
1. The `bics_bot/config/server_ids.py` file needs to be updated so that it contains the right codes of your developmet server.


## Commands Available
> All commands can be used in any channel as only the user that requests for one is able to see the bot messages.

- `/help`: Displays the list of the available bot commands.
  
- `/intro` (Only for new members): Allows new member to set their roles and to introduce themselves. This command can only be used in the introduction channel.

- `/gamer`: Gives the `Gamer` role, which also gives access to the gamer channel to communicate with other gamers in the server.

- `/harem`: Gives the `Harem` role, which also gives access to the harem channel to collect harem cards.

- `/useful_links`: Shows some links that might be useful, such as the BSP enrolment form.

- `/courses`: Allows the user to select the course channels they are currently taking.

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
