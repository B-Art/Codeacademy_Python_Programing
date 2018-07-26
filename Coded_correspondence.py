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
punctuation = "!?.'"

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

# the function below takes the reverse direction by taking a message as an argument and encodes it into a ciphertext
# according to a defined offset which is the number of positions to the *left* of the alphabet
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
# should print the encoded message appearing in line 60 as an argument for the decode function


# decode this: "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(decode("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.",10))
# this prints "the offset for the second message is fourteen."

# now decode the second message "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(decode("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14)) # 14 offset
# this prints "performing multiple caesar ciphers to code your messages is even more secure!"

# brute-force decryption... when the offset is not given to you...
# vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm
# mh dxxi hnk fxlltzxl ltyx.

# i am not typing out every possible offset to call out the decode function, so I'll run a for-loop as shown below
for i in range(100):
    print(decode("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx "
                 "by px ptgm mh dxxi hnk fxlltzxl ltyx.", i) + " (The offset was " + str(i) + ".)")
# the for loop above also prints out the offset of which the message resembled the English language
# after reading out the 100 printouts, the only readable message was with an offset of 7 (everything else was gibberish)
# Result: "computers have rendered all of these old ciphers as obsolete. we'll have to really step up our game
# if we want to keep our messages safe." (The offset was 7.) ... true that

# Now comes the harder cryptography method to implement... The Vigenere Cipher
# Originally developed by Giovan Battista Ballaso in 1553, Blaise de Vigenere enhanced the polyalphabetic cipher
# where each letter of the message are shifted according to the corresponding cipher key, unlike the monoalphabetic
# cipher of how Caesar would encrypt messages
# The Vegenere Cipher confers a stronger encryption as the user could use virtually *any* key to influence how the
# message is encoded into cipher text

# To encode each letter of the plaintext: take the index of letter *respective to the alphabet ("a" is 0, "b" is 1,
# "c" is 2, and so forth) and add that to the corresponding index of letter of the key, and the sum is the index of the
# encoded letter - if the index >= 26, subtract 26 to get the actual index (i.e. "z" is 25 but there is nothing at 26)

def vigenere_letter_encode(plaintext_letter, key_letter):
    index_plaintext_letter = alphabet.find(plaintext_letter)
    index_key_letter = alphabet.find(key_letter)
    encoded_index = index_plaintext_letter + index_key_letter

    if encoded_index > 25:
        return alphabet[encoded_index - 26] # based on the comment made on line 119
    else:
        return alphabet[encoded_index] # simple enough..

# testing
print(vigenere_letter_encode("b", "d")) # should print "e"
print(vigenere_letter_encode("a", "o")) # should print "o"
print(vigenere_letter_encode("r", "g")) # should print "x"
print(vigenere_letter_encode("t", "o")) # should print "h"
# great!

# now, if the key is shorter in length than the message, the key is repeated as a string to match the message length
def vigenere_encode(message, keyword):
    modified_keyword = ""
    for i in range(len(message)):
        modified_keyword += keyword[i % len(keyword)] # modulo to the rescue!

    # test 1 below
    #print(message)
    #print(modified_keyword)

    ciphertext = ""
    for i in range(len(message)):
        if message[i] in punctuation:
            ciphertext += message[i]
        elif message[i] is " ":
            ciphertext += " "
        else:
            ciphertext += vigenere_letter_encode(message[i], modified_keyword[i])

    return ciphertext

# test
print(vigenere_encode("hello my name is william!!", "friend"))

print(vigenere_encode("barryisthespy", "dog"))
print("eoxumovhnhgvb")


# now going the reverse direction...
def vigenere_letter_decode(ciphertext_letter, key_letter):
    index_ciphertext_letter = alphabet.find(ciphertext_letter)
    index_key_letter = alphabet.find(key_letter)
    decoded_index = index_ciphertext_letter - index_key_letter
    return decoded_index

def vigenere_decode(ciphertext, keyword):
    modified_keyword = ""
    for i in range(len(ciphertext)):
        modified_keyword += keyword[i % len(keyword)]

    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i] in punctuation:
            plaintext += ciphertext[i]
        elif ciphertext[i] is " ":
            plaintext += " "
        else:
            plaintext += alphabet[vigenere_letter_decode(ciphertext[i], modified_keyword[i])]
    return plaintext

print(vigenere_decode("eoxumovhnhgvb", "dog"))

# now the grand finale
print(vigenere_decode("dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!",
                      "friends"))

# message: you were able to decode this? nice work! you are becoming quite the expert at crytography!
# Done.