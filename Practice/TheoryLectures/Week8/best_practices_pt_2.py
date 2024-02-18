
"""
Type Annotations :
"""
def add_numbers(a: int, b:int) -> int:  # return value must be int
    return a + b

# If you want to indicate types like List and Dict
from typing import List, Dict

def process_data(data: List[str]) -> None:
    # Code to process the data
    data.sort()

# Annotations will not give compile or runtime errors, but helps with documentation	
# and some error checking tool extention might point out errors

"""
Return types
"""
# -- Example 1
def find_item(item, item_list):
    if item in item_list:
        return True
    else:
        return "Item not in list"
    
# Above example can return a boolean or a string
    
# --- The better option
def find_item(item, item_list):
    return item in item_list

# Above example will always return the type of item


"""
Building Custom decorators: 
"""
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        # *args = variable arguments, ie. name, company, etc
        # **kwargs = variable keyword arguments, ie. name="John", company="Company Y"
        start_time = time.time()
        result = func(*args, **kwargs)
        """ 
        result above is a new variable and will take on the type of whatever
        the function returns.
        Wrapper then calls the original function (function name in variable func) 
		with any provided arguments and keyword arguments.
        """
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

# -- decorator implimentation
@time_decorator
def slow_function():
    # some time-consuming task
    time.sleep(6)	# waits 6 seconds

# Using the decorated function
slow_function()

# --- Alternative to above decorator implimentation
def slow_function():
    # some time-consuming task
    time.sleep(6)	# waits 6 seconds

# declare new decorated function
function_duration = time_decorator(slow_function)
# Using the decorated function
function_duration()

# ---- The end: Enjoy the carrot_cake
