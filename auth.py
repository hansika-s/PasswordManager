# Authentication for the Password Manager CLI - handles master password setup, verification, and reset

import os
import getpass
import bcrypt


def authenticate_user():
    """
    Prompt user for master password and verify it.

    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    saved_password = get_master_password()
    master_password = getpass.getpass("Enter the master password: ")
    return verify_master_password(master_password, saved_password)


def setup_master_password():
    """
    Prompt user to set up a new master password and save it.
    """
    while True:
        master_password = getpass.getpass("Setup a master password: ")
        confirm_password = getpass.getpass("Confirm master password: ")
        if master_password == confirm_password:
            save_master_password(master_password)
            print("Master password setup successful!")
            break
        else:
            print("Passwords do not match. Try again.")


def get_master_password():
    """
    Retrieve the hashed master password from file, or prompt setup if missing.

    Returns:
        bytes: Hashed master password.
    """
    if not os.path.exists("master.hash"):
        print("Master password does not exist. Please set one.")
        setup_master_password()
    with open("master.hash", "rb") as f:
        return f.read()


def save_master_password(pw):
    """
    Hash and save the master password to file.

    Args:
        pw (str): Master password to hash and save.
    """
    hashed_password = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    with open("master.hash", "wb") as f:
        f.write(hashed_password)


def verify_master_password(pw, stored_pw):
    """
    Check if the provided password matches the stored hash.

    Args:
        pw (str): Password to verify.
        stored_pw (bytes): Stored hashed password.
    Returns:
        bool: True if password matches, False otherwise.
    """
    if bcrypt.checkpw(pw.encode(), stored_pw):
        print("Access granted")
        return True
    else:
        print("Access denied")
        return False


def reset_master_password():
    """
    Allow user to reset the master password after verifying the current one.
    """
    entered_password = getpass.getpass(f"Enter the current master password: ")
    stored_password = get_master_password()
    if verify_master_password(entered_password, stored_password):
        new_master_password = getpass.getpass(f"Enter new master password: ")
        save_master_password(new_master_password)
        print("Master password has been reset.")
    else:
        print("Authetication failed!")
