
"""
How do we use '*args' and '**kwargs'	- Not reserved words. Can use any name, but this is a convention
"""
# Args allow us to provide a function a variable amount of
# NON-KEYWORD arguments. We use * before the parameter name('args' is conventional).
# *args = variable arguments, ie. name, company, etc
# **kwargs = variable keyword arguments, ie. name="John", company="Company Y"
def triple(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

triple(1, 2, 3)
triple(9, 21, 40, 46)


# -- Example 2
def calculate_area(shape, *args):
    if shape == "circle":
        radius = args[0]
        return 3.14 * (radius ** 2)
    elif shape == "rectangle":
        length, width = args
        return length * width
    else:
        return "Unsupported shape" # Here the return type is inconsistent

# For Example - Duplicate code:
circle_area = calculate_area("circle", 5)
print(f"The area of the circle is: {circle_area}")

rectangle_area = calculate_area("rectangle", 5, 4)
print(f"The area of the rectangle is: {rectangle_area}")

# ---- The better way to do this would be as follows:
def calculate_area(shape, *args):
    if shape == "circle":
        radius = args[0]
        return 3.14 * (radius ** 2)
    elif shape == "rectangle":
        length, width = args
        return length * width
    else:
        raise ValueError("Unsupported shape")

# Now we'll raise an error if the types are unsupported instead:
try:
    triangle_area = calculate_area("triangle", 2, 4, 6)
except ValueError as e:
    print(f"Error: {e}")


# ******************* using both *args and **kwargs *********************************

def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

"""
The order to pass multiple arguments for a function is :- func( arg1,arg2,*args,**kwargs)
ex:- my_fun(1,2, x,y,z, name="a",age=20,place="abc")
 here *args -> x,y,z
    **kwargs -> name="a",age=20,place="abc"
"""