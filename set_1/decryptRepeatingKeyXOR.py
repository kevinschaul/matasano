#!/usr/bin/env python3

import codecs
import math
import sys

def main():
    with open(sys.argv[1], 'rb') as ciphertextFile:
        ciphertext = ciphertextFile.read()
        ciphertextBytes = base64ToBytes(ciphertext)
        key = sys.argv[2]
        encrypted = encryptRepeatingKeyXOR(ciphertextBytes, key)
        encryptedHex = bytesToHex(encrypted)
        print(encrypted)

def encryptRepeatingKeyXOR(plaintextBytes, key):
    keyBytes = key.encode()
    keyBytesRepeated = repeatBytes(len(plaintextBytes), keyBytes)
    return xor(plaintextBytes, keyBytesRepeated)

def repeatBytes(length, keyBytes):
    """
    Returns a repeated sequence of `keyBytes` with length `length`
    """
    repeatedBytes = bytearray(length)
    keyBytesLength = len(keyBytes)
    for i in range(0, length):
        repeatedBytes[i] = keyBytes[i % keyBytesLength]
    return repeatedBytes

def xor(bytes1, bytes2):
    bytes_len = len(bytes1)
    xord = bytearray(bytes_len)
    for i in range(bytes_len):
        xord[i] = bytes1[i] ^ bytes2[i]
    return xord

def bytesToHex(the_bytes):
    return codecs.encode(the_bytes, 'hex_codec')

def hexToBytes(the_hex):
    return codecs.decode(the_hex, 'hex_codec')

def bytesToBase64(the_bytes):
    return codecs.encode(the_bytes, 'base64')

def base64ToBytes(the_base64):
    return codecs.decode(the_base64, 'base64')

if __name__ == '__main__':
    main()

