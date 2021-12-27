package main

import (
	"fmt"
	"os"
	"text/tabwriter"
)

func ShowWebsite(website string, d Data) {
	entries, ok := d[website]
	if !ok {
		fmt.Printf("[-] No entries exist on %s\n", website)
		return
	}
	w := tabwriter.NewWriter(os.Stdout, 1, 1, 5, ' ', 0)
	fmt.Fprintln(w, "Website\tEmail\tPassword")
	for addr, pass := range entries {
		fmt.Fprintf(w, "%s\t%s\t%s\n", website, addr, pass)
	}
	w.Flush()
}
