import json
import os

VAULT_FILE = 'vault.json'


def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, 'r') as f:
        return json.load(f)


def save_vault(vault):
    with open(VAULT_FILE, 'w') as f:
        json.dump(vault, f, indent=4)
