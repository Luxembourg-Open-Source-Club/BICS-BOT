# BICS-BOT
This repo contains the source code of the **BICS bot**. It's main purpose is to automate the server and to give the users/students different ways
to interact with the server as well.

## Table of Contents
- [Getting Started](#getting-started)
- [Commands Available](#commands-available)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Getting Started
> This repo contains a python package **bics_bot** which is where all the logic is implemented. For this reason, you will need to install the package locally.
For this reason I advice you to install it using a python virtual environment.

1. Set up a python virtual environment (*ingore this command if you don't want to*)
    - `python3 -m env env`
1. Install the dependencies
    - `pip install -r requirements.txt`
1. Build the package
    - `python3 setup.py build`
1. Install the package
    - `python3 setup.py install`
1. Run the bot
    - `python3 main.py`


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
