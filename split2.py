#!/usr/bin/env python3

key_length = input("Enter the key length: ")
key_length = int(key_length)
ciphertext = input("Enter the ciphertext: ")
ciphertext = ciphertext.replace(" ", "")

string_list = []

for step in range(key_length):
  curr_string = ''
  for pos in range(step, len(ciphertext), key_length):
    curr_string = curr_string + ciphertext[pos]
  string_list.append(curr_string)
  
print(string_list)