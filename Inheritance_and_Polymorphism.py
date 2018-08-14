# Inheritance

# Example case
class User: # this is the base class
  is_admin = False
  def __init__(self, username):
    self.username = username

class Admin(User): # Admin is the subclass, having the same constructor of User but is_admin differs between the two
  # the base class is also known as the child class
  is_admin = True

# Practice
class Bin:
  pass

# RecyclingBin is a type of Bin
class RecyclingBin(Bin):
  pass


# Exceptions

"""
An Exception is a class that inherits from Python's Exception class.
"""

class OutOfStock(Exception):
  pass


# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"

  def __init__(self, stock):
    self.stock = stock

  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
candle_shop.buy('green')


# override methods, case of a messaging system

class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text


class User:
  def __init__(self, username):
    self.username = username

  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

# Create an Admin class that subclasses the User class.
class Admin(User):
  # Override User's .edit_message() method in Admin so that an Admin can edit any messages.
  def edit_message(self, message, new_text):
    message.text = new_text


"""
Overriding methods is really useful in some cases but sometimes we want to add some extra logic to the existing method.
In order to do that we need a way to call the method from the parent class. Python gives us a way to do that using super().
"""


class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40

# Interfaces
"""
When two classes have the same method names and attributes, we say they implement the same interface.
"""


class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item


# create a subclass of InsurancePolicy
class VehicleInsurance(InsurancePolicy):
  def __init__(self, price_of_item):
    self.price_of_vehicle = price_of_item

  # declare a .get_rate() method
  def get_rate(self):
    return 0.001 * self.price_of_vehicle


# create another subclass of InsurancePolicy
class HomeInsurance(InsurancePolicy):
  def __init__(self, price_of_item):
    self.price_of_home = price_of_item

  # declare a .get_rate() method
  def get_rate(self):
    return 0.00005 * self.price_of_home


# polymorphism refers how an action could become different depending on the data type it handles

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))
print(len(a_dict))
print(len(a_string))


class Atom:
  def __init__(self, label):
    self.label = label

  def __add__(self, other):
    return Molecule([self, other])

class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms

sodium = Atom("Na")
chlorine = Atom("Cl")
#salt = Molecule([sodium, chlorine])
salt = sodium + chlorine
print(salt)

class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyer):
    return lawyer in self.lawyers

d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])


class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()

test = SortedList([4, 1, 5])
print(test)
test.append(15)
print(test)