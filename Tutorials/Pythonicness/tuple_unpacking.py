numbers = (1, 2, 3)

# Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.
a, b, c = numbers

print(a)
print(b)
print(c)

# This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side forms the tuple (b, a) which is then unpacked.
a, b, c = b, c, a

print(a)
print(b)
print(c)

# A variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(d)