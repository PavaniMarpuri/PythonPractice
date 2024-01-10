# -- Dealing with mixed lists
mixed_list = ["Hello", 13, 87.89, True, None, (), [1, 2, 3, ['a', 'b', 'c']], {}]
my_item = mixed_list[6][3][1]  # Access the 'b'

"""=================== List dimensions ========================="""

# 1-dimensional list

list_1d = [1, 2, 3, 4, 5]
my_1d_item = list_1d[1]  # refer to 2
print(f"my_1d_item {my_1d_item}")

# -- Creating a 2-dimensional list

list_2d = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

my_2d_item = list_2d[1][1]  # refer to 5
print(f"my_2d_item {my_2d_item}")

# -- Creating a 3-dimensional list

list_3d = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
           [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
           [[21, 22, 23], [24, 25, 26], [27, 28, 29]]]

my_3d_item = list_3d[2][1][1]  # Refer to value 25
print(f"my_3d_item {my_3d_item}")

# iterate a 2-dimensional list using for loop

matrix_list = [[1, 2, 3], ["Darth Maul", "Darth Vader", "Darth Sidius"]]
print(f"My favorite person is at position: {matrix_list[0][0]} and they are {matrix_list[1][0]}")

for i in matrix_list:
    print(i)  # which will print iterate matrix_list and print the values
    for j in i:
        print(j)  # which will iterate i and print the values
