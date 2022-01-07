package main

import "fmt"

func RemoveWebsite(d Data, website string) Data {
	if _, ok := d[website]; !ok {
		fmt.Printf("[-] No Entries Found on %q\n", website)
		return d
	}
	delete(d, website)
	fmt.Println("[+] Deleted all entries")
	return d
}
