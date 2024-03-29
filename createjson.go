package main

import (
	"io/ioutil"
	"os"
)

func CreateJson(path string) (created bool, pass string) {
	if _, err := os.Stat(path); err != nil {
		initData := []byte(`{"email": {"test@email.com": "test"}}`)
		err := ioutil.WriteFile(path, initData, 0600)
		CheckErr(err, false)
		created = true
		pass = GetPass(true)
		encryptJson(path, pass)
	}
	return
}
