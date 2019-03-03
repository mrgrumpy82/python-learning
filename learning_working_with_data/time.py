import time
print(time.asctime())

print(time.localtime())

print(time.strftime('%A'))
print(time.strftime('%a'))
print(time.strftime('%B'))
print(time.strftime('%b'))
print(time.strftime('%H'))
print(time.strftime('%H:%M'))

# name=input("Enter login name: ")
# print("Welcome", name)
# print("User:", name, "logged in at", time.strftime("%H:%M"))

start_time=time.time()
name=input("Enter login name: ")
end_time=time.time()-start_time
print("Welcome", name)
print("User:", name, "logged in at", time.strftime("%H:%M"))
print("It took", name, end_time, "to login.")
