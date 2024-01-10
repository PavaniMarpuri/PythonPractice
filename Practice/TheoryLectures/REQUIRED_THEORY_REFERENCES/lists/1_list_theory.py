# ========================== Creating a list ================
new_list = []
word_list = ["word1", "word2", "word3"]

"""---- Operations on list --- """

# obtaining a value from list
my_pokemon = ["squirtle", "metapod", "pikachu", "charizard", "gengar"]

print(f"I choose you {my_pokemon[2]}")

# adding items to the list (will append at the end position)
my_pokemon.append("gastly")
print(my_pokemon)

# inserting items to specific position in list
my_pokemon.insert(3, "charmander")
print(my_pokemon)

# taking one item from list 1 to list 2
current_poke_hand = [my_pokemon[2], my_pokemon[5]]
print(f"Current pokemon: {current_poke_hand}")

current_poke_hand.insert(1, my_pokemon[3])
print(f"Current pokemon: {current_poke_hand}")

# default will remove last item
current_poke_hand.pop()
print(f"Current pokemon: {current_poke_hand}")

# remove specific item at index
current_poke_hand.pop(0)
print(f"Current pokemon: {current_poke_hand}")

"""  ============= List Comprehension example ================== """

numbers = [2, 4, 6, 8, 10]
square_values = [x ** 2 for x in numbers]
print(f"square_values {square_values}")


""" -- Creating lists with the range ---- """

# Normally we will have
for even_num in range(2, 11, 2):
    print(even_num)

# Another option to above
my_range = list(range(2, 11, 2))
print(my_range)

for even_num in my_range:
    print(even_num)


""" -- Setting a list to another list - BE WARNED (This can create a logic error)--- """

num_list = [1, 2, 3, 4, 5]
new_num_list = num_list

new_num_list[2] = 200

num_list_sum = sum(num_list)  # Answer is 212 which is not what we expected
print(f"-- The sum of the items in num_list is {num_list_sum}.")

print(num_list)  # The 3rd value in num_list will also change to 200

# -------------  To prevent the above use the copy method

num_list = [1, 2, 3, 4, 5]
new_num_list = num_list.copy()

new_num_list[2] = 200

num_list_sum = sum(num_list)  # This answer is 15 which is what we are looking for.
print(f"-- The sum of the items in num_list is {num_list_sum}.")

print(num_list)


"""  -- Dealing with boolean lists --- """

bool_list = [False, True, True, False]
bool_list = [0, 1, 1, 0]

my_bool = bool(bool_list[0])
my_bool = bool(0)  # my_bool = False

if my_bool == False:
    pass

if my_bool:  # Conditions always test for True or False (Here: if True)
    pass

if not my_bool:  # (Here: if not True)
    pass

bool_list = [False, True, True, False, "Word1"]
for item in bool_list:
    if item:  # If True
        print("The value is True")
    elif not item:  # If False
        print("The value is False")
    else:
        print("The value is not a boolean")

student_number = [1, 2, 3, 4]
pass_result = [False, True, True, False]
for student in range(len(student_number)):
    if pass_result[student]:  # If True
        print(f"Student {student_number[student]} : passed")
    elif not pass_result[student]:  # If False
        print(f"Student {student_number[student]} : failed")
    else:
        print(f"Student {student_number[student]} : result unknown")

