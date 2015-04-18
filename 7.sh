#!/usr/bin/env bash

openssl enc -d -base64 -in 7-ciphertext.txt | openssl enc -d -aes-128-ecb -k "YELLOW SUBMARINE"
