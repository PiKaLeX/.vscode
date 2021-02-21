import re

# Another important metacharacter is |.
# This means "or", so red|blue matches either "red" or "blue".

pattern = r"gr(a|e)y"

if re.match(pattern, "gray"):
    print("Match 1")

if re.match(pattern, "grey"):
    print("Match 2")
    
if re.match(pattern, "gris"):
    print("Match 3")
    