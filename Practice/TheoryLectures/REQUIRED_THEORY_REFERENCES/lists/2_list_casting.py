
""" -- Create lists with casting """

# Data types that we can cast to a list
my_string = "Hello"
my_list = list(my_string)
print(my_list)

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)

my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_from_keys = list(my_dictionary.keys())
print(list_from_keys)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_from_values = list(my_dictionary.values())
print(list_from_values)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_from_items = list(my_dictionary.items())
print(list_from_items)
