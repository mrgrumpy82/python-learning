import time

# text=open("file.txt")

# line=text.readlines()

# print(line[0])
# print(line[2])
# print(line[4])

# text=open("file.txt")
# for lines in text:
#     print(lines)

text=open("file.txt")
lines=text.read()
for lines in lines:
    print(lines, end="")
    time.sleep(.15)