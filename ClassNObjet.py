from tkinter import Variable


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
