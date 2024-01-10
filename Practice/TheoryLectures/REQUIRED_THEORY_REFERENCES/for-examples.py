"""FOR LOOPS"""

# Example 1: Range function, will loop over a sequence of numbers
for num in range(0, 3):
    print(num)
    num = 66
    print(num)

# Example 2: Iterate over a list of items or stuff
list_wizards = ["Dumbledore", "Gandalf", "Saruman", "Palpatine", "Merlin", "Radagast"]
for wizard in list_wizards:
    print(f"{wizard} is a wizard!")

# Example 3: Calculate sum of value using range()
total = 0

for number in range(1, 6):
    print(f"The current value of number is: {number}")
    print(f"The current total is: {total}")
    total += number
print(f"Sum: {total}")

"""
ENUMERATE IS USED TO KEEP TRACK OF NUMBER OF ITERATIONS IN THE LOOP (it is a simply a iteration function )
Enumerate() will keep track of the records in the list or anything along with position/count details
"""
# Example 4: Enumerate()
pokemons = ["metapod", "pikachu", "charmeleon",
            "charizard", "charmander", "serge",
            "snorlax", "wartotle", "magikarp"]
# index = 0

# for poke in pokemons:
#     print(index, poke)
#     index += 1

# Enumerate()
"""
enumerate(obj, start_postion) 
 start_postion :- will start the positioning of data from start_postion( it wont change the actual collection position)
enumerate(obj) :- The dafault start_postion is "0".
"""
total = 0
for pos, poke in enumerate(pokemons, 1):
    print(pos, poke)
    total += 1

print(pos)
"""
# Count: The count of the current iteration
# Poke: The value of the item at current iteration
 Here the first param will hold the position and the second param will hold the value . name does not matter.
 
"""


# Example 5: Break

# print(pokemons[1])
for pos, poke in enumerate(pokemons, 1):
    if poke == "pikachu":
        print(f"Pikachu is in position {pos}!")
        break

# Example 6: Continue

# print(pokemons[1])

for pos, poke in enumerate(pokemons, 1):
    if poke in ["charmeleon", "charizard", "charmander"]:
        print(f"{poke} You are fire type!")
    else:
        print(f"{poke} you are different type!")

# If we mention single temp variable in case of enumerate,
# Then the tem variable will store both cont and value in it as below

for poke in enumerate(pokemons):
    print(f"{poke}")

"""
pass :- The pass statement is used as a placeholder for future code. 
When the pass statement is executed, nothing happens,
but you avoid getting an error when empty code is not allowed. 
Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

continue :- continue will break the current iteration and jumps to next iteration

break :- break will come out of the loop either for or while what ever. 
Incase of nested loops,break will break the immediate loop alone not all the loops.

"""