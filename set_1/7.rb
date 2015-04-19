#!/usr/bin/env ruby

require 'base64'
require 'openssl'

# Read ciphertext, convert from base64
ciphertext = File.open('7-ciphertext.txt', 'rb').read
cipherbytes = Base64.decode64(ciphertext)

# Decrypt
key = 'YELLOW SUBMARINE'

aes_cipher = OpenSSL::Cipher.new('aes-128-ecb')
aes_cipher.decrypt
aes_cipher.key = key

plaintext = aes_cipher.update(cipherbytes) + aes_cipher.final

puts plaintext
