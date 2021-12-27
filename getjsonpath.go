package main

import (
	"os"

	"github.com/joho/godotenv"
)

func GetJsonPath() string {
	godotenv.Load()
	path := os.Getenv("PMANAGER_DATA_PATH")
	if path == "" {
		path = "data.json"
	}
	return path
}
