# Python allows to have function with varying number of arguments.
# Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function.

def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

# **kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
# The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.
# The arguments returned by **kwargs are not included in *args.

def function2(x, y=7, *args, **kwargs):
    print(f'(x, y) = ({x}, {y})')   
    print(args)  
    print(kwargs)

function2(2, 3, 4, 5, 6, 7, a=8, b=9)