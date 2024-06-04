from bill_cipher_cli import *

from typer import Argument,Option,Typer 

app = Typer(pretty_exceptions_enable=True)

@app.command(help="Encrypt or decrypt a message in Cesar cipher")
def Cesar(
    e:bool = Option(False,help="Encypty mode"),
    d:bool = Option(False,help="Decypt mode"),
    f:bool = Option(False,help="File encrypt or decrypt"),
    text:str = Argument(...,help="the msg to encrypt or decrypt"),
    key:int = Argument(...,help="the key to encrypt or decrypt")
    ):

    if e or d:
        if e :
            mode = 'e'
        elif d:
            mode = 'd'
        print(CesarCipher(text,key,mode))
    else:
        print("Information needed flags --e or --d")


@app.command()
def Vigenere():
    ...



app()