package main

import (
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
		os.Exit(0)
	}()
}
