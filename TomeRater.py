class User(object):

    # Constructor method
    def __init__(self, name, email):
        self.name = name # string
        self.email = email # string
        self.books = {} # empty dictionary that will map a Book object to a user's rating of the book

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email address has been updated.")

    def __repr__(self):
        return "User {name}, email: {email}, number of books read: {books_count}".format(name=self.name, email=self.email, books_count=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        # a way of "appending" elements to a dictionary
        self.books[book] = rating

    def get_average_rating(self):
        list_of_ratings = self.books.values()
        sum = 0
        length_of_rating = 0
        for rating in list_of_ratings:
            if rating == None:
                pass
            else:
                sum += rating
                length_of_rating += 1
        return sum / length_of_rating


# The __eq__ dunder method is new to me, so the next 6 lines is a test of equality
william = User("William", "wchian2@uic.edu")
jack = User("William", "wchian2@uic.edu")
other_jack = User("William", "william.chiang@domain.com")

print("Equality result: " + str(william == jack)) # prints out true, oh I get it...
print("Equality result: " + str(william == other_jack)) # prints out false

# Testing the get_average_rating method.. looks good
william.read_book("Of mice and men", 9)
william.read_book("Batman", 17.5)
william.read_book("A Work in Progress")
william.read_book("Testing Self", 22.5)
print(william.get_average_rating())


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

    # the following method will make the Book class hashable
    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title}".format(title=self.title)


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

# This important class allows interaction between the User and Books class!
class TomeRater(object):

    def __init__(self):
        self.users = {} # empty dictionary that will map a user's email to the User object
        self.books = {} # empty dictionary that will map Book objects to the number of users who read it

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, isbn, author)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users.keys():
            print("No user with email {email}".format(email=email))
        else:
            self.users[email].read_book(book, rating)
            if book not in self.books.keys():
                self.books[book] = 1
                book.add_rating(rating)
            else:
                self.books[book] += 1
                book.add_rating(rating)


    def add_user(self, name, email, books=None):
        new_user = User(name, email)
        self.users[email] = new_user

        if books != None:
            for book in books:
                self.add_book_to_user(book, email)


#test = TomeRater()
#test.add_book_to_user("How to Python", "wchian2@uic.edu")
#test.add_user("Michael", "mstevens@gmail.com", ["Dicey", "Running Times"])
#test.add_book_to_user("How to Python", "mstevens@gmail.com")
#test.add_user("Some Guy", "some_dude@gmail.com")
#test.add_book_to_user("Finally, a new book", "some_dude@gmail.com")
#test.add_user("Pythonista", "pythonista@psf.com", ["How to Python"])
#print(test.users["mstevens@gmail.com"].books)
#print(test.books)

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1.0)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3.0)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3.0)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4.0)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1.0)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)



