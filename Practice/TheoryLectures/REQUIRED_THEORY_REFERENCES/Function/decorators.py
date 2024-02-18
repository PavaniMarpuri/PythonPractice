"""
Function Decorators:

Implementing some logic before calling the actual function.

"""


# -- Example 1 - Decorate a cake
def decorate_it(func):
    # Define the inner function
    def decoration():
        # Add some functionality to decorate the other function with
        print("I've been decorated!!!")

        # call original function(Remember this will be provided as an argument)
        func()

    # return the inner function
    return decoration


# Define normal function - Decorate the cake with a cherry on top
@decorate_it
def carrot_cake():
    print("I am a carrot cake!")


# Decorate the normal function
print(carrot_cake())

"""
like num = num + 1, now carrot_cake = decorate_it(carrot_cake)
We use the original carrot_cake function and decorate_it and now
we update the carrot_cake function with the updated version.

This will be the same as decorated_carrot_cake = decorate_it(carrot_cake)
and now we print or call the decorated_carrot_cake function with
decorated_carrot_cake()
"""


# -- Example 2
def my_decorator(func):  # func is paramater that receives the function name
    def wrapper():  # wrapper can be any name
        print("It is time to celebrate.")
        func()
        print("Here comes the sparkles.")

    return wrapper


@my_decorator  # Same as say_hello_with_sparkles = my_decorator(say_hello)
def say_hello():
    print("Hello!")


@my_decorator  # Same as say_cheers_while_smiling = my_decorator(say_cheers)
def say_cheers():
    print("Cheers!")


# Using the decorated function
say_hello()
"""
You can also remove @my_decorator above function and the say_hello() and
replace with below by placing it after the function
"""
# say_hello_with_sparkles = my_decorator(say_hello)
# say_hello_with_sparkles()
print()

say_cheers()
"""
You can also remove @my_decorator above function and the say_cheers() and
replace with below by placing it after the function
"""
# say_cheers_while_smiling = my_decorator(say_cheers)
# say_cheers_while_smiling()


"""Function Decorators"""


def positives_only(func):
    def wrapper(values): # here the values will have the values that we are
        # passing to average function from line 94( function calling)
        # if the function has two arguments the wrapper also should have two arguments
        values = [i for i in values if i >= 0]
        return func(values)

    return wrapper


@positives_only
def average(numbers):
    return sum(numbers) / len(numbers)

# print(average([-1,-5,-2,-6,1,5,3,2]))
