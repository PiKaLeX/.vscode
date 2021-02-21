import re

pattern = r"spam"
word = "egg" + "spam" * 3

if re.match(pattern, word):
    print("Match")
else:
    print("No Match")

if re.search(pattern, word):
    print("Match")
else:
    print("No Match")

print(re.findall(pattern, word))