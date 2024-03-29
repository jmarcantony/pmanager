# Pmanager
Password Manager in go

## Written in go 1.17.5

# Installation:
#### Make sure `$GOPATH/bin` is added to PATH
    go install github.com/jmarcantony/pmanager@latest
#### Set `PMANAGER_DATA_PATH` environment variable to path of data file (data file doesnt have to exist yet). eg:
    export PMANAGER_DATA_PATH="/home/user/data.json"

# Docs:
## add:
### Description:
    Adds a new email and a password to json file
### Usage:
    add [website] [email] [password]

## remove:
### Description:
    Removes an email from json file
### Usage:
    remove [website] [email]

## remove website:
### Description:
    Removes all emails by given website name
### Usage:
    remove website [website]

## show [website] [email]:
### Description:
    Shows Email and Password for a given Email and copies password to clipboard.
### Usage:
    get [website] [email]

## getpass:
### Description:
    Copies password of a given email to clipboard without showing it.
### Usage:
    getpass [website] [email]

## show all [website]:
### Description:
    Gets all emails by given website name
### Usage:
    show all [website]

## show all:
### Description:
    Shows all stored data in tabulated form.
### Usage:
    show all

## switch:
### Description:
    Changes master password
### Usage:
    switch

## help:
### Description:
    Shows Documementation
### Usage:
    help

## clear, cls:
### Description:
    Clears the scren.
### Usage:
    clear 

## quit:
### Description:
    Quits the proramme, Ctrl + c also works.
### Usage:
    quit
