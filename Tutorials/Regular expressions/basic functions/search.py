import re

pattern = r"pam"
word = "eggspamsausage"

match = re.search(pattern, word)

if match:
    print(match)
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

