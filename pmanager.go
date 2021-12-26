package main

import (
	"log"

	"github.com/jmarcantony/pmanager/cmd"
)

func main() {
	pass, err := cmd.Getpass()
	if err != nil {
		log.Fatal(err)
	}
	_ = pass
}
