import re

# The class [a-z] matches any lowercase alphabetic character.
# The class [G-P] matches any uppercase character from G to P.
# The class [0-9] matches any digit.
# Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.

pattern = r"[A-Z][A-Z][0-9]"
pattern2 = r"[A-Za-z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")
    
if re.search(pattern, "1ab"):
    print("Match 3")
    
if re.search(pattern2, "a1"):
    print("Match 4")

if re.search(pattern2, "A1"):
    print("Match 5")

if re.search(pattern2, "1a"):
    print("Match 6")