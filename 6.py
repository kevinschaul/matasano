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

    bestKeySizes = range(1, 40)
    print(bestKeySizes)

    for keysize in bestKeySizes:
        blocks = splitBytearrayIntoSize(keysize, cipherBytes)
        transposedBlocks = transposeBlocks(blocks)

        key = ''
        blockIndex = 0
        for block in transposedBlocks:
            results = []
            for character in [chr(i) for i in range(1, 128)]:
                tryCharacter(block, character, results)

            sortedResults = sorted(results, key=lambda result: -result.get('score'))
            for result in sortedResults[:8]:
                if result.get('score') > 0:
                    pass
                    #print('{}: {}\t{}\n{}\n\n'.format(blockIndex, result.get('score'), result.get('key'), result.get('xord')))
            key += sortedResults[0].get('key')
            blockIndex += 1
            #print()
            #print()
            #print()

        print(key)

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
    for keysize in range(2, 10):
        distance = getHammingDistance(
            cipherBytes[0:keysize],
            cipherBytes[keysize:keysize * 2]
        )
        keysizeDistances[keysize] = distance / keysize

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

def isEnglishCharacter(c):
    """
    Returns whether the character is generally used in English writing.
    """
    return True
    if c.isalpha() or c in [' ', '\t', '\n', '.', ',', '?', '!', ';', ':',
            '\'', '"', '/', '\\', '(', ')', '[', ']', '#', '$', '%', '&', '-',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False

def score(plaintext_bytes):
    """
    Attempts to score a string based on closeness to expected English
    letter frequencies.

    Scores range from 0 to 1, with 1 being a perfect match to the expected
    frequencies.
    """
    plaintext = plaintext_bytes.decode('utf-8')
    plaintextLength = len(plaintext)
    letters = [letter.lower() for letter in plaintext if isEnglishCharacter(letter)]
    lettersLength = len(letters)
    printables = [character for character in plaintext if character.isprintable()]
    if len(letters) != len(printables):
        return 0
    counts = {}
    for letter in letters:
        count = counts.get(letter, 0)
        counts[letter] = count + 1

    difference = 0
    frequencies = {}
    for letter in counts:
        count = counts.get(letter)
        expected = expected_frequencies.get(letter, 0) * lettersLength
        difference += abs(count - expected)

    if lettersLength == 0:
        differencePerLetter = 1
    else:
        differencePerLetter = difference / lettersLength

    if plaintextLength == 0:
        percentLetters = 0
    else:
        percentLetters = lettersLength / plaintextLength

    # differencePerLetter should be close to 0
    # percentLetters should be close to 1
    return abs(1 - differencePerLetter) * percentLetters

def xor(bytes1, bytes2):
    bytes_len = len(bytes1)
    xord = bytearray(bytes_len)
    for i in range(bytes_len):
        xord[i] = bytes1[i] ^ bytes2[i]
    return xord

def base64ToBytes(the_base64):
    return codecs.decode(the_base64, 'base64')

# Expected frequencies via WikiPedia:
# https://en.wikipedia.org/wiki/Letter_frequency
expected_frequencies = {
    'a': .08167,
    'b': .01492,
    'c': .02782,
    'd': .04253,
    'e': .13000,
    'f': .02228,
    'g': .02015,
    'h': .06094,
    'i': .06966,
    'j': .00153,
    'k': .00772,
    'l': .04025,
    'm': .02406,
    'n': .06749,
    'o': .07507,
    'p': .01929,
    'q': .00095,
    'r': .05987,
    's': .06327,
    't': .09056,
    'u': .02758,
    'v': .00978,
    'w': .02360,
    'x': .00150,
    'y': .01974,
    'z': .00074,
}

if __name__ == '__main__':
    main()

