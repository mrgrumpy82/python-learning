# try:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else:
#     print("You didn't divide by zero")

try:
    txt = open("file.txt", "w")
    txt.write("This is a test. Normal service will shortly resume")
except IOError:
    print("Error: unable to write the file. Check permissions")
else:
    print("Content written to file successfully")
    txt.close