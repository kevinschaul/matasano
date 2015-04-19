#!/usr/bin/env ruby

require 'base64'
require 'set'

# Read ciphertext file
lines = File.open('8-ciphertext.txt', 'rb').readlines
bytes_array = lines.map{ |line| Base64.decode64(line) }

# Split cipherbytes into 8 or 16 byte blocks
# Keep in mind the key is probably 128 or 256 bits long (8 or 16 bytes)
KEYSIZE = 16
bytes_array.each do |bytes|
    num_blocks = (bytes.length / KEYSIZE).ceil
    blocks = []
    for i in 0..num_blocks do
        block = bytes[i * KEYSIZE..i * KEYSIZE + KEYSIZE - 1]
        blocks.push(block)
        #puts Base64.encode64(block)
        #puts block.unpack('H*')
    end

    # Create a set to remove duplicates
    set = blocks.to_set

    # If the lengths are different, we found repetition. This may
    # indicate CBC mode.
    if blocks.length != set.length
        puts
        puts "CBC possibly detected, #{blocks.length - set.length} byte sequences of length #{KEYSIZE} match"
        puts "Ciphertext was:"
        puts Base64.encode64(bytes)
    end
end
