try:
    import os
    import json
    import time
    import base64
    import hashlib
    import pyperclip
    import cryptography
    from getpass import getpass
    from os import system, name
    from tabulate import tabulate
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    print("[-] Requirements not satisfied!\n\trun 'pip install -r requirements.txt'\n\t\tOR\n\trun 'pip3 install -r requirements.txt'")
    quit()

# Functions
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def encode_sha(string):
    sha_hash = hashlib.sha256(string.encode()).hexdigest()
    return sha_hash

def encrypt_file():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open("data.json", "rb") as f:
        original = f.read()
    encrypted = fernet.encrypt(original)
    with open("data.json", "wb") as new_f:
        new_f.write(encrypted)
    with open("key.txt", "wb") as key_f:
        key_f.write(key)

def decrypt_file():
    try:
        with open("key.txt", "rb") as f:
            key = f.read()
    except FileNotFoundError:
        try:
            with open("error-log.txt", "a") as f:
                f.write("[-] 'key.txt' file not found!")
        except FileNotFoundError:
            with open("error-log.txt", "w") as f:
                f.write("[-] 'key.txt' file not found!")
    else:
        try:
            fernet = Fernet(key)
            with open("data.json", "rb") as encoded_file:
                encrypted = encoded_file.read()
            decrypted = fernet.decrypt(encrypted)
            with open("data.json", "wb") as dec_file:
                dec_file.write(decrypted)
        except cryptography.fernet.InvalidToken:
            os.remove("key.txt")
            try:
                with open("error-log.txt", "a") as f:
                    f.write("[-] An Error Occured and was handled!")
            except FileNotFoundError:
                with open("error-log.txt", "w") as f:
                    f.write("[-] An Error Occured and was handled!")

def change_master_password(data):
    new_pass = getpass("\nEnter new password: ")
    retype = getpass("Retype new password: ")
    
    if new_pass == retype:
        data["master_password"] = encode_sha(new_pass)
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
            print("[+] Master Password has been updated succcesfully!")
    else:
        print("\n[-] Password do not match!")
        change_master_password(data)

def exit_programme(args):
    quit_args = ['quit', "goodbye", 'bye']
    return args[0] in quit_args

def encode_password(password):
    password_bytes = password.encode('ascii')
    base64_encode_bytes = base64.b64encode(password_bytes)
    return base64_encode_bytes.decode('ascii')

def decode_password(password):
    password_bytes = password.encode('ascii')
    base64_decode_bytes = base64.b64decode(password_bytes)
    return base64_decode_bytes.decode('ascii')

def show_all_entries(data):
    entries = [[key, decode_password(value)] for (key, value) in data['entries'].items()]
    print(f"\n{tabulate(entries, headers=['Email', 'Password'], tablefmt='orgtbl')}\n")
def show_details(get, data):
    email_to_get = get
    try:
        print(f"[+] Email: {email_to_get}\n[+] Password: {decode_password(data['entries'][email_to_get])}")
        pyperclip.copy(decode_password(data['entries'][email_to_get]))
    except KeyError:
        print(f"[-] No Data found on {email_to_get}")

def copy_password(get, data):
    email_to_get = get
    try:
        pyperclip.copy(decode_password(data['entries'][email_to_get]))
        clear()
        print(f"[+] Password Copied to Clipboard")
    except KeyError:
        print(f"[-] No Data found on {email_to_get}")  


def add_data(email_to_add, email_password):
    with open("data.json") as base_file:
        data = json.load(base_file)
        with open("data.json", "w") as file:
            if email_to_add not in data['entries']:
                new_data = data
                new_data['entries'][email_to_add] = email_password
                json.dump(new_data, file, indent=4)
                clear()
                print("[+] Added Entry to Database")
            else:
                update = input(f"{email_to_add} is already in the databse, do you want to update it? (y / n): ").lower()
                if update == "y":
                    new_data = data
                    new_data['entries'][email_to_add] = email_password
                    json.dump(new_data, file, indent=4)
                    clear()
                    print("[+] Updated Entry to Database, restart app to get data.")

try:
    decrypt_file()
    with open("data.json") as file:
        # Read Master Password
        data = json.load(file)
        master_password = data['master_password']

        if master_password == "dGVzdA==":
            print("\nPlease Change your master password!")
            change_master_password(data)
            encrypt_file()
            quit()

        master_password_input = getpass("Enter master password: ")
        if encode_sha(master_password_input) == master_password:
            clear()
            while True:
                decrypt_file()
                with open("data.json", "r") as f:
                    data = json.load(f)
                command = input(">> ").split()
                try:
                    if command[0] == "getpass":
                        if len(command) == 2:
                            copy_password(command[1], data)
                        else:
                            print("[-] Invalid Arguments")
                    elif command[0] == "get":
                        if len(command) == 2:
                            show_details(command[1], data)
                    elif command[0] == "add":
                        if len(command) == 3:
                            add_data(command[1], encode_password(command[2]))
                        else:
                            print("[-] Invalid Arguments")
                    elif command[0] == "show" and command[1] == "all":
                        show_all_entries(data)
                    elif command[0] == "switch":
                        curr = getpass("Enter current master password: ")
                        if encode_sha(curr) == master_password:
                            change_master_password(data)
                        else:
                            print("[-] Wrong master password!")
                    elif command[0] == "clear" or command[0] == "cls":
                        clear()                        
                    
                    # Exit Command                    
                    if exit_programme(command):
                        clear()
                        encrypt_file()
                        break
                except IndexError:
                    clear()

        else:
            clear()
            print("[-] Wrong Password, Try again.")
            encrypt_file()
except FileNotFoundError:
    with open("data.json", "w") as f:
        f.write("""
{
    "master_password": "dGVzdA==",
    "entries": {
        "test@gmaill.com": "dGVzdA=="
    }
}
            """)
        clear()
        print("[+] Data File has been created. Run the programme again to use it.")
        encrypt_file()
        os.remove("key.txt")
except KeyboardInterrupt:
    clear()
    print("Goodbye...")
    time.sleep(0.5)
    clear()
    encrypt_file()
