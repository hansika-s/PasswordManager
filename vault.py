from storage import load_vault, save_vault
from encryption import encrypt_data, decrypt_data


def add_password(service, username, password):
    vault = load_vault()
    vault[service] = {
        'username': encrypt_data(username),
        'password': encrypt_data(password)
    }
    save_vault(vault)
    print(f"[+] Credentials added for {service}.")


def get_password(service):
    vault = load_vault()
    if service in vault:
        creds = vault[service]
        username = decrypt_data(creds['username'])
        password = decrypt_data(creds['password'])
        print(
            f"Service: {service}\nUsername: {username}\nPassword: {password}")
    else:
        print("[-] Service not found.")


def delete_password(service):
    vault = load_vault()
    if service in vault:
        del vault[service]
        save_vault(vault)
        print(f"[+] Credentials deleted for {service}.")
    else:
        print("[-] Service not found.")


def edit_service(service, username, password):
    vault = load_vault()
    if service in vault:
        if username:
            vault[service]['username'] = encrypt_data(username)
        if password:
            vault[service]['password'] = encrypt_data(password)
        save_vault(vault)
        print(f"[+] Credentials updated for {service}.")
    else:
        print("[-] Service not found.")


def list_services():
    vault = load_vault()
    if vault:
        print("Stored services:")
        for service in vault:
            print(f"- {service}")
    else:
        print("No services stored yet.")
