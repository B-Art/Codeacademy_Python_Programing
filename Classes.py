print(type(5))

my_dict = {}
print(type(my_dict))

my_list = [num for num in range(100)]
print(type(my_list))
print(my_list)

class Circle():
    # constant
    pi = 3.14

    # method
    def area(self, radius):
        return self.pi * radius ** 2


# Python Class
class CoolClass:
  pass

class Facade:
  pass


# Class instatiation
class Facade:
  pass

# a Facade instance
facade_1 = Facade()

# Object-oriented programming
class Facade:
  pass

facade_1 = Facade()

facade_1_type = type(facade_1)
print(facade_1_type)


# Class variables
class Grade:
  minimum_passing = 65


# Methods
class Rules():
    # method
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


# Methods with Arguments
class Circle():
    # constant
    pi = 3.14

    # method
    def area(self, radius):
        return self.pi * radius ** 2

circle = Circle()
pizza_area = circle.area(12 * 0.5)
teaching_table_area = circle.area(36 * 0.5)
round_room_area = circle.area(11460 * 0.5)

big_circle = Circle()
print(big_circle.area(50))

pizza_area = big_circle.area(12 * 0.5)
teaching_table_area = big_circle.area(36 * 0.5)
round_room_area = big_circle.area(11460 * 0.5)
print(pizza_area, teaching_table_area, round_room_area)


# Constructors
class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print("New circle with diameter: " + str(diameter))

teaching_table = Circle(36)


# Instant Variables
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


# Attribute Functions
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

"""
Python functions that checks for attibutes within an object

hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value
"""
s_count = 0

for item in how_many_s:
  if hasattr(item, "count") == True:
    for x in item:
      if x == "s":
        s_count += 1

print(s_count)


# self
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = 0.5 * diameter

    def circumference(self):
        return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())


# Everything is an object
print(dir(5))

def this_function_is_an_object(num):
  return "Cheese is {} times better than everything else".format(num)

print(dir(this_function_is_an_object))


# String representation
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)


# Review

# 1: Define a class named Student
class Student():
    # 2: Add a constructor for Student, e.g. name and year
    def __init__(self, name, year):
        self.name = name
        self.year = year

        # 6 ...
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)
        else:
            pass


# 4: Create a Grade class with minimum passing = 65
class Grade():
    minimum_passing = 65

    # 5: Give grade a constructor, param is score
    def __init__(self, score):
        self.score = score


# 3: Create three instances of the Student class:
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))