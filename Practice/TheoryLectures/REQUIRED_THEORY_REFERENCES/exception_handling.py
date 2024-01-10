# =========   A try-except block is used to catch and handle exceptions in Python.
try:
    # Code that might raise an exception
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    result = numerator / denominator

    # This block will be skipped if an exception occurs
    print("Result:", result)

except ValueError as ve:
    # Handle the case where the user enters a non-integer
    print(f"Error: {ve}. Please enter valid integers.")

except ZeroDivisionError:
    # Handle the case where the user tries to divide by zero
    print("Error: Division by zero is not allowed.")

except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")

else:
    # This block will be executed if no exception occurs
    print("No exceptions were raised.")

finally:
    # This block will be executed whether an exception occurred or not
    print("This block always executes, providing cleanup or finalization.")

# ======================= raise is used to raise the exceptions ====================

# raise example
num1 = 10
num2 = 0

if num2 == 0:
    raise ZeroDivisionError("Cannot divide by zero")