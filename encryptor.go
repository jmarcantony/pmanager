package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"encoding/hex"
	"io"
	"io/ioutil"
	"os"
)

func encryptJson(path string, pass string) {
	c, err := ioutil.ReadFile(path)
	CheckErr(err, false)
	contents := hex.EncodeToString(c)
	k, _ := hex.DecodeString(pass)
	b := []byte(contents)
	block, err := aes.NewCipher(k)
	CheckErr(err, false)
	aesGCM, err := cipher.NewGCM(block)
	CheckErr(err, false)
	nonce := make([]byte, aesGCM.NonceSize())
	_, err = io.ReadFull(rand.Reader, nonce)
	CheckErr(err, false)
	encrypted := aesGCM.Seal(nonce, nonce, b, nil)
	err = os.WriteFile(path, encrypted, 0644)
	CheckErr(err, false)
}
