package main

import (
	"fmt"
	"os"

	"github.com/jedib0t/go-pretty/v6/table"
)

func ShowWebsite(website string, d Data) {
	entries, ok := d[website]
	if !ok {
		fmt.Printf("[-] No entries exist on %s\n", website)
		return
	}
	t := table.NewWriter()
	t.SetOutputMirror(os.Stdout)
	t.AppendHeader(table.Row{"Website", "Email", "Password"})
	var rows []table.Row
	for addr, pass := range entries {
		rows = append(rows, table.Row{website, addr, pass})
	}
	t.AppendRows(rows)
	t.Render()
}
