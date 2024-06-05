from bill_cipher_cli import *

from typer import Argument, Option, Typer

app = Typer(pretty_exceptions_enable=True)


@app.command(help="Encrypt or decrypt a message in Cesar cipher")
def Cesar(
    e: bool = Option(False, help="Encypty mode"),
    d: bool = Option(False, help="Decypt mode"),
    file: bool = Option(False, help="encrypt or decrypt one File "),
    space: bool = Option(False, help="with space (obs Only with --e)"),
    text: str = Argument(..., help="the msg to encrypt or decrypt"),
    key: int = Argument(..., help="the key to encrypt or decrypt")
):

    if e or d:
        if e:
            mode = 'e'
        elif d:
            mode = 'd'
        if file:
            msg = fileRead(text)
            fileWrite(newFilePath(text, mode),
                      CesarCipher(msg, key, mode, space))
        else:
            print(CesarCipher(text, key, mode, space))
    else:
        print("Information needed flags --e or --d")


@ app.command()
def Vigenere():
    ...


app()
