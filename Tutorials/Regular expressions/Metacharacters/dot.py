import re

# The first metacharacter we will look at is . (dot).
# This matches any character, other than a new line.

pattern = r"gr.y"
pattern2 = r"gr/.\y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")
    
if re.match(pattern, "blue"):
    print("Match 3")