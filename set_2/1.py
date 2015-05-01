#!/usr/bin/env python3

import codecs

def main():
    string = 'YELLOW SUBMARINE'
    the_bytes = bytes(string, 'ascii')
    print(the_bytes)
    padded_bytes = pad(the_bytes, 20)
    print(padded_bytes)

def hexToBytes(the_hex):
    return codecs.decode(the_hex, 'hex_codec')

def bytesToBase64(the_bytes):
    return codecs.encode(the_bytes, 'base64')

def pad(the_bytes, block_length):
    """
    Returns a PKCS#7-padded version of `the_bytes`, padded to a length of
    `block_length`.
    """
    pad_length = block_length % len(the_bytes)
    pad_bytes = bytearray([pad_length for x in range(pad_length)])
    return the_bytes + pad_bytes

if __name__ == '__main__':
    main()

