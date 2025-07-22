from cryptography.fernet import Fernet
import os

KEY_FILE = 'secret.key'


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)


def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, 'rb') as f:
        return f.read()


def encrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(data.encode()).decode()
