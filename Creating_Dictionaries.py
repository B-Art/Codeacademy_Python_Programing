# What is a dictionary?

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)

# Making a dictionary

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

# Invalid keys
# children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}

# the key must always be unchangeable of hashable data types like numbers or strings
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

# declaring an empty dictionary

empty_dict = {} # easy enough..

# adding a key
# create empty dictionary
animals_in_zoo = {}

# add "zebras" to animals_in_zoo as key with a value of 8
animals_in_zoo["zebras"] = 8

# add more animals!
animals_in_zoo["monkeys"] = 12

# moar!
animals_in_zoo["dinosaurs"] = 0 # sort of...

# print the dictionary
print(animals_in_zoo)

# adding multiple keys
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# overwriting values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

# adding key and value
oscar_winners["Supporting Actress"] = "Viola Davis"

# changing an existing key-value pair
# hmm... this happened in real life...
oscar_winners["Best Picture"] = "Moonlight"

# verify
print(oscar_winners)

# List comprehensions to dictionaries... whoa

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key: value for key, value in zipped_drinks}

print(drinks_to_caffeine)

# review

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# 1
plays = {key: value for key, value in zip(songs, playcounts)}

# 2
print(plays)

# 3
plays["Purple Haze"] = 1

# 4
plays["Respect"] = 94

# 5
library = {"The Best Songs": plays, "Sunday Feelings": {}}

# 6
print(library)


# Using Dictionaries

# Accessing values in a dictionary

# Getting a key

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])

print(zodiac_elements["fire"])

# Getting an invalid key (not in dict) will throw an error

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"])

# try/except to get a key, a means of error-handling

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level['matcha'] = 30

try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")

# "safely" getting a key

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# .pop() method to delete a key
health_points += available_items.pop("stamina grains", 0)

health_points += available_items.pop("power stew", 0)

health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

# get all keys with the .keys() method

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

# get all values with the .values() method

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
                 "dictionaries": 18}

total_exercises = 0

for value in num_exercises.values():
    total_exercises += value

print(total_exercises)

# ... get all items with the .items() method

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for profession, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + profession + "s.")


# Review:
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13, 0)

spread["present"] = tarot.pop(22, 0)

spread["future"] = tarot.pop(10, 0)

for key, value in spread.items():
  print("Your " + key + " is the " + str(value) + " card.")


# code challanges

# Write your add_ten function here:
def add_ten(my_dictionary):
    for key, value in my_dictionary.items():
        my_dictionary[key] += 10

    return my_dictionary


# Uncomment these function calls to test your function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}