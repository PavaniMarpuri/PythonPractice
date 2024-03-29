"""
=> PIP - it is a Python Package Installer( means it well useful when we want to install/uninstall external packages
 like pandas)
 example :- pip install tabulate
=> pandas - it will be used for large amount of data from files like excel files , csv files etc...

"""

"""
=> import math :- Will import the math module. 
                  Any functions that you use would have to be used as math.sqrt, math.ceil, etc.
=> from math import * :- Will import all functions from math to the namespace of your current file. 
                         Any functions that you use can be used as sqrt, ceil, etc.
=> from math import ceil :- Will import particular module oly.

"""

"""

division :- "/" gives float/ decimal output
            "//" gives integer output
            
"""

"""
Self represents the instance of the class. 
By using the “self” we can access the attributes and methods of the class in Python. 
It binds the attributes with the given arguments. 
The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes
"""

"""
for _ in range(20)

 Basically it means you are not interested in how many times the loop is run till now 
 Just that it should run some specific number of times overall.
"""

"""

differences between docstrings(""" """ ) and single comments (# ) :-

=> Docstrings explain what a function/class is needed for 
(i.e., its description, arguments, and output — and any other useful information) 
=> While comments explain what specific code strings do. 
=> In other words, code comments are for people who want to modify the code, 
and docstrings are for people who want to use the code

"""

"""
word_list = ["word1", "word2", "word3"]
my_pokemon = ["squirtle", "metapod", "pikachu", "charizard", "gengar"]

# adding two lists
list_3 = word_list + my_pokemon

"""

"""
=> method overloading:- 

In Python, compile-time polymorphism is primarily achieved through function overloading, 
although Python does not support true function overloading.
However, you can define functions with the same name in Python, 
but only the latest defined function will be considered.
"""

"""
-> python supports multiple inheritance, it is developer responsibility to use inherited classes methods wisely 
and making sure both the inherited classes should not have same named methods

class Vehicle:
    pass
class Electric:
    pass
class HybridCar(Vehicle, Electric):
    pass
"""

"""
=> Destructor :- It is a special method that gets called when an object is about to be destroyed.
It is used to perform clean up actions. (opposite to constructor)

def __del__(self):
    print(f"{self.name} {self.age} {etc} {etc} destroyed")
"""