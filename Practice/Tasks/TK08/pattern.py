import math
number_of_rows = int(input("Please enter number of rows for the * pattern "))
middle_row_count = math.ceil(number_of_rows / 2)
decrement_count = 2
for n in range(1, number_of_rows + 1):
    if n <= middle_row_count:
        print(f"{n * "*"}")
    else:
        print(f"{(n - decrement_count) * "*"}")
        decrement_count += 2
