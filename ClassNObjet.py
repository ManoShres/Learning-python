from tkinter import Variable
from unicodedata import name


class Klass:
    variable = "Maa"

    def punction(self):
        print("this is function")
abjectOne = Klass()
abjectTwo = Klass()

abjectTwo.variable = "Baa"
print(abjectOne.variable)
print(abjectTwo.variable)

# Accessing Object Functions
class Klass:
    Variable = "Maa"

    def punction(self):
        print("This is accessing object functions that is inside the class.")

abjectThree = Klass()
abjectThree.punction()

#_ini_
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

### Exercise
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str     
# your code goes here
car1 = Vehicle()
car1.name = "Toyata"
car1.color = "Red"
car1.value = 60000

car2 = Vehicle()
car2.name = "Tesla"
car2.color = "Red"
car2.value = 160000
# test code
print(car1.description())
print(car2.description())