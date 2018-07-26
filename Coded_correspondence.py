# The following describes the writing of a cipher decryption tool in Python.
# Historically, the Caesar cipher was conceived by Julius Caesar himself to secure his private communications.
# Each letter are replaced by a letter that is shifted by a certain number of positions up or down the alphabet.


import string

# declare alphabets
alphabet = string.ascii_lowercase

print(alphabet.find('a'))

# declare punctuations, they are not encrypted
punctuation = "!?."

# test
print("." in punctuation) # should print out True

# q -> a
print(26%25 - 1) # shifted by 10 indices to the right, should print "a"

# y -> i
print(34%25 - 1) # shifted by 10 indices to the right, should print "i"

# z -> j
print(35%25 - 1) # shifted by 10 indices to the right, should print "j"

# this will be a helper function taking a letter and offset as inputs, which outputs the deciphered letter
def letter_reassign(letter, offset):
    letter_index = alphabet.find(letter)
    offset_index = letter_index + offset
    if offset_index > 25: # in case the new index goes over 25, the modulo '%' helps greatly
        return alphabet[offset_index % 25 - 1] # line 18, 21, and 24 confirms this declaration
    else:
        return alphabet[offset_index]

print(letter_reassign('q', 10))
some_letter = letter_reassign("a", 10)
print("Converted letter: " + some_letter)

# the main function, which will call out letter_reassign function
def decode(sentence, cipherdex):
    words = sentence.split(" ")

    new_sentence = ""
    for letter in sentence:
        if letter in punctuation:
            new_sentence += letter
        elif letter is " ":
            new_sentence += " "
        else:
            new_sentence += letter_reassign(letter, cipherdex)
    return new_sentence

print(decode("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!", 10))

# this prints: "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"