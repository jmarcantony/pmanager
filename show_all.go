package main

import (
	"os"

	"github.com/jedib0t/go-pretty/v6/table"
)

func ShowAll(d Data) {
	t := table.NewWriter()
	t.SetOutputMirror(os.Stdout)
	t.AppendHeader(table.Row{"Website", "Email", "Password"})
	var rows []table.Row
	for website, entries := range d {
		for addr, pass := range entries {
			rows = append(rows, table.Row{website, addr, pass})
		}
	}
	t.AppendRows(rows)
	t.Render()
}
