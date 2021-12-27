package main

import (
	"fmt"

	"github.com/atotto/clipboard"
)

func CopyPass(website string, addr string, d Data) {
	entries, ok := d[website]
	if !ok {
		fmt.Printf("[-] No such website %s\n", website)
		return
	}
	pass, ok := entries[addr]
	if !ok {
		fmt.Printf("[-] No data found on %s\n", addr)
	}
	err := clipboard.WriteAll(pass)
	if err != nil {
		fmt.Println("[-] Could not copy password to clipboard")
	} else {
		fmt.Println("[+] Password copied to clipboard")
	}
}
