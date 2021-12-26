package main

import (
	"encoding/json"
	"os"

	"github.com/jmarcantony/pmanager/pkg"
)

func decryptJson(path string, pass string) map[string]string {
	var data map[string]string
	f, _ := os.ReadFile(path)
	err := json.Unmarshal(f, &data)
	pkg.CheckErr(err)
	return data
}
