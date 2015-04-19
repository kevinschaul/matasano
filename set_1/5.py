#!/usr/bin/env python3

import base64
import codecs
import math

def main():
    plaintext = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    #plaintext = 'Israeli Prime Minister Benjamin Netanyahu vowed to keep targeting Palestinian militants despite the growing casualties and diplomatic pressure to end the conflict. Israel\'s military on Sunday also denied its soldiers were behind the deaths of 16 Palestinians killed by shells as they sought refuge in a U.N. school Thursday near an area of intense fighting between Israeli forces and Hamas militants. But Israel\'s military, in a statement, offered no details of its \"comprehensive inquiry,\" releasing a grainy, aerial video showing an Israeli mortar landing in an empty courtyard of the school as proof that it bore no responsibility'
    key = 'ICE'
    encrypted = encryptRepeatingKeyXOR(plaintext, key)
    encryptedHex = bytesToHex(encrypted)
    print(encryptedHex)
    print(bytesToBase64(encrypted))

def encryptRepeatingKeyXOR(plaintext, key):
    plaintextBytes = plaintext.encode()
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

