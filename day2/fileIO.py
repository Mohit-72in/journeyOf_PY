"""
FILE I/O IN PYTHON
------------------

Definition:
File I/O (Input/Output) in Python is the process of reading data from
and writing data to files stored on a disk.

Python provides the built-in open() function to perform file operations.

Syntax:
    file_object = open("filename", "mode")
"""

# -------------------------------------------------
# FILE MODES EXPLANATION
# -------------------------------------------------
"""
'r'  -> Read mode (default)
       Opens file for reading.
       Error if file does not exist.

'w'  -> Write mode
       Creates a new file or overwrites an existing file.

'a'  -> Append mode
       Writes data at the end of the file.

'r+' -> Read and Write
       File must exist.

'w+' -> Write and Read
       Overwrites file if it exists.

'a+' -> Append and Read
       Writes at the end, reading allowed.

'b'  -> Binary mode (used with other modes)
"""

# -------------------------------------------------
# 1. WRITE MODE ('w')
# -------------------------------------------------
# Creates a file or overwrites existing file
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This file demonstrates File I/O in Python.\n")
file.close()

# -------------------------------------------------
# 2. READ MODE ('r')
# -------------------------------------------------
# Reads the entire content of the file
file = open("example.txt", "r")
content = file.read()
print("Read Mode Output:")
print(content)
file.close()

# -------------------------------------------------
# 3. READLINE METHOD
# -------------------------------------------------
file = open("example.txt", "r")
print("Readline Output:")
print(file.readline())  # reads first line
print(file.readline())  # reads second line
file.close()

# -------------------------------------------------
# 4. READLINES METHOD
# -------------------------------------------------
file = open("example.txt", "r")
lines = file.readlines()
print("Readlines Output:")
print(lines)
file.close()

# -------------------------------------------------
# 5. APPEND MODE ('a')
# -------------------------------------------------
# Adds content at the end of the file
file = open("example.txt", "a")
file.write("This line is appended.\n")
file.close()

# -------------------------------------------------
# 6. READ + WRITE MODE ('r+')
# -------------------------------------------------
file = open("example.txt", "r+")
print("r+ Mode Output:")
print(file.read())
file.write("Added using r+ mode.\n")
file.close()

# -------------------------------------------------
# 7. WITH STATEMENT (BEST PRACTICE)
# -------------------------------------------------
"""
The 'with' statement automatically closes the file
even if an exception occurs.
"""
with open("example.txt", "r") as file:
    print("Using with statement:")
    print(file.read())

# -------------------------------------------------
# 8. APPEND + READ MODE ('a+')
# -------------------------------------------------
file = open("example.txt", "a+")
file.write("Final appended line.\n")
file.seek(0)  # move pointer to beginning
print("a+ Mode Output:")
print(file.read())
file.close()

# -------------------------------------------------
# END OF PROGRAM
# -------------------------------------------------

#ddelete a file // uncomment the below lines to use
# import os   #operating system module
# os.remove("example.txt")
