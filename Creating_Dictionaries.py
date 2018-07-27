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