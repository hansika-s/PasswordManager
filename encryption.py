# Encryption utils for the Password Manager CLI
from cryptography.fernet import Fernet
import os

KEY_FILE = 'secret.key'


def generate_key():
    """
    Generate a new Fernet key and save it to KEY_FILE.
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)


def load_key():
    """
    Load the Fernet key from KEY_FILE, generating one if it doesn't exist.

    Returns:
        bytes: Loaded key.
    """
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, 'rb') as f:
        return f.read()


def encrypt_data(data):
    """
    Encrypt a string using Fernet symmetric encryption.

    Args:
        data (str): Data to encrypt.
    Returns:
        str: Encrypted data (base64-encoded string).
    """
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(data):
    """
    Decrypt a string using Fernet symmetric encryption.

    Args:
        data (str): Encrypted data (base64-encoded string).
    Returns:
        str: Decrypted data.
    """
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(data.encode()).decode()
