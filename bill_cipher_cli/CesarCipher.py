import typer
from rich import print

try:
    from .utils import alfbet, coretion
except:
    from utils import alfbet, coretion


def encryption(text: str, key: int, space: bool = False):
    """
    Encripta o texto usando a chave de encriptação.

    Parameters:
        text: o texto a ser encriptado.
        key: a chave de encriptação.
        space: se True, mantem os espaços.


    Examples:
        >>> encryption('thequickbrownfoxjumpsoverthelazydog',3)
        'wkhtxlfneurzqiramxpsvryhuwkhodcbgrj'
    """
    text = coretion(text, space)
    textEnctypt = ""
    for letter in text:
        if letter == " ":
            textEnctypt += " "
            continue
        if letter == "\n":
            textEnctypt += "\n"
            continue
        ind = alfbet.index(letter)
        ind = (ind + key) % 26
        textEnctypt += alfbet[ind]
    return textEnctypt


def decryption(text: str, key: int):
    """
    Decripta o texto usando a chave de decriptação.

    Parameters:
        text: o texto a ser decriptado.
        key: a chave de decriptação.


    Examples:
        >>> decryption('wkhtxlfneurzqiramxpsvryhuwkhodcbgrj',3)
        'thequickbrownfoxjumpsoverthelazydog'
    """
    textDecypt = ""
    for letter in text:
        if letter == " ":
            textDecypt += " "
            continue
        if letter == "\n":
            textDecypt += "\n"
            continue
        ind = alfbet.index(letter)
        ind = (ind - key) % 26
        textDecypt += alfbet[ind]
    return textDecypt


def CesarCipher(text: str, key: int, mode: str, space: bool = False):
    """
    Encripta ou decripta o texto usando a chave de encriptação.

    Parameters:
        text: o texto a ser encriptado ou decriptado.
        key: a chave de encriptação.
        mode: o modo de encriptação ou decriptação.

    Examples:
        >>> CesarCipher('thequickbrownfoxjumpsoverthelazydog',3,'e')
        'wkhtxlfneurzqiramxpsvryhuwkhodcbgrj'

        >>> CesarCipher('wkhtxlfneurzqiramxpsvryhuwkhodcbgrj',3,'d')
        'thequickbrownfoxjumpsoverthelazydog'
    """
    match mode:
        case "e":
            return encryption(text, key, space)
        case "d":
            return decryption(text, key)
        case _:
            raise ValueError("Mode must be e or d")


if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog"
    key = 3
    encryp = CesarCipher(text, key, "e")
    print(encryp)
    decryp = CesarCipher(encryp, key, "d")
    print(decryp)
