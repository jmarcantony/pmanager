package pkg

import (
	"fmt"
	"log"
)

func CheckErr(err error) {
	if err != nil {
		fmt.Printf("%T\n", err)
		log.Fatal(err)
	}
}
