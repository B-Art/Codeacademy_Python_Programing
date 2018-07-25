# 1: This was particularly challenging. When I had the "light bulb", it was not so bad after all...

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Write your unique_english_letters function here:
def unique_english_letters(word):
    count = 0
    unique_letters = []
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)
            count += 1
    return count


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters(letters))


# 2: So much more straightforward than the first problem

# Write your count_char_x function here:
def count_char_x(word, x):
  count = 0
  for letter in word:
    if letter == x:
      count +=1
  return count

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1


# 3

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  return word.count(x)

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


# 4

# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  if start in word and end in word:
    return word[word.find(start) + 1:word.find(end)]
  else:
    return word

print("William".find("i"))
print("William".find("a"))
print(substring_between_letters("William", "i", "i"))

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


# 5
# Write your x_length_words function here:
def x_length_words(sentence, x):
  words = sentence.split(" ")
  print(words)
  for word in words:
    if len(word) < x:
      return False
  return True

# Uncomment these function calls to test your  function:
print(x_length_words("like i apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


# 6

# Write your check_for_name function here:
def check_for_name(sentence, name):
  if name.lower() in sentence or name.upper() in sentence or name.title() in sentence:
    return True
  else:
    return False

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# 7

# Write your every_other_letter function here:
def every_other_letter(word):
    new_string = ""
    for i in range(len(word)):
        if i % 2 == 0:
            new_string += word[i]
    return new_string


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print


# 8

# Write your reverse_string function here:
def reverse_string(word):
    new_string = ""
    index = 0
    for i in range(1, len(word) + 1):
        new_string += word[-i]
    return new_string


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


# 9

# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  new_word1 = word2[0] + word1[1:len(word1)]
  new_word2 = word1[0] + word2[1:len(word2)]
  return " ".join([new_word1, new_word2])


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


# 10

# Write your add_exclamation function here:
def add_exclamation(word):
    new_word = word
    if len(word) < 21:
        for i in range(20 - len(word)):
            new_word += "!"
        return new_word
    else:
        return word


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
print(add_exclamation("William"))