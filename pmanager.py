try:
    import os
    import json
    import time
    import base64
    import hashlib
    import pyperclip
    import cryptography
    import datetime as dt
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

def help():
    docs = """
 add:
  Description:
    Adds a new email and a password to json file
  Usage:
    add [website] [email] [password] (Replace placeholders in squarebackets with actual email and password)

 remove:
  Description:
    Removes an email from json file
  Usage:
    remove [email] (Replace placeholders in squarebackets with email to remove)

 remove website:
  Description:
    Removes all emails by given website name
  Usage:
    remove website [website] (Replace placeholders in squarebackets with website to remove)

 get:
  Description:
    Shows Email and Password for a given Email and copies password to clipboard.
  Usage:
    get [email] (Replace placeholders in squarebackets with actual email)

 getpass:
  Description:
    Copies password of a given email to clipboard without showing it.
  Usage:
    getpass [email] (Replace placeholders in squarebackets with actual email) 

 fetch website:
  Description:
    Gets all emails by given website name (Replace placeholders in squarebackets with website to fetch)
  Usage:
    fetch website [website]

 show all:
  Description:
    Shows all stored data in tabulated form.
  Usage:
    show all

 switch:
  Description:
    Changes master password
  Usage:
    switch

 help:
  Description:
    Shows Documementation
  Usage:
    help

 clear:
  Description:
    Clears the scren.
  Usage:
    clear 
 
 quit:
  Description:
    Quits the proramme, Ctrl + c also works.
  Usage:
    quit
    """
    print(docs)

def decrypt_file():
    try:
        with open("key.txt", "rb") as f:
            key = f.read()
    except FileNotFoundError:
        with open("error-log.txt", "w") as f:
            f.write(f"({dt.date.today().strftime('%d/%m/%Y')}, {dt.datetime.now().strftime('%H:%M:%S')}) 'key.txt' file not found!")
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
            with open("error-log.txt", "w") as f:
                f.write(f"({dt.date.today().strftime('%d/%m/%Y')}, {dt.datetime.now().strftime('%H:%M:%S')}) An Error Occured and was handled!")

def change_master_password(data):
    new_pass = getpass("\nEnter new password: ")
    retype = getpass("Retype new password: ")
    
    if new_pass == retype:
        data["master_password"] = encode_sha(new_pass)
        decrypt_file()
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
            print("[+] Master Password has been updated succcesfully!")
        encrypt_file()
    else:
        print("\n[-] Password does not match!")
        change_master_password(data)

def remove(email, by_website=False):
    decrypt_file()
    with open("data.json") as base_file:
        data = json.load(base_file)
        if email in data["entries"]:
            new_data = data
            del new_data["entries"][email]
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
            if not by_website:
                print("[+] Removed entry from database")
        else:
            if not by_website:
                print("[-] Email not found in database")
    encrypt_file()

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
    entries = [[value["website"], key, decode_password(value["password"])] for (key, value) in data['entries'].items()]
    print(f"\n{tabulate(entries, headers=['Website', 'Email', 'Password'], tablefmt='orgtbl')}\n")

def show_details(get, data):
    email_to_get = get
    try:
        print(f"[+] Website: {data['entries'][email_to_get]['website']}\n[+] Email: {email_to_get}\n[+] Password: {decode_password(data['entries'][email_to_get]['password'])}")
        pyperclip.copy(decode_password(data['entries'][email_to_get]["password"]))
    except KeyError:
        print(f"[-] No Data found on {email_to_get}")

def copy_password(get, data):
    email_to_get = get
    try:
        pyperclip.copy(decode_password(data['entries'][email_to_get]["password"]))
        print(f"[+] Password Copied to Clipboard")
    except KeyError:
        print(f"[-] No Data found on {email_to_get}")  

def add_data(website, email_to_add, email_password):
    decrypt_file()
    with open("data.json") as base_file:
        data = json.load(base_file)
        with open("data.json", "w") as file:
            if email_to_add not in data['entries']:
                new_data = data
                new_data['entries'][email_to_add] = {}
                new_data['entries'][email_to_add]["password"] = email_password
                new_data['entries'][email_to_add]["website"] = website
                json.dump(new_data, file, indent=4)
                print("[+] Added Entry to Database")
            else:
                update = input(f"{email_to_add} is already in the databse, do you want to update it? (y / n): ").lower()
                if update == "y":
                    new_data = data
                    new_data['entries'][email_to_add]["password"] = encode_password(email_password)
                    new_data['entries'][email_to_add]["website"] = website
                    json.dump(new_data, file, indent=4)
                    print("[+] Updated Entry to Database")
    encrypt_file()

def get_website(website, data):
    found = []
    for (email, pairs) in data["entries"].items():
        if pairs["website"] == website:
            found.append([pairs["website"], email, decode_password(pairs["password"])])
    print(f"\n{tabulate(found, headers=['Website', 'Email', 'Password'], tablefmt='orgtbl')}\n")

def remove_website(website, data):
    removed = 0
    for (email, pairs) in data["entries"].items():
        if pairs["website"] == website:
            remove(email, by_website=True)
            removed += 1
    if removed > 0:
        print(f"[+] Removed {removed} entries from database")
    else:
        print(f"[-] No entries found with website '{website}'")

def main():
    try:
        decrypt_file()
        with open("data.json", "r") as file:
            # Read Master Password
            data = json.load(file)
            master_password = data['master_password']
        encrypt_file()
        if master_password == "dGVzdA==":
            print("\nPlease Change your master password!")
            change_master_password(data)
            quit()

        master_password_input = getpass("Enter master password: ")
        if encode_sha(master_password_input) == master_password:
            clear()
            while True:
                decrypt_file()
                with open("data.json", "r") as f:
                    data = json.load(f)
                encrypt_file()
                command = input(">> ").split()
                try:
                    if command[0] == "getpass":
                        if len(command) == 2:
                            copy_password(command[1], data)
                        else:
                            print("[-] Invalid Arguments, try 'help' for help")
                    elif command[0] == "fetch" and command[1] == "website":
                        if len(command) == 3:
                            get_website(command[2], data)
                        else:
                            print("[-] Invalid Arguments, try 'help' for help")
                    elif command[0] == "get":
                        if len(command) == 2:
                            get_website(command[2].lower(), data)
                        else:
                            print("[-] Invalid Arguments, try 'help' for help")
                    elif command[0] == "add":
                        if len(command) == 4:
                            add_data(command[1], command[2], encode_password(command[3]))
                        else:
                            print("[-] Invalid Arguments, type 'help' for help")
                    elif command[0] == "remove":
                        if len(command) == 3:
                            if command[1] == "website":
                                remove_website(command[2], data)
                        elif len(command) == 2:
                            remove(command[1])
                        else:
                            print("[-] Invalid Arguments, type 'help' for help")
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
                    elif command[0] == "help":
                        help()                        

                    # Exit Command                    
                    if exit_programme(command):
                        clear()
                        break
                except IndexError:
                    clear()

        else:
            print("[-] Wrong Password, Try again.")

    except FileNotFoundError:
        with open("data.json", "w") as f:
            f.write("""
{
    "master_password": "dGVzdA==",
    "entries": {
        "test@gmail.com": {
                "website": "google",
                "password": "dGVzdA=="
            }
    }
}
            """)
        print("[+] Data File has been created. Run the programme again to use it.")
        encrypt_file()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
