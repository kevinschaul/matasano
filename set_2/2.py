#!/usr/bin/env python3

import codecs
import math

from Crypto.Cipher import AES

def main():
    cipherBytes = bytes()
    with open('2-ciphertext.txt', 'rb') as ciphertextFile:
        ciphertext = ciphertextFile.read()
    cipherBytes = base64ToBytes(ciphertext)

    iv = bytes([0 for x in range(16)])
    print(decryptCBC(cipherBytes, 'YELLOW SUBMARINE', iv))

def decryptCBC(the_bytes, key, iv):
    blocks = splitBytearrayIntoSize(len(key), the_bytes)
    seed = iv
    plainbytes = bytearray()
    for block in blocks:
        decrypted = decryptECB(block, key)
        xored = xor(decrypted, seed)
        plainbytes.extend(xored)
        seed = block
    return plainbytes

def encryptECB(the_bytes, key):
    cipher = AES.new(key, AES.MODE_ECB)
    msg = cipher.encrypt(the_bytes)
    return msg

def decryptECB(the_bytes, key):
    cipher = AES.new(key, AES.MODE_ECB)
    msg = cipher.decrypt(the_bytes)
    return msg

def xor(bytes1, bytes2):
    bytes_len = len(bytes1)
    xord = bytearray(bytes_len)
    for i in range(bytes_len):
        xord[i] = bytes1[i] ^ bytes2[i]
    return xord

def splitBytearrayIntoSize(size, b):
    innerBytearraySize = math.ceil(len(b) / size)
    splitBytearray = getListOfBytearrays(innerBytearraySize)

    i = 0
    for byte in b:
        bytearrayIndex = math.floor(i / size)
        splitBytearray[bytearrayIndex].append(byte)
        i += 1

    return [bytes(array) for array in splitBytearray]

def getListOfBytearrays(size):
    l = []
    for i in range(0, size):
        l.append(bytearray())
    return l

def base64ToBytes(the_base64):
    return codecs.decode(the_base64, 'base64')

if __name__ == '__main__':
    main()

