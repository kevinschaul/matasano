#!/usr/bin/env python3

import codecs

def main():
    hex1 = '1c0111001f010100061a024b53535009181c'
    hex2 = '686974207468652062756c6c277320657965'

    bytes1 = hexToBytes(hex1)
    bytes2 = hexToBytes(hex2)

    xord = xor(bytes1, bytes2)
    print(xord)
    print(bytesToBase64(xord))

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

