package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func HandleInterrupt() {
	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		Clear()
		fmt.Println("Interrupted...")
		os.Exit(0)
	}()
}
