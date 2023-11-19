import logging


def setup_nextcord_logging():
    """
    Sets up the logging of the bot on the discord server.
    """
    logger = logging.getLogger("nextcord")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename="./logs/nextcord_logs.log", encoding="utf-8", mode="w"
    )
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)


def get_bot_logger():
    """
    Gets bot logger to be able to add handlers.
    """
    logger = logging.Logger("BICS-BOT", logging.INFO)
    handler = logging.FileHandler(
        filename="./logs/bot_logs.log", encoding="utf-8", mode="w"
    )
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)
    return logger
