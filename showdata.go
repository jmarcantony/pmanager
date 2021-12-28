package main

import (
	"fmt"
)

func ShowAddr(website string, addr string, d Data) {
	r, ok := d[website]
	if !ok {
		fmt.Println("[-] No record found on", website)
		return
	}
	pass, ok := r[addr]
	if !ok {
		fmt.Println("[-] Invalid adress", addr)
		return
	}
	fmt.Printf("[+] Website: %s\n[+] Email: %s\n[+] Password: %s\n", website, addr, pass)
}
