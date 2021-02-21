import re

# Place a ^ at the start of a character class to invert it.
# This causes it to match any character other than the ones included.
# Other metacharacters such as $ and ., have no meaning within character classes.
# The metacharacter ^ has no meaning unless it is the first character in a class.

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbcdefG123"):
    print("Match 2")
    
if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")