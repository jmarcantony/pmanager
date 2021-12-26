package cmd

import (
	"fmt"
	"syscall"

	"golang.org/x/term"
)

func Getpass() (string, error) {
	fmt.Print("🔒 Enter master password: ")
	password, err := term.ReadPassword(int(syscall.Stdin))
	fmt.Println()
	return string(password), err
}
