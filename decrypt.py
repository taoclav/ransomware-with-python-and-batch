from cryptography.fernet import Fernet
import os

def cargar_key():
    return open('key.key', 'rb').read()

def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item, 'wb') as file:
            file.write(decrypted_data)

if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\taocl\\OneDrive\\Escritorio\\ransom\\encriptadojaja'
    os.remove(path_to_encrypt+'\\'+'readme.txt')

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    key = cargar_key()
    decrypt(full_path, key)
archivo = "C:\\Users\\taocl\\OneDrive\\Escritorio\\ransom\\encriptadojaja"
encriptadojaja = "C:\\Users\\taocl\\OneDrive\\Escritorio\\ransom\\encriptadojaja"
archivo = "C:\\Users\\taocl\\OneDrive\\Escritorio\\ransom\\Files"
encriptadojaja = "C:\\Users\\taocl\\OneDrive\\Escritorio\\ransom\\encriptadojaja"

os.rename(encriptadojaja, archivo)
