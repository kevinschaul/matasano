#!/usr/bin/env python3

import codecs

from Crypto.Cipher import AES

def main():
    cipherBytes = bytes()
    with open('7-ciphertext.txt', 'rb') as ciphertextFile:
        ciphertext = ciphertextFile.read()
    cipherBytes = base64ToBytes(ciphertext)

    key = 'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    msg = cipher.decrypt(cipherBytes)
    print(msg)

def base64ToBytes(the_base64):
    return codecs.decode(the_base64, 'base64')

if __name__ == '__main__':
    main()

