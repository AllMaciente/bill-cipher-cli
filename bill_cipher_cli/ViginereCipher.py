import typer
from rich import print

try:
    from .utils import alfbet, coretion
except:
    from utils import alfbet, coretion


def keyMatcheLength(key, text):
    keyReturn = ""
    n = 0
    for i in range(len(text)):
        if text[i] in alfbet:
            index = n % len(key)
            keyReturn += key[index]
            n += 1
        elif text[i] == " ":
            keyReturn += " "
        elif text[i] == "\n":
            keyReturn += "\n"
        else:
            keyReturn += "*"
    return keyReturn


def encrpyt(text, key, space: bool = False): ...
