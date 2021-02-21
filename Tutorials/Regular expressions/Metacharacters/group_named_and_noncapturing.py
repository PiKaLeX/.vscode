import re
# Group = ce qui est entre paranthèse

# There are several kinds of special groups.
# Two useful ones are named groups and non-capturing groups.
# Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
# Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.

pattern = r"(?P<first>abc)(?:def)(ghi)"

Match = re.match(pattern, "abcdefghijklmnop")

if Match:
    print(Match.group("first"))
    print(Match.groups())
