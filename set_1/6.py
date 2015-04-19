#!/usr/bin/env python3

import binascii
import codecs
import math

from score import score

def main():
    cipherBytes = bytes()
    with open('6-ciphertext.txt', 'rb') as ciphertextFile:
        ciphertext = ciphertextFile.read()
    cipherBytes = base64ToBytes(ciphertext)
    bestKeySizes = getBestKeySizes(cipherBytes)

    print(bestKeySizes)

    for keysize in bestKeySizes:
        blocks = splitBytearrayIntoSize(keysize, cipherBytes)
        transposedBlocks = transposeBlocks(blocks)

        key = ''
        blockIndex = 0
        for block in transposedBlocks:
            results = []
            for character in [chr(i) for i in range(1, 128)]:
                if character.isprintable():
                    tryCharacter(block, character, results)

            sortedResults = sorted(results, key=lambda result: -result.get('score'))
            for result in sortedResults:
                if result.get('score') > 0:
                    #print('{}: {}\t{}\n{}\n\n'.format(blockIndex, result.get('score'), result.get('key'), result.get('xord')))
                    pass
            key += sortedResults[0].get('key')
            blockIndex += 1

        print(keysize)
        print(key)
        # KEY IS:
        # Terminator X: Bring the noise

def transposeBlocks(blocks):
    transposed = getListOfBytearrays(len(blocks[0]))

    for block in blocks:
        i = 0
        for byte in block:
            transposed[i].append(byte)
            i += 1

    return transposed

def splitBytearrayIntoSize(size, b):
    innerBytearraySize = math.ceil(len(b) / size)
    splitBytearray = getListOfBytearrays(innerBytearraySize)

    i = 0
    for byte in b:
        bytearrayIndex = math.floor(i / size)
        splitBytearray[bytearrayIndex].append(byte)
        i += 1

    return splitBytearray

def getListOfBytearrays(size):
    l = []
    for i in range(0, size):
        l.append(bytearray())
    return l

def getBestKeySizes(cipherBytes):
    keysizeDistances = {}
    for keysize in range(2, 41):
        distance_1 = getHammingDistance(
            cipherBytes[0:keysize],
            cipherBytes[keysize:keysize * 2]
        )
        distance_2 = getHammingDistance(
            cipherBytes[keysize * 2:keysize * 3],
            cipherBytes[keysize * 3:keysize * 4]
        )

        keysizeDistances[keysize] = (distance_1 + distance_2) / 2.0 / keysize

    sortedKeysizeDistances = sorted(keysizeDistances.items(),
            key=lambda x: x[1])
    return [x[0] for x in sortedKeysizeDistances[:10]]

def getHammingDistance(bytesA, bytesB):
    distance = 0
    for i in range(0, len(bytesA)):
        for j in range(0, 8):
            bitA = (bytesA[i] >> j) & 0x1
            bitB = (bytesB[i] >> j) & 0x1
            if bitA != bitB:
                distance += 1
    return distance

def tryCharacter(cipherBytes, character, results):
    keyBytes = bytes(character, 'ascii') * len(cipherBytes)
    xord = xor(cipherBytes, keyBytes)
    s = score(xord)

    results.append({
        'character': character,
        'xord': xord,
        'score': s,
        'key': character,
    })

def xor(bytes1, bytes2):
    bytes_len = len(bytes1)
    xord = bytearray(bytes_len)
    for i in range(bytes_len):
        xord[i] = bytes1[i] ^ bytes2[i]
    return xord

def base64ToBytes(the_base64):
    return codecs.decode(the_base64, 'base64')

if __name__ == '__main__':
    main()

