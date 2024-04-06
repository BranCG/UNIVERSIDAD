import hashlib

# Módulo que proporciona funciones para codificar y decodificar contraseñas utilizando el algoritmo MD5.
def encode(string):

    result = hashlib.md5(string.encode())
    return result.hexdigest()


def decode(string, claveMd5):

    if hashlib.md5(string.encode()).hexdigest() == claveMd5:
        return True
    else:
        return False
