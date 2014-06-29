#!/usr/bin/env python3

import codecs

def main():
    the_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# 0x49      0x27      0x6d
# 0100 1001 0010 0111 0110 1101
# 010010 010010 011101 101101
# 18 18 30 45
# S S e t

    the_bytes = hexToBytes(the_hex)
    the_hex_again = bytesToBase64(the_bytes)

    print(the_bytes)
    print(the_hex_again)

def hexToBytes(the_hex):
    return codecs.decode(the_hex, 'hex_codec')

def bytesToBase64(the_bytes):
    return codecs.encode(the_bytes, 'base64')

if __name__ == '__main__':
    main()

