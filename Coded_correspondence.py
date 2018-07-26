# The following describes the writing of a cipher decryption tool in Python
# Historically, the Caesar cipher was conceived by Julius Caesar himself to secure his private communications
# Each letter are replaced by a letter that is shifted by a certain number of positions up or down the alphabet
# We will take a encrypted message with letters shifted to the right by 10 positions and write a decryption algorithm
# Line 54 shows the code in action and line 57 prints out the solution

import string

# declare alphabets
alphabet = string.ascii_lowercase # this is why I am importing the string library in line 7

print(alphabet.find('a'))

# declare punctuations, they are not encrypted
punctuation = "!?."

# test
print("." in punctuation) # should print out True

# more testing
# q -> a
# "q" with index of 16 when shifted by 10 indices to the right makes an index for 26
# but alphabet goes up to only to the 25th index...
# we will use the "%" (modulo) which takes the remainder after dividing the new index and subtract 1
# it's a math trick and it works
print(26%25 - 1) # 16+10 divided by 25 has a remainder of 1... 1 - 1 = 0, the alphabet with 0 index is "a"

# y -> i
print(34%25 - 1) # 24+10 divided by 25 has a remainder of 9... 9 - 1 = 8, index 8 refers to letter "i"

# z -> j
print(35%25 - 1) # just for more show, "z" index of 25 + 10 offset = 35; remainder is 10, subtract 1: 9 -> "j"

# this will be a helper function taking a letter and offset as inputs, which outputs the deciphered letter
def letter_reassign(letter, offset):
    letter_index = alphabet.find(letter)
    offset_index = letter_index + offset
    if offset_index > 25: # in case the new index goes over 25, the modulo '%' helps greatly
        return alphabet[offset_index % 25 - 1] # line 26, 29, and 32 confirms this declaration
    else:
        return alphabet[offset_index]

# testing out the letter_reassign function
print(letter_reassign('q', 10)) # should print "a"
some_letter = letter_reassign("a", 10)
print("Reassigned letter: " + some_letter) # should print "Converted letter: k"

# the main function, which will call out letter_reassign function
def decode(ciphertext, cipherdex):
    new_sentence = ""
    for letter in ciphertext:
        if letter in punctuation:
            new_sentence += letter
        elif letter is " ":
            new_sentence += " "
        else:
            new_sentence += letter_reassign(letter, cipherdex)
    return new_sentence

print(decode("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q "
             "cuiiqwu rqsa myjx jxu iqcu evviuj!", 10))

# this prints: "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me
# a message back with the same offset!"

def letter_encode(letter, offset):
    letter_index = alphabet.find(letter)
    new_index = letter_index - offset # if new_index is negative, a index of -1 in alphabet is "z", -2 for "y"...
    return alphabet[new_index]

def encode(message, offset):
    ciphertext = ""
    for letter in message:
        if letter in punctuation:
            ciphertext += letter
        elif letter is " ":
            ciphertext += " "
        else:
            ciphertext += letter_encode(letter, offset)
    return ciphertext

print(encode("hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me "
             "a message back with the same offset!", 10))
# should print the encoded message appearing in line 63 as an argument for the decode function