package main

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"syscall"

	"golang.org/x/term"
)

func createPass(pass []byte) string {
	p := sha256.Sum256(pass)
	return hex.EncodeToString(p[:])
}

func GetPass(create bool) string {
	fmt.Print("🔒 Enter master password: ")
	password, err := term.ReadPassword(int(syscall.Stdin))
	CheckErr(err, false)
	if create {
		fmt.Print("\n✅ Retype master password: ")
		retyped, err := term.ReadPassword(int(syscall.Stdin))
		CheckErr(err, false)
		if string(password) != string(retyped) {
			fmt.Println("\n❌ Passwords do not match, try again")
			return GetPass(create)
		}
	}
	fmt.Println()
	return createPass(password)
}
