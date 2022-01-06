package main

import (
	"encoding/json"
	"io/ioutil"
)

func WriteChanges(d Data, path string, pass string) {
	f, _ := json.Marshal(d)
	_ = ioutil.WriteFile(path, f, 0600)
	encryptJson(path, pass)
}
