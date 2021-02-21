import re

# Some more metacharacters are * + ? { and }.
# These specify numbers of repetitions.
# The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions".

# The example matches strings that start with "egg" and follow with zero or more "spam"s
pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")

if re.match(pattern, "gggggggggggggg"):
    print("Match 2")
    
if re.match(pattern, "abc"):
    print("Match 3")