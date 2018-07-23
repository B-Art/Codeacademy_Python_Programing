# Formatting Methods
# There are three string methods that can change the casing of a string. These are .lower(), .upper(), and .title().

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

# .split() is performed on a string, takes one argument, and returns a list of substrings found between the given
# argument (which in the case of .split() is known as the delimiter).

line_one = "The sky has given over"

line_one_words = line_one.split()
print(line_one_words)

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(', ')
print(author_names)

author_last_names = [last_name.split()[-1] for last_name in author_names]
print(author_last_names)

spring_storm_text = \
"""The sky has given over
its bitterness.
Out of the dark change
all day long
rain falls and falls
as if it would never end.
Still the snow keeps
its hold on the ground.
But water, water
from a thousand runnels!
It collects swiftly,
dappled with black
cuts a way for itself
through green ice in the gutters.
Drop after drop it falls
from the withered grass-stems
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split(' \n')
print(spring_storm_lines)

# join()
# join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter.
# The syntax of .join() is:

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

# .strip()

# When working with strings that come from real data, you will often find that the strings aren't super clean.
# You'll find lots of extra whitespace, unnecessary linebreaks, and rogue tabs.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = [line.strip() for line in love_maybe_lines]
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# .replace
# string_name.replace(character_being_replaced, new_character)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)

# .find()
# find() takes a string as an argument and searching the string it was run on for that string.
# It then returns the first index value where that string is located.

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

# .format()
# .format() takes variables as an argument and includes them in the string that it is run on.
# You include {} marks as placeholders for where those variables will be imported.

def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))

# part 2

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

print(poem_description(2017, "Edwin Lefevre", "Reminiscences of a Stock Operator", "Albatross Publishers"))

my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

# Review
# Excellent work! This lesson has shown you the vast variety of string methods and their power. Whatever the problem
# you are trying to solve, if you are working with strings then string methods are likely going to be part of the solution.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# 1
print(highlighted_poems)

# 2
highlighted_poems_list = highlighted_poems.split(',')

# 3
print(highlighted_poems_list)

# 4
highlighted_poems_stripped = [item.strip() for item in highlighted_poems_list]

# 5
print(highlighted_poems_stripped)

# 6
highlighted_poems_details = []

# 7
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

# 8
titles = []
poets = []
dates = []

# 9
for item in highlighted_poems_details:
  titles.append(item[0])
  poets.append(item[1])
  dates.append(item[2])

for x in range(0, len(titles)):
  print("The poem {title} was published by {poet} in {date}.".format(title=titles[x], poet=poets[x], date=dates[x]))