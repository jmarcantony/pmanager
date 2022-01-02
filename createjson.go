package main

import (
	"io/ioutil"
	"os"
)

func CreateJson(path string) (created bool) {
	if _, err := os.Stat(path); err != nil {
		initData := []byte(`
{
	"email": {
    	"test@email.com": "dGVzdA=="
	}
}	
		`)
		err := ioutil.WriteFile(path, initData, 0600)
		CheckErr(err, false)
		created = true
		pass := GetPass(true)
		encryptJson(path, pass)
	}
	return
}
