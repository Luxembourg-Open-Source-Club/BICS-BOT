import csv


def read_txt(path: str) -> str:
    """Returns the text from a text file as a string

    Args:
        path: path of the text file

    Returns:
        The text from the file as a string
    """
    text = ""
    with open(path, "r") as file:
        for line in file.readlines():
            text += line
    return text
