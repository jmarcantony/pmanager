package main

import (
	"crypto/aes"
	"crypto/cipher"
	"encoding/hex"
	"encoding/json"
	"os"
)

func decryptJson(path string, pass string) Data {
	var data Data
	c, _ := os.ReadFile(path)
	key, _ := hex.DecodeString(pass)
	enc, _ := hex.DecodeString(hex.EncodeToString(c))
	block, err := aes.NewCipher([]byte(key))
	CheckErr(err, true)
	aesGCM, err := cipher.NewGCM(block)
	CheckErr(err, true)
	nonceSize := aesGCM.NonceSize()
	nonce, ciphertext := enc[:nonceSize], enc[nonceSize:]
	decrypted, err := aesGCM.Open(nil, nonce, ciphertext, nil)
	CheckErr(err, true)
	f, err := hex.DecodeString(string(decrypted))
	CheckErr(err, true)
	err = json.Unmarshal(f, &data)
	CheckErr(err, true)
	return data
}
