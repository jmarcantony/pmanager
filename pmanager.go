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
	created, pass := CreateJson(jsonPath)
	if !created {
		pass = GetPass(false)
	}
	data := decryptJson(jsonPath, pass)
	s := bufio.NewScanner(os.Stdin)
	Clear()
	var skip bool
mainloop:
	for {
		if !skip {
			fmt.Print(">> ")
		} else {
			skip = false
		}
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
					ShowAll(data)
				} else if len(cmd) == 3 {
					ShowWebsite(cmd[2], data)
				} else {
					fmt.Println(argerr)
				}
			} else if len(cmd) == 3 {
				ShowAddr(cmd[1], cmd[2], data)
			}
		case "add":
			if len(cmd) == 4 {
				data, updated := Add(data, cmd[1], cmd[2], cmd[3])
				WriteChanges(data, jsonPath, pass)
				if updated {
					skip = true
				}
			} else {
				fmt.Println(argerr)
			}
		case "remove":
			if len(cmd) == 3 {
				if cmd[1] == "website" {
					data = RemoveWebsite(data, cmd[2])
					WriteChanges(data, jsonPath, pass)
				} else {
					data = Remove(data, cmd[1], cmd[2])
					WriteChanges(data, jsonPath, pass)
				}
			} else {
				fmt.Println(argerr)
			}
		case "switch":
			a := GetPass(true)
			WriteChanges(data, jsonPath, a)
			fmt.Println("[+] Changed master password succesfully")
		case "help":
			Help()
		case "cls", "clear":
			Clear()
		case "quit":
			Clear()
			break mainloop
		}
	}
}
