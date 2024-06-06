alfbet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()


def coretion(text, space: bool = False):
    """
    Converte o texto para minusculo, remove os espaços e troca os ç por c.

    Parameters:
        text: o texto a ser convertido.
        space: se True, mantem os espaços.


    Examples:
        >>> Coretion('The quick brown fox jumps over the lazy dog')
        'thequickbrownfoxjumpsoverthelazydog'

        >>> Coretion('The quick brown fox jumps over the lazy dog',true)
        'thequickbrownfoxjumpsoverthelazydog'
    """

    text = text.lower()
    if not space:
        text = text.replace(" ", "")
    text = text.replace("ç", "c")
    return text


def fileRead(filepath):
    with open(filepath, "r") as f:
        return f.read()


def fileWrite(filepath, content):
    with open(filepath, "w") as f:
        f.write(content)


def newFilePath(filepath, mode):
    match mode:
        case "e":
            return filepath.replace(".txt", "_Encrypted.txt")
        case "d":
            return filepath.replace(".txt", "_Decrypted.txt")
