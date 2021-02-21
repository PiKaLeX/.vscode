import re

name = "Alex"
str = f"My name is {name}. Hi {name}"
pattern = r"{0}".format(name)

newstr = re.sub(pattern, "Sophie", str)
print(str)
print(newstr)


