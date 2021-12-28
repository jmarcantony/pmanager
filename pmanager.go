package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Data map[string]map[string]string

const argerr = "[-] Invalid arguments, try 'help' for help"

func main() {
	HandleInterrupt()
	jsonPath := GetJsonPath()
	created := CreateJson(jsonPath)
	if created {
		fmt.Println("Created!")
		return
	}
	pass := GetPass()
	data := decryptJson(jsonPath, pass)
	for k, v := range data {
		fmt.Printf("%s: %s\n", k, v)
	}
	s := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print(">> ")
		s.Scan()
		cmd := strings.Split(s.Text(), " ")
		switch cmd[0] {
		case "getpass":
			if len(cmd) == 3 {
				CopyPass(cmd[1], cmd[2], data)
			} else {
				fmt.Println(argerr)
			}
		case "show":
			if cmd[1] == "all" {
				if len(cmd) == 2 {
					// TODO: Show all data in tabulated form
				} else if len(cmd) == 3 {
					ShowWebsite(cmd[2], data)
				} else {
					fmt.Println(argerr)
				}
			} else if len(cmd) == 3 {
				ShowAddr(cmd[1], cmd[2], data)
			}
		default:
			Clear()
		}
	}
}
