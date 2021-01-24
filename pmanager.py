import json
import time
import base64
import pyperclip
from getpass import getpass
from os import system, name
from tabulate import tabulate

# Master Password is: test

# Functions
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

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
                print("[+] Added Entry to Database, restart app to get data.")
            else:
                update = input(f"{email_to_add} is already in the databse, do you want to update it? (y / n): ").lower()
                if update == "y":
                    new_data = data
                    new_data['entries'][email_to_add] = email_password
                    json.dump(new_data, file, indent=4)
                    clear()
                    print("[+] Updated Entry to Database, restart app to get data.")

try:
    with open("data.json") as file:
        # Read Master Password
        data = json.load(file)
        encoded_master_password = data['master_password']
        master_password_bytes = encoded_master_password.encode('ascii')
        master_password_decoded_bytes = base64.b64decode(master_password_bytes)
        master_password = master_password_decoded_bytes.decode('ascii')

        master_password_input = getpass("Enter master password: ")
        if master_password_input == master_password:
            clear()
            while True:
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
                    elif command[0] == "clear" or command[0] == "cls":
                        clear()                        
                    
                    # Exit Command                    
                    if exit_programme(command):
                        clear()
                        break
                except IndexError:
                    clear()

        else:
            clear()
            print("[-] Wrong Password, Try again.")
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
except KeyboardInterrupt:
    clear()
    print("Goodbye...")
    time.sleep(0.5)
    clear()
