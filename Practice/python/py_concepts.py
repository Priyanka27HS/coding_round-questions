# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.
# If you have a JSON string, you can parse it by using the json.loads() method.
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# You can convert Python objects of the following types, into JSON strings:
#
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

import json

# JSON string
json_str = '{"name": "Ram", "age": "29", "city": "Madurai"}'

# Deserialize JSON to a Python dictionary
data = json.loads(json_str)

# Serialize Python dictionary to JSON
json_data = json.dumps(data)

print(data)
print(json_data)

# TRY EXCEPT BLOCK

try:
    num1 = int(input("Enter a number 1:"))
    num2 = int(input("Enter a number 2:"))
    result = num1 / num2
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")

# Now, let's explain each of the four concepts in the context of this program:
#
# try:
#
# In the try block, we attempt to read two integers from the user as the numerator and denominator.
# It's the main code section where exceptions may occur if the user enters invalid input or tries to divide by zero.
# except:
#
# We have two except blocks: one for ValueError and another for ZeroDivisionError. If the user enters non-integer
# input or attempts to divide by zero, these exceptions will be caught in the respective except blocks. else:
#
# The else block is executed if no exceptions are raised in the try block.
# In this case, it prints the result of the division.
# finally:
#
# The finally block is executed regardless of whether an exception occurred or not. It's used to ensure that some
# final actions, in this case, printing "Execution completed," take place, whether an exception occurred or not.
# Here's how the program works:
#
# If the user enters non-integer values for num1 or num2, the ValueError exception is raised, and the first except
# block is executed, printing "Invalid input." If the user enters 0 as num2, the ZeroDivisionError exception is
# raised, and the second except block is executed, printing "Cannot divide by zero." If valid integer values are
# entered and no exceptions occur, the else block is executed, printing the result of the division. Finally,
# regardless of the outcome, the finally block is executed, printing "Execution completed." This program demonstrates
# how the try, except, else, and finally blocks work together to handle exceptions and ensure code execution and
# cleanup as needed.


# FIle handling

# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# The key function for working with files in Python is the open() function.
#
# The open() function takes two parameters; filename, and mode.
#
# There are four different methods (modes) for opening a file:
#
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists
#
# In addition you can specify if the file should be handled as binary or text mode
#
# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)

# f = open("demo.txt", "r")
# print(f.read())
#
# f1 = open("demo.txt", "w")
# # print(f1.write())
# f1.write("Welcome")
#
# f2 = open("demo.txt", "a")
# f2.write("Welcome to India")

with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

# f1.close()

