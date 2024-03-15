# Program to take username as input and print Hello message
name = " "
# validation to check if the username is null or is not alphabetic string
while name == " " or not name.isalpha():
    # Asking user to enter name
    name = input("Please enter your name ")
# Printing Hello message to user
print(f"Hello {name}!")
