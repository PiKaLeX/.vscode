import re

# Some more metacharacters are * + ? { and }.
# These specify numbers of repetitions.
# The metacharacter ? means "zero or one repetitions".

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")

if re.match(pattern, "icecream"):
    print("Match 2")
    
if re.match(pattern, "sausages"):
    print("Match 3")
    
if re.match(pattern, "ice--cream"):
    print("Match 4")