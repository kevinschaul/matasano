#!/usr/bin/env python3

import binascii
import codecs
import math

def main():
    cipherBytes = bytes()
    with open('6-ciphertext.txt', 'rb') as ciphertextFile:
        ciphertext = ciphertextFile.read()
    cipherBytes = base64ToBytes(ciphertext)
    bestKeySizes = getBestKeySizes(cipherBytes)
    print(bestKeySizes)

    for keysize in bestKeySizes:
        blocks = splitBytearrayIntoSize(keysize, cipherBytes)
        print(blocks)

def splitBytearrayIntoSize(size, b):
    splitBytearray = []
    innerBytearraySize = math.ceil(len(b) / size)
    for i in range(0, innerBytearraySize):
        splitBytearray.append(bytearray())

    i = 0
    for byte in b:
        bytearrayIndex = math.floor(i / size)
        splitBytearray[bytearrayIndex].append(byte)
        i += 1

    return splitBytearray

def getBestKeySizes(cipherBytes):
    keysizeDistances = {}
    for keysize in range(2, 40):
        distance = getHammingDistance(
            cipherBytes[0:keysize],
            cipherBytes[keysize:keysize * 2]
        )
        keysizeDistances[keysize] = distance / keysize

    sortedKeysizeDistances = sorted(keysizeDistances.items(),
            key=lambda x: x[1])
    return [x[0] for x in sortedKeysizeDistances[:4]]

def getHammingDistance(bytesA, bytesB):
    distance = 0
    for i in range(0, len(bytesA)):
        for j in range(0, 8):
            bitA = (bytesA[i] >> j) & 0x1
            bitB = (bytesB[i] >> j) & 0x1
            if bitA != bitB:
                distance += 1
    return distance

def base64ToBytes(the_base64):
    return codecs.decode(the_base64, 'base64')

if __name__ == '__main__':
    main()

