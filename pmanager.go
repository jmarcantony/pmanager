package main

import (
	"fmt"

	"github.com/jmarcantony/pmanager/pkg"
)

func main() {
	jsonPath := pkg.GetJsonPath()
	created := pkg.CreateJson(jsonPath)
	if created {
		fmt.Println("Created!")
		return
	}
	pass := pkg.GetPass()
	data := decryptJson(jsonPath, pass)
	for k, v := range data {
		fmt.Printf("%s: %s\n", k, v)
	}
}
