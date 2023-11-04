#!/usr/bin/env python3

frequencies = {}

ciphertext = input("Enter the Ciphertext: ")
ciphertext = ciphertext.replace(" ", "")
ciphertext = ciphertext.upper()

for character in ciphertext:
    if character.isalpha():
        frequencies[character] = frequencies.get(character, 0) + 1 
    
for character, frequency in sorted(frequencies.items(), key = lambda x:x[1], reverse = True):
    print(f"{character}: {frequency} ")