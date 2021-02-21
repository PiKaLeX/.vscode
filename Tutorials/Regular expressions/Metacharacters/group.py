import re
# Group = ce qui est entre paranthèse

# The content of groups in a match can be accessed using the group function.
# A call of group(0) or group() returns the whole match.
# A call of group(n), where n is greater than 0, returns the nth group from the left.
# The method groups() returns all groups up from 1.

pattern = r"a(bc)(de)(f(g)h)i"

Match = re.match(pattern, "abcdefghijklmnop")

if Match:
    print(Match.group())
    print(Match.group(0))
    print(Match.group(1))
    print(Match.group(2))
    print(Match.groups())
