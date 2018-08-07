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