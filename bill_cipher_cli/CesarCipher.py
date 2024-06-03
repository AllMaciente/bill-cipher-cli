from rich import print

alfbet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

def coretion(text):
    text = text.lower()
    text = text.replace(' ','')
    return text

def encryption(text,key):
    text = coretion(text)
    try:
        key = int(key)
    except:
        print('[red]key must be int[/]')
        return
    textEnctypt = ''
    for letter in text:
        ind = alfbet.index(letter)
        ind = (ind + key) % 26
        textEnctypt += alfbet[ind]
    return textEnctypt

def decryption(text,key):
    text = coretion(text)
    try:
        key = int(key)
    except:
        print('[red]key must be int[/]')
        return
    textDecypt = ''
    for letter in text:
        ind = alfbet.index(letter)
        ind = (ind - key) % 26
        textDecypt += alfbet[ind]
    return textDecypt

def CesarCipher(text,key,mode):
    '''
    text: str
    key: int
    mode: str only 'e' or 'd'
    '''
    match mode:
        case 'e':
            return encryption(text,key)
        case 'd':
            return decryption(text,key)
        case _:
            print('[red]mode must be e or d[/]')
            return



if __name__ == '__main__':
    text = 'saahv'
    key = '18'
    encryp = CesarCipher(text,key,'e')
    print(encryp)
    decryp = CesarCipher(encryp,key,'d')
    print(decryp)   