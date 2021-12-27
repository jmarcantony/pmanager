package main

import (
	"encoding/json"
	"os"
)

func decryptJson(path string, pass string) Data {
	var data Data
	f, _ := os.ReadFile(path)
	err := json.Unmarshal(f, &data)
	CheckErr(err)
	return data
}
