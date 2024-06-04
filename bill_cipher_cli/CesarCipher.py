from rich import print
import typer

alfbet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

def coretion(text):
    """
    Converte o texto para minusculo, remove os espaços e troca os ç por c.
    
    Parameters:
        text: o texto a ser convertido.
    
    Examples:
        >>> Coretion('The quick brown fox jumps over the lazy dog')
        'thequickbrownfoxjumpsoverthelazydog'
    """
    
    text = text.lower()
    text = text.replace(' ','')
    text = text.replace('ç','c')
    return text

def encryption(text,key):
    """
    Encripta o texto usando a chave de encriptação.

    Parameters:
        text: o texto a ser encriptado.
        key: a chave de encriptação.

    Examples:
        >>> encryption('thequickbrownfoxjumpsoverthelazydog',3)
        'wkhtxlfneurzqiramxpsvryhuwkhodcbgrj'
    """
    text = coretion(text)
    textEnctypt = ''
    for letter in text:
        ind = alfbet.index(letter)
        ind = (ind + key) % 26
        textEnctypt += alfbet[ind]
    return textEnctypt

def decryption(text,key):
    """
    Decripta o texto usando a chave de encriptação.

    Parameters:
        text: o texto a ser encriptado.
        key: a chave de encriptação.

    Examples:
        >>> decryption('wkhtxlfneurzqiramxpsvryhuwkhodcbgrj',3)
        'thequickbrownfoxjumpsoverthelazydog'
    """
    text = coretion(text)
    textDecypt = ''
    for letter in text:
        ind = alfbet.index(letter)
        ind = (ind - key) % 26
        textDecypt += alfbet[ind]
    return textDecypt

def CesarCipher(text,key,mode):
    '''
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
    '''
    match mode:
        case 'e':
            return encryption(text,key)
        case 'd':
            return decryption(text,key)



if __name__ == '__main__':
    text = 'The quick brown fox jumps over the lazy dog'
    key = 3
    encryp = CesarCipher(text,key,'e')
    print(encryp)
    decryp = CesarCipher(encryp,key,'d')
    print(decryp)   