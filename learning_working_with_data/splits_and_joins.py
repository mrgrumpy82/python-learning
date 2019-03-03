text = "Brad Marianne Harrison"

names=text.split(" ")

print(names)

text = "Jan,Feb,Mar,Apr,May,Jun"

months=text.split(",")

print(months)

alphabet="".join(["a","b","c","d","e"])

print(alphabet)

name=list("Brad")

print(name)

name="".join(name)

print(name)

title="mr bradley adam thomas"
title.capitalize()
print(title.title())

title="mr bradley adam thomas"
print("brad" in title)

print("marianne" not in title)
print("thomas" not in title)