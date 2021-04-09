# Pmanager
Password Manager with python

## Written in python 3.7.3 

# Installation on Windows:
* `git clone https://github.com/ninjahacker123/Pmanager.git`
* `cd Pmanager`
* `pip install -r requirements.txt`
* `python pmanager.py`

# Installation on Linux and Unix like OS:
* `git clone https://github.com/ninjahacker123/Pmanager.git`
* `cd Pmanager`
* `pip3 install -r requirements.txt`
* `python3 pmanager.py`


# Docs:
## add:
###  Description:
    Adds a new email and a password to json file
###  Usage:
    add [email] [password] (Replace placeholders in squarebackets with actual email and password)

## get:
###  Description:
    Shows Email and Password for a given Email and copies password to clipboard.
###  Usage:
    get [email] (Replace placeholders in squarebackets with actual email)

## getpass:
###  Description:
    Copies password of a givem email to clipboard without showing it.
###  Usage:
    getpass [email] (Replace placeholders in squarebackets with actual email) 

## show all:
###  Description:
    Shows all stored data in tabulated form.
###  Usage:
    show all

## switch:
###  Description:
    Changes master password
###  Usage:
    switch

## clear:
###  Description:
    Clears the scren.
###  Usage:
    clear 
 
## quit:
###  Description:
    Quits the proramme, Ctrl + c also works.
###  Usage:
    quit
