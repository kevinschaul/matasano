#!/usr/bin/env python3

import binascii
import codecs

def main():
    h = getHammingDistance('this is a test', 'wokka wokka!!!')
    print('Should be 37: {}'.format(h))

def getHammingDistance(a, b):
    bytesA = a.encode()
    bytesB = b.encode()

    distance = 0
    for i in range(0, len(bytesA)):
        for j in range(0, 8):
            bitA = (bytesA[i] >> j) & 0x1
            bitB = (bytesB[i] >> j) & 0x1
            if bitA != bitB:
                distance += 1
    return distance

if __name__ == '__main__':
    main()

