# OverTheWire Krypton Walkthrough

Hello, my name is Kevin Ngo. Welcome to my walkthrough of the Krypton wargame. In this repo, you'll find:
* My walkthrough in PDF format
* All of the Python code I wrote to solve the challenges

Furthermore, in this README, I'll explain how each program works.

## rot13.py
rot13.py encrypts/decrypts any given string using the ROT13 algorithm. It works using two dictionaries, one to store lower case letters along with their indexes, and the other to store upper case letters. Respective lists are then made from these dictionaries to exclusively store the letters. The user inputs a message via STDIN, then the program loops through each character in the string. Each character is shifted forward by 13 characters using the operation: (characterIndex + 13) mod 26. The shifted character is concatenated to the “decoded” string and printed after all characters have been looped over. Due to the limitations of ROT13, any character that isn’t in the alphabet is not shifted. 

## caesar_decrypt.py
This program is essentially the same as rot13.py. The only differences are that it takes a user-inputted shift value rather than a constant value of 13, and the operation (characterIndex + 13) mod 2 is changed to (characterIndex - shift) mod 26.

## freq_analysis.py
freq_analysis.py performs single letter frequency analysis on a user inputted string. The program simply loops over each character in the string, and checks if it is an alphabetic letter. If so, it will add the letter to the frequencies dictionary (if the letter isn't already in the dictionary) and increment its frequency value. After each character has been considered, the program will print each letter in the dictionary alongside its frequency in descending order. This is done via a lambda function within the sorted function. 

## split.py
split.py performs a specific operation required for cracking polyalphabetic substitution ciphers (such as Vignere ciphers). It creates substrings from a user-inputted ciphertext where each substring consists of every x letters starting from the n-th position of the ciphertext, where x refers to the user-inputted key length. This concept is further explained in the walkthrough. The program accomplishes this using a nested for-loop and the range function. The outer for loop determines which index of the ciphertext the split will start from. Whereas the inner for loop extracts every x letter starting from said index. Each letter is concactenated into a 'curr_string'. After the inner loop finishes, curr_string is appended to a string_list. Finally, the string_list is printed after the outer for_loop finishes.
