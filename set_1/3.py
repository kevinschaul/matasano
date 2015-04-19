#!/usr/bin/env python3

import codecs
import re

from score import score

results = []

def main():
    hex1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    bytes1 = hexToBytes(hex1)

    for character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        tryCharacter(bytes1, character)

    sortedResults = sorted(results, key=lambda result: result.get('score'))
    for result in sortedResults[-5:]:
        print('key: {}\tresult: {}\tscore: {}\n'.format(result.get('character'), result.get('xord'), result.get('score')))

def tryCharacter(cipherBytes, character):
    keyBytes = bytes(character, 'ascii') * len(cipherBytes)
    xord = xor(cipherBytes, keyBytes)
    s = score(xord)

    results.append({
        'character': character,
        'xord': xord,
        'score': s,
    })

def xor(bytes1, bytes2):
    bytes_len = len(bytes1)
    xord = bytearray(bytes_len)
    for i in range(bytes_len):
        xord[i] = bytes1[i] ^ bytes2[i]
    return xord

def hexToBytes(the_hex):
    return codecs.decode(the_hex, 'hex_codec')

def bytesToBase64(the_bytes):
    return codecs.encode(the_bytes, 'base64')

if __name__ == '__main__':
    main()

