package main

import (
	"fmt"
	"os"
	"strings"
)

func Add(d Data, website string, addr string, pass string) Data {
	if _, ok := d[website]; !ok {
		d[website] = map[string]string{}
	}
	if _, ok := d[website][addr]; ok {
		fmt.Printf("%q already exists, do you want to update the password [y]es/[n]o: ", addr)
		buf := make([]byte, 1)
		n, err := os.Stdin.Read(buf)
		CheckErr(err, false)
		if strings.ToLower(string(buf[:n])) != "y" {
			return d
		}
		fmt.Println("[+] Updated Entry to Database")
	}
	d[website][addr] = pass
	return d
}
