import typer
from rich import print

try:
    from .utils import alfbet, coretion
except:
    from utils import alfbet, coretion


def keyMatcheLength(key: str, text: str):
    """
    repetindo a chave até ter o comprimento do texto a cifra

    Parameters:
        key: a chave base
        text: o texto a ser cifrado

    Examples:
        >>> keyMatcheLength('LIMAO', 'ATACARBASESUL')
        'LIMAOLIMAOLIM'
    """
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


def encrpyt(text: str, key: str, space: bool = False):
    """
    Encripta o texto usando a chave de encriptação.

    Parameters:
        text: o texto a ser encriptado.
        key: a chave de encriptação.
        space: se True, mantem os espaços.

    Examples:
        >>> encrpyt('atacar base Sul', 'limao', True)
        'lbmcoc jmss dcx'
        >>> encrpyt('atacar base Sul', 'limao')
        'lbmcocjmssdcx'
    """
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
    """
    Decripta o texto usando a chave de decriptação.

    Parameters:
        text: o texto a ser decriptado.
        key: a chave de decriptação.


    Examples:
        >>> decrypt('lbmcoc jmss dcx', 'limao')
        'atacar base sul'

        >>> decrypt('lbmcocjmssdcx', 'limao')
        'atacarbasesul'
    """
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
    """Encripta ou decripta o texto usando a chave de encriptação.

    Parameters:
        text: o texto a ser encriptado ou decriptado.
        key: a chave de encriptação.
        mode: o modo de encriptação ou decriptação.

    Examples:
        >>> vigenere('atacar base Sul', 'limao', 'e', True)
        'lbmcoc jmss dcx'
        >>> vigenere('lbmcoc jmss dcx', 'limao', 'd')
        'atacar base sul'
        >>> vigenere('atacar base Sul', 'limao', 'e')
        'lbmcocjmssdcx'
        >>> vigenere('lbmcjmssdcx', 'limao', 'd')
        'atacarbasesul'
    """
    match mode:
        case "e":
            return encrpyt(text, key, space)
        case "d":
            return decrypt(text, key)
