alfbet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()


def fileRead(filepath):
    with open(filepath, 'r') as f:
        return f.read()


def fileWrite(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)


def newFilePath(filepath, mode):
    match mode:
        case 'e':
            return filepath.replace('.txt', '_Encrypted.txt')
        case 'd':
            return filepath.replace('.txt', '_Decrypted.txt')
