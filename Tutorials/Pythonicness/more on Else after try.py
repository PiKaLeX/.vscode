# The else statement can also be used with try/except statements.
# In this case, the code within it is only executed if no error occurs in the try statement.

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

    
try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)