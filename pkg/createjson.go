package pkg

import (
	"io/ioutil"
	"os"
)

func CreateJson(path string) bool {
	var created bool
	if _, err := os.Stat(path); err != nil {
		initData := []byte(`
{
    "test@email.com": "dGVzdA=="
}	
		`)
		err := ioutil.WriteFile(path, initData, 0600)
		CheckErr(err)
		created = true
	}
	return created
}
