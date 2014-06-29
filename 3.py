#!/usr/bin/env python3

import codecs
import re

results = []

def main():
    hex1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    bytes1 = hexToBytes(hex1)

    for character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        tryCharacter(bytes1, character)

    sortedResults = sorted(results, key=lambda result: result.get('score'))
    for result in sortedResults[-5:]:
        print('{}: {}\n'.format(result.get('xord'), result.get('score')))

def tryCharacter(cipherBytes, character):
    keyBytes = bytes(character, 'ascii') * len(cipherBytes)
    xord = xor(cipherBytes, keyBytes)
    s = score(str(xord))

    results.append({
        'character': character,
        'xord': xord,
        'score': s,
    })

def score(plaintext):
    """
    Attempts to score a string based on closeness to expected English
    letter frequencies.

    Scores range from 0 to 1, with 1 being a perfect match to the expected
    frequencies.
    """
    plaintextLength = len(plaintext)
    letters = [letter.lower() for letter in plaintext if letter.isalpha()]
    lettersLength = len(letters)
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
    return (1 * abs(1 - differencePerLetter)) + (100 * percentLetters)

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

