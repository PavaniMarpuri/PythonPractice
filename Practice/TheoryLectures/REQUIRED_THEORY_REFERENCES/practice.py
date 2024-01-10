
# int and float practice

# first_value = float(input("enter first value "))
# second_value = float(input("enter the second value "))
# elements_sum = first_value + second_value
# print("sum of two elements "+str(elements_sum))

        # String practice

course = 'python for beginners'
        # 01234567891011..
print(course.find('b'))                         # 11 returns the first index of the letter or the word
print(course.upper())  # PYTHON FOR BEGINNERS
print(course.lower())  # python for beginners
print(course.replace('for' ,'4'))  # python 4 beginners
print('python' in course)                       # returns boolean values stating the word is present or not
print(course.capitalize())  # Python for beginners

# f-Strings

'''

When working with strings,we are able to put variables into our strings with the format method. 
To do this, we use curly braces { } as placeholders for our values.
Then, after the string, we put.format(variable_name). 
When the code runs, the curly braces will be replaced by the value in the variable specified in the brackets after the format method.

'''

num_days = 28
pay_per_day = 50
print(f"I worked {num_days} days this month. I earned ${pay_per_day} per day.")

print("You worked {1} this month and earned ${0} per day".format(num_days ,pay_per_day))
print("You worked {} this month and earned ${} per day".format(num_days ,pay_per_day))

file_path = "sub-folder\list_of_cats.txt"
# open a file in the path in read "r"  mode  and storing data in a variable file_data_variable
with open(file_path, "r") as file_data_variable:
    content = file_data_variable.readlines()
    print(content)

for x in content:
    # print values by removing new lines and ','
    print(x.strip("\n").strip(", "))

print("*************************")