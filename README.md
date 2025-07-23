# Password Manager CLI

A simple Python tool to securely store and manage passwords using Fernet encryption, built with [Typer](https://typer.tiangolo.com/) for the CLI and [click-repl](https://github.com/click-contrib/click-repl) for interactive shell support.

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

- Add: `python main.py add SERVICE USERNAME PASSWORD`
- Get: `python main.py get SERVICE`
- Edit: `python main.py edit SERVICE [USERNAME] [PASSWORD]`
- Delete: `python main.py delete SERVICE`
- List: `python main.py services`
- Commands: `python main.py commands`
- Interactive shell: `python main.py repl`

> On first run, there will be a prompted to set up a master password for authentication.
