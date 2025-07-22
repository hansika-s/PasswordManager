# Password Manager CLI

A simple Python tool to securely store and manage passwords using Fernet encryption.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Generate encryption key:
   ```bash
   python -c "from encryption import generate_key; generate_key()"
   ```
   > Keep `secret.key` private

## Usage

- Add: `python main.py add --service SERVICE --username USER --password PASS`
- Get: `python main.py get --service SERVICE`
- Edit: `python main.py edit --service SERVICE [--username USER] [--password PASS]`
- Delete: `python main.py delete --service SERVICE`
- List: `python main.py list`
