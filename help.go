package main

import "fmt"

func Help() {
	fmt.Println(`        add:
		Description:
			Adds a new email and a password to json file
		Usage:
			add [website] [email] [password]

	remove:
		Description:
			Removes an email from json file
		Usage:
			remove [website] [email]

	remove website:
		Description:
			Removes all emails by given website name
		Usage:
			remove website [website]

	show [website] [email]:
		Description:
			Shows Email and Password for a given Email and copies password to clipboard.
		Usage:
			get [website] [email]

	getpass:
		Description:
			Copies password of a given email to clipboard without showing it.
		Usage:
			getpass [website] [email]

	show all [website]:
		Description:
			Gets all emails by given website name
		Usage:
			show all [website]

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

	clear, cls:
		Description:
			Clears the scren.
		Usage:
			clear 

	quit:
		Description:
			Quits the proramme, Ctrl + c also works.
		Usage:
	  		quit
	`)
}
