# Example 1

# first_value = 10
# second_value = int("SergeCat")

# answer_var = first_value + second_value


# print(answer_var)

# Example 2

file_path = "sub-folder\list_of_cats.txt"

# open a file in the path in read "r"  mode  and storing data in a variable file_data_variable
with open(file_path, "r") as file_data_variable:
    content = file_data_variable.readlines()
    print(content)

for x in content:
    # print values by removing new lines and ','
    print(x.strip("\n").strip(", "))

print("*************************")

# for x in content:
#     print(x.strip(", "))


# file_content = open("list_of_cats.txt", "r")
# # logic - reading, writing or updating
# file_content.close()
