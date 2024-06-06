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


def encrpyt(text, key, space: bool = False):
    text = coretion(text, space)
    key = coretion(key, space)
    key = keyMatcheLength(key, text)
    result = ""
    for n in range(len(text)):
        if text[n] == "":
            result += " "
        elif text[n] == "\n":
            result += "\n"
        else:
            ikey = alfbet.index(key[n])
            itxt = alfbet.index(text[n])
            i = (itxt + ikey) % 26
            result += alfbet[i]
    return result


def decrypt(text, key, space: bool = False):
    key = keyMatcheLength(key, text)
    result = ""
    for n in range(len(text)):
        if text[n] == " ":
            result += " "
        elif text[n] == "\n":
            result += "\n"
        else:
            ikey = alfbet.index(key[n])
            itxt = alfbet.index(text[n])
            i = (itxt - ikey) % 26
            result += alfbet[i]
    return result


def vigenere(text: str, key: str, mode, space: bool = False):
    match mode:
        case "e":
            return encrpyt(text, key, space)
        case "d":
            return decrypt(text, key)
