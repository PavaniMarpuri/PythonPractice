name = " "
while name == " " or not name.isalpha():
    name = input("Please enter your name ")
print(f"Hello {name}!")