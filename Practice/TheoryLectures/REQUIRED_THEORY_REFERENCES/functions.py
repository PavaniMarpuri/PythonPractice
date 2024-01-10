def function_call():
    return last_function()


def last_function():
    return another_function()


def another_function():
    return 3 * 12


result = function_call()

print(result)
