import re

# Some more metacharacters are * + ? { and }.
# These specify numbers of repetitions.

# Curly braces can be used to represent the number of repetitions between two numbers.
# The regex {x,y} means "between x and y repetitions of something".
# Hence {0,1} is the same thing as ?.
# If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.

pattern = r"9{1,3}$"

if re.match(pattern, "0"):
    print("Match 1")

if re.match(pattern, "9"):
    print("Match 2")
    
if re.match(pattern, "99"):
    print("Match 3")
    
if re.match(pattern, "999"):
    print("Match 4")
    
if re.match(pattern, "9999"):
    print("Match 5")
    
if re.match(pattern, "99099"):
    print("Match 6")