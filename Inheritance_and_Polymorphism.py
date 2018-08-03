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