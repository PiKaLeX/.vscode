import re

#1 There are various special sequences you can use in regular expressions. They are written as a backslash followed by another character.
#1 One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This matches the expression of the group of that number.

pattern = r"(.+) \1"

# Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression, which is the matched expression itself, and not the regex pattern.

match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "!? !?")
if match:
    print("Match 2")

match = re.match(pattern, "abc cde")
if match:
    print("Match 3")