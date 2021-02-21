import re

pattern = r"spam"

if re.match(pattern, "spam" * 3):
    print("Match")
else:
    print("No Match")