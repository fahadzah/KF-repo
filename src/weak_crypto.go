// Deliberately weak/deprecated crypto usage for AgileSec GitHub sensor test coverage.
package main

import (
	"crypto/des"
	"crypto/md5"
	"crypto/sha1"
)

func hashPassword(pw []byte) [16]byte {
	// deprecated: MD5
	return md5.Sum(pw)
}

func legacyHash(data []byte) [20]byte {
	// deprecated: SHA-1
	return sha1.Sum(data)
}

func weakCipher(key []byte) (interface{}, error) {
	// deprecated: DES (56-bit, broken)
	return des.NewCipher(key)
}
