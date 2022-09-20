Phonebook = {
    "Manoj" : 9860941235,
    "Shrestha" : 9808159743,
    "Hemraj" : 9875641230
}
print(Phonebook)

### Iterating over dictionaries

Phonebook = {"Manoj" : 9860941235, "Shrestha" : 9808159743, "Hemraj" : 9875641230}
for name, number in Phonebook.items():
    print("Phone number of %s is %d" %(name, number))

### deleting items for dictionary

Phonebook = {"Manoj" : 9860941235, "Shrestha" : 9808159743, "Hemraj" : 9875641230}
del Phonebook["Shrestha"]
print(Phonebook)
            # OR
Phonebook = {"Manoj" : 9860941235, "Shrestha" : 9808159743, "Hemraj" : 9875641230}
Phonebook.pop("Shrestha")
print(Phonebook)

### Example

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
phonebook["Jake"] =  9876543210
phonebook.pop("Jill")
# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  