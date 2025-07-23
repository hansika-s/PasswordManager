# Handles loading and saving the password vault as a JSON file

import json
import os

VAULT_FILE = 'vault.json'


def load_vault():
    """
    Load the password vault from VAULT_FILE (JSON).

    Returns:
        dict: Vault data as a dictionary. Returns empty dict if file does not exist.
    """
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, 'r') as f:
        return json.load(f)


def save_vault(vault):
    """
    Save the password vault to VAULT_FILE (JSON).

    Args:
        vault (dict): Vault data to save.
    """
    with open(VAULT_FILE, 'w') as f:
        json.dump(vault, f, indent=4)
