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