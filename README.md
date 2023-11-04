# Krypton

The above code I produced works using two dictionaries, one to store lower case letters along with their indexes, and the other to store upper case letters. The user inputs a message via STDIN, then the program loops through each character in the string. Each character is shifted forward by 13 characters using the operation: (characterIndex + 13) mod 26. The shifted character is concatenated to the “decoded” string and printed after all characters have been looped over. Due to the limitations of ROT13, any character that isn’t in the alphabet is not shifted. 
