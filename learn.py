# while loops
count = 0
while count<5:
    print (count)
    count = count+1
else:
    print("count is more than or equal to 5")

print('hello world')
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append("apple")


# prints out 1,2,3
for y in mylist:
    print(y)
print(mylist[3])

# list
numbers= []
strings= []
names= []

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("Hello")
strings.append("world")

names.append ("Manoj")
names.append("Sunita")
names.append("Mansu")

second_name = names[2]

print(numbers)
print(strings)
print ("The second name is %s" %second_name)

#operator with list
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print (all_numbers)

#String Formatting
name = 'Manoj'
age  = 27
print('Hello %s !! Are you %d yrs old?'%(name,age))

#Function
def namefunction(name,age):
    print("Hello I'm %s and I'm %d yrs old. " %(name, age ))

namefunction("Manoj",27)
