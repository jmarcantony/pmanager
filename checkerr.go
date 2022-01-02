package main

import (
	"fmt"
	"log"
	"os"
)

func CheckErr(err error, validate bool) {
	if err != nil {
		if validate {
			fmt.Println("Incorrect password")
			os.Exit(1)
		}
		log.Fatal(err)
	}
}
