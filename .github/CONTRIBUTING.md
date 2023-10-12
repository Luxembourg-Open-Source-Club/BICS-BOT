# Welcome to BICS-BOT contributing guide
Thank you for investing your time in contributing to our project! Any contribution you make will be reflected on [BICS-BOT](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT) :sparkles:.

In this guide you will get an overview of how to set up your development environment and what the contribution workflow looks like if you are open-source newbie :)

## Table of Contents

- [Technical Requirements Before Starting](#technical-requirements-before-starting)
- [New Contributor Guide](#new-contributor-guide)
- [Setting Up Testing Environment](#setting-up-testing-environment)
  - [Bot Creation FAQ](#bot-creation-faq)
    - [What should the name of my testing bot be?](#what-should-the-name-of-my-testing-bot-be)
    - [What priviliges should I give to my testing bot in the Bot section?](#what-priviliges-should-i-give-to-my-testing-bot-in-the-bot-section)
    - [Where do I get the token for my testing bot?](#where-do-i-get-the-token-for-my-testing-bot)
    - [What Bot Permissions should I choose in the URL Generator section?](#what-bot-permissions-should-i-choose-in-the-url-generator-section)
- [Setting Up Development Environment](#setting-up-development-environment)
- [Running the Bot](#running-the-bot)
- [Issues](#issues)
  - [Create a New Issue](#create-a-new-issue)
  - [Solve an Issue](#solve-an-issue)
  - [Pull Requests](#pull-requests)

## Pre-Requisites
- Linux (recommended) or macOS are fine. Use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) if on Windows. 
- Python3.9>=

Check out our [technical guide](https://github.com/Luxembourg-Open-Source-Club/guides/tree/main) for help with setting up your OS, and learning about `git` and `bash` (Linux terminal) if you are unfamiliar with these software.

## Setting up Development Environment
This process should take roughly 15 minutes. Steps 12-17 are directed at absolute beginners; if you are experienced with development, feel free to skip. Steps 18 and 19 are still very necessary. However, everything in this section is still recommended.

If you see text like `$ sudo apt update`, that means this is a *Bash command*. You can copy and paste the text **after the $ sign**.
1. Create your own server by using the [BICS Discord server template](https://discord.new/ymnNrwxGJHNf).
2. Go to [this link](https://discord.com/developers/docs/getting-started)
3. Click `Create a new app`. Give your bot any name you want.
4. Navigate to the `Bot` page on the left-side sidebar.
5. Click `Reset Token`. Save the token somewhere and don't lose it.
6. Scroll down, and toggle all three options under **Privileged Gateway Intents**. (Presence Intent, Server Members Intent, Message Content Intent)
7. Scroll down more, enabled the `Administrator` option in the **Bot Permissions** section.
8. Navigate to the `OAuth2/URL Generator` page on the left-side sidebar.
9. In the **Scopes** section enable `bot` and `application.commands` options. In the section below, **Bot Permissions**, enable the `Administrator` option.
10. Copy and paste the link at the bottom of the page to your browser.
11. Invite the bot to the new server you created at Step 1.
12. [Fork](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT/fork) the repository.
13. Clone the repository to your machine.
14. Navigate to the root of the repository in your terminal.
15. Install the `python3-venv` package *if you are on Linux*. For example; `$ sudo apt install python3-venv` for Ubuntu/Debian users.
16. Create a **Python Virtual Environment**. `$ python3 -m venv .venv`. This command will create a sandbox Python installation just for this project in a folder named `.venv` at the root of the prepository.
17. Activate the virtual environment. `$ source .venv/bin/activate`.
18. Install requirement. `$ pip install -r requirements.txt`
19. Install your bot's token which you saved before using the command below. Replace the placeholder with your own token. Do not put it in any brackets, quotes, etc.
- `$ touch .env && echo TOKEN_BOT=<PLACE YOUR TOKEN HERE> >> .env`

### Running the Bot
Navigate into the `src` directory, and run `main.py`. `$ cd src && python3 main.py` if you are at the root of the project (which you should be if you followed our steps). You should get feedback in the terminal, and your bot should become online on the test Discord server.

### So what can I do now?
Now, any changes you make on the source code will be reflected on your own bot on your own test server. You can make your implementations and play around with them in this testing environment. You are ready to start contributing!

We strongly suggest you take a look at our [issues](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT/issues). These are our TODO items, new features, and needed bug-fixes.

Feel free to open new issues for things you want to work on.

## How to submit your changes
You can do a **Pull Request** to send us your work. When you are done implementing your changes, go to your fork's Github repository, and press `Contribute`.