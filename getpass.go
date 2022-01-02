package main

import (
	"encoding/hex"
	"fmt"
	"syscall"

	"golang.org/x/term"
)

func createPass(pass []byte) string {
	if len(pass) == 32 {
		return hex.EncodeToString(pass)
	}
	if len(pass) < 32 {
		b := make([]byte, 32)
		for i := range b {
			if i < len(pass) {
				b[i] = pass[i]
			} else {
				b[i] = '0'
			}
		}
		return hex.EncodeToString(b)
	} else {
		return hex.EncodeToString(pass[:33])
	}
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
