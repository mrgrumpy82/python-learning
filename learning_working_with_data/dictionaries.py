phonebook = {"Brad": 1234, "Mez": 4567, "Harry": 6789 }

print(phonebook)

print(phonebook["Brad"])

phonebook["Summer"] = 0000

print(phonebook)

del phonebook["Summer"]

print(phonebook)

file={}

name=input("Enter name: ")
number=int(input("Enter number: "))

file[name] = number

print(file["Brad"])