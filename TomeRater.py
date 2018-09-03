class User(object):

    # Constructor method
    def __init__(self, name, email):
        self.name = name # string
        self.email = email # string
        self.books = {} # empty dictionary that will map a Book object

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email address has been updated.")

    def __repr__(self):
        return "User {name}, email: {email}, number of books read: {books_count}".format(name=self.name, email=self.email, books_count=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

# The __eq__ dunder method is new to me, so the next 6 lines is a test of equality
william = User("William", "wchian2@uic.edu")
jack = User("William", "wchian2@uic.edu")
other_jack = User("William", "william.chiang@domain.com")

print("Equality result: " + str(william == jack)) # prints out true, oh I get it...
print("Equality result: " + str(william == other_jack)) # prints out false

class Book(object):

    # Constructor method
    def __init__(self, title, isbn):
        self.title = title # string
        self.isbn = isbn # int
        self.ratings = [] # empty list

    # method returning the title of the book
    def get_title(self):
        return self.title

    # method returning the isbn of the book
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN of this book has been updated.")

    def add_rating(self, rating):
        if rating <= 4 and rating > 0:
            self.ratings.append(rating)
        else:
            print("Invalid rating. Please rate between 0 to 4.")

    def __eq__(self, other):
        return self.title == other.title and self.isbn == other.isbn


class Fiction(Book):

    def __init__(self, title, isbn, author):
        # Python 2.7 doesn't support the syntax
        # super().__init__(title, isbn)
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}. ISBN: {isbn}".format(title=self.title, author=self.author, isbn=self.isbn)

alice = Fiction("Alice in Wonderland", 12345, "Lewis Carroll")
print(alice)

class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject # a string, e.g. "Geology"
        self.level = level # a string, e.g. "advanced"

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

society_of_mind = Non_Fiction("Society of Mind", "Artificial Intelligence", "beginner", 100000)
print(society_of_mind)