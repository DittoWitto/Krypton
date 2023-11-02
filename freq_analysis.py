#!/usr/bin/env python3

frequencies = {}

ciphertext = input("Enter the Ciphertext: ")
ngrams = input("Enter the n-gram count: ")

# if int(ngrams) != 1 or int(ngrams) != 2:
#     print("Usage: n-gram count must be either 1 or 2.")
#     exit(0)
    
for character in ciphertext:
    frequencies[character] = frequencies.get(character, 0) + 1 
    
for character, frequency in sorted(frequencies.items(), key = lambda x:x[1], reverse = True):
    print(f"{character}: {frequency} ")