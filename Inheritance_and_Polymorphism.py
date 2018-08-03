# Inheritance

# Example case
class User:
  is_admin = False
  def __init__(self, username):
    self.username = username

class Admin(User):
  is_admin = True

# Practice
class Bin:
  pass

# RecyclingBin is a type of Bin
class RecyclingBin(Bin):
  pass