# Can we show an error message if 
# there is a white space line in the text file?
# it will disply empty line if the file dont hv data
with open("secret_secret_secret_pokemon.txt", 'r') as file:
    content = file.readlines()

    print(content)


