package main

import "fmt"

func Remove(d Data, website string, addr string) Data {
	if _, ok := d[website]; !ok {
		fmt.Printf("[-] No records found on %q\n", website)
		return d
	}
	if _, ok := d[website][addr]; !ok {
		fmt.Println("[-] Address not found in records")
		return d
	}
	delete(d[website], addr)
	return d
}
