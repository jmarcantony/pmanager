package pkg

import (
	"fmt"
	"syscall"

	"golang.org/x/term"
)

func GetPass() string {
	fmt.Print("🔒 Enter master password: ")
	password, err := term.ReadPassword(int(syscall.Stdin))
	CheckErr(err)
	fmt.Println()
	return string(password)
}
