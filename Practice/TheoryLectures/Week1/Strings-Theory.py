""" This is a C6 Open Session Demonstration """

# ======================== String Literals =========================

# -- Single quotes --
# single_quote = 'A'

# -- Double quotes --
# double_quote = "The quick brown fox jumps over the lazy dog"

# -- Quotes in quotes --
quote_in_quote = "Join said 'I love this session.'"
print(quote_in_quote)

# -- Triple quotes (Multi-line) --
multi_line_string = """This is a
multi-line
string."""

print(multi_line_string)
print()

# ======================== Escape Characters =========================

# -- Only one set of double quotes used here
multi_line_esc_string = "This is a\nmulti-line\nstring."
print(multi_line_esc_string)
print()

# ======================== Concatenation =========================

# Assigning a string to a variable
name = "Miles"
surname = "Morales"

# using , in print will include space

print("using , in print to print name :- " + name, surname)

# -- Assigning the result of two concatenated strings
# -- to a variable called 'full_name'
full_name = name + surname
print(full_name)

full_name = name + " " + surname
print(full_name)

# ======================== Formatted Strings =========================

# -- f-strings
show_friend = f"My friend {name} has the {surname} surname."
show_friend = f"{name} {surname}"

print(show_friend)

# -- .format
name = "Miles"
age = 30

greeting = "Hello, my name is {} and I am {} years old.".format(name, age)
print(greeting)

# -- Change variable order
greeting = "Hello, my name is {1} and I am {0} years old.".format(name, age)
print(greeting)

# ======================== Raw Strings =========================

print()
raw_string = r"This is a\nraw\nstring."
print(raw_string)
print()

multi_line_esc_string = "This is a\nmulti-line\nstring."
print(multi_line_esc_string)
print()

# ===== Printing a user-friendly output to the terminal =====

print("========= Introducing my friend ========\n")
full_name = "Riaan Deventer"
print(f"My name is {full_name}")
print(f"My friend's name is {name} {surname}")
print('=' * 50)

# String Strip function

new_string = "======Hel====lo====="
print(new_string.strip("="))

# String can be printed on index basic both in forward and backward directions

new_string = "Hello"
print(new_string[0])
print("0:3 " + new_string[0:3])  # It will start at index 1, and end at index 3 (which is not included).
print(new_string[0:])
print(new_string[-1])
print(new_string[0::2])  # indicates print evry second letter after printing one letter
print(new_string[::-1])  # reverse a string

""" 
Extended slice :- the syntax foe extended slice is [start(incl):end(excl):step(forw/rev)]

"""

greeting = "Hello"
print(greeting[1::2])  # o/p :- el ( start from index '1' and till end. print evry second letter )
print(greeting[4:1:-1])  # o/p :- oll ( start from index '4' and till index '1' note here the index 1 is not include.
# step is -1 indicates reverse order )
print("forward "+greeting[0:4:1])  # o/p :- Hell ( start from index '0' and till index '4' note here the index 4 is not include.
# step is 1 indicates forward order )
print("forward "+greeting[4:0:1])  # wont print anything
print("Hello " + greeting[::])
print("forward "+greeting[0:4:2]) # Hl print evry 2nd letter after printing one letter
print("reverse "+greeting[4:0:-2]) #ol print evry 2nd letter after printing one letter
"""
Some useful escape sequences are listed below:
\n - Newline - this will insert the equivalent of pressing enter to take the
insertion point for output to the next line
\t - Tab - inserts a tab
\s - Space - inserts a space

"""
