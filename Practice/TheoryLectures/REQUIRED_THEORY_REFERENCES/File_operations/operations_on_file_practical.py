# File Reading

                            # traditional way
                            # read()

cat_names_object = open("list_of_cats.txt", 'r')
print(f"cat_names_object {cat_names_object}")  # prints the object

cat_names_read = cat_names_object.read()
print(f"cat_name_read {cat_names_read}")  # prints cat names

"""
cat_names_object = open("REQUIRED_THEORY_REFERENCES/cats_names.txt", 'r')
above line will cause exception , bcz the path is different we need to mention complete path
if the same file is there in the subfolder of "File_operations" folder then it will work with above line

"""

cat_names_object1 = open(r"subfolder_test\cats_names.txt", 'r')
print(f"cat_names_object {cat_names_object1.read()}")  # prints cat names

                            # readline()
"""
cat_names_readline = cat_names_object1.readline()
print(f"cat_names_readline {cat_names_readline}")  

=> above line prints empty line bcz in line 17 we already red the data from file.
 so the control is at the end of the line, if we want to read it again it will continue read from there .
 
"""

cat_names_object2 = open("list_of_cats.txt", 'r')
cat_names_readline = cat_names_object2.readline()

print(f"cat_names_readline {cat_names_readline}")  # prints the first name

                            # readlines()

cat_names_object3 = open("list_of_cats.txt", 'r')
cat_names_readlines = cat_names_object3.readlines()

print(f"cat_names_readlines {cat_names_readlines}")

"""
if we leave it as it is .. data/resource leakage will happen . so we need to close the objects
"""

cat_names_object.close()
cat_names_object1.close()
cat_names_object2.close()
cat_names_object3.close()

                        # BEST PRACTICE APPROACH

with open("list_of_cats.txt", 'r') as cat_names_object:

    cat_names_read = cat_names_object.read()
    print(f"with cat_name_read {cat_names_read}")  # prints cat names

    cat_names_object.seek(0)  # will make the reading from the 0 i.e first line of the file

    cat_names_read = cat_names_object.readline()
    print(f"with cat_name_readline {cat_names_read}")  # prints first cat name

    cat_names_read = cat_names_object.readlines()
    print(f"with cat_name_readlines {cat_names_read}")  # prints all the cat names

"""
using for loop we can iterate over file without use of read methods
"""

with open("list_of_cats.txt", 'r') as file:
    for line in file:
        print(f"iteration file using for loop {line}")

                    # Exceptional Handling

try:
    with open("random_names.txt", 'r') as file:
        for line in file:
            print(f"iteration file using for loop {line}")
except FileNotFoundError:
    print(" File not Found ")
except IOError as e:
    print(f"Error reading the file : {e}")

                    # exceptional handling with traditional way

random_names_object = open("random_names.txt", 'r')

try:

    read_object = random_names_object.read()
    print(f"Random names:- \n{read_object}")
except FileNotFoundError:
    print(" File not found ")
finally:
    random_names_object.close()

