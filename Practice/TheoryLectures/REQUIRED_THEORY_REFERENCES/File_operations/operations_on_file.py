"""

=> To open a file :-
                    open(file_path, mode)

-> file_path can be relative path (just file name is enough if text file and code file are in same directory)
    and absolute path(full path of the file)
-> generally it is recommended to use relative path
-> mode can be
            r -- read mode
            w -- write mode
            a -- append
            + -- read & write
=> File Methods for Reading :-

            read() -- it reads the whole content of the specified file if no argument specifies
                        if argument specified as n, it reads the n bytes from the file in the form of string
            readline() -- it reads the first single line/first column(in case of csv), if argument specified,
                        then reads n number of bytes and returned as string but not exceed a single line.
            readlines() -- it reads all the lines from file and returns in the form of list

=> flow  :-
                open() -> read/write -> close()
"""

# traditional way of dealing with file
"""
file_object = open("cats.txt", 'r')
# process file logic
file_object.close()

"""
# context manager
"""
-> In this way, we will open and load the file data & will store it in an object
-> And also we no need to explicitly close the file. it will be taken care of context manager

            with open("cats.txt", 'r') as file_object:
                process your logic
"""

