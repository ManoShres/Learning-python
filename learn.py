

# break and continue statements
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
for x in range (10):
    if x%2 ==0:
        continue
    print(x)
while count<5:
    print (count)
    count = count+1
from curses import ACS_GEQUAL
from unicodedata import name


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
