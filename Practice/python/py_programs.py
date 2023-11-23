# import random
#
# print(random.randrange(1, 100))

# **2. Write a program to reverse a string without using any inbuilt functions.**
# s = "Hello what's your name?"
# reverse_ = ""
# for char in s:
#     reverse_ = char + reverse_
# print(reverse_)

# **3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**
# new_ = ""
# my_str = "Welcome to India"
# old_word = "India"
# new_word = "Sri Lanka"
#
# for word in my_str.split():
#     if old_word == word:
#         new_ += new_word + " "
#     else:
#         new_ += word + " "
# print(new_)

# **4. How to convert a string to a list and vice-versa.**
# s = " hi hello welcome to python programming"


# def convert(string):
#     list_ = string.split()
#     print(list_)
#     neww_ = ""
#     for word in string:
#         neww_ += word
#     print(neww_)
#
#
# convert(s)


# def conv_(string):
#     list_ = string.split()
#     print(list_)
#     newww_ = " ".join(list_)
#     print(newww_)
#
#
# conv_(s)

# **5. Convert the string "Hello welcome to Python" to a comma separated string.**

# listt_ = list(s)
# new = ",".join(listt_)
# print(new)

# l_ = s.split()
# ",".join(l_)
#
# # **6. Write a program to print alternate characters in a string.**
#
# for index, char in enumerate(s):
#     if index % 2 == 0:
#         print(char, end=" ")
#
# s[::2]


# **7. Write a Program to print ascii values of the characters present in a string.**

# def ascii_(letter):
#     return ord(letter)
#
#
# ascii_("h")


# **8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**

# def conv_upper_to_lower(letter):
#     if ord("A") <= ord(letter) <= ord("Z"):
#         print(chr(ord(letter) + 32))
#
#
# def conv_lower_to_upper(letter):
#     if ord("a") <= ord(letter) <= ord("z"):
#         char = print(chr(ord(letter) - 32))
#         print(char)
#
#
# conv_upper_to_lower("R")
# conv_lower_to_upper("p")


# def convert_upper_to_lower(letter):
#     if ord("A") <= ord(letter) <= ord("Z"):
#         print(chr(ord(letter) + 32))
#     else:
#         return letter
#
#
# def convert_lower_to_upper(letter):
#     if ord("a") <= ord(letter) <= ord("z"):
#         return chr(ord(letter) - 32)
#     else:
#         return letter
#
#
# # Test the functions
# input_char = "r"
# output_char1 = convert_lower_to_upper(input_char)
# print(output_char1)
#
# input_char = "P"
# output_char2 = convert_upper_to_lower(input_char)
# print(output_char2)

# **9. Write a program to swap two numbers without using the 3rd variable.**

# x = 17
# y = 21
#
# print(f"Before swapping x={x}, y={y}")
# x, y = y, x
# print(f"After swapping x={x}, y={y}")
#
# # **10. Write a program to merge two different lists.**
#
# l1 = [1, 23, 89, 345, 0]
# l2 = [63, 98, 83628, -90, 523]
#
# merge_ = l1 + l2
# print(merge_)
# # OR
# l1.extend(l2)
# print(l1)

# **11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**

# n = 4
# with open("demo.txt") as file:
#     for line_no, line in enumerate(file, start=1):
#         if line.strip():
#             if line_no == n:
#                 print(line_no, line)

# OR

# from itertools import islice
#
# n = 7
# with open("demo.txt") as fh:
#     lines = list(islice(fh, n - 1, n))
# print(*lines)

# **12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**

# from itertools import islice
#
# with open("demo.txt") as file:
#     lines = islice(file, 3, 7)
#     print(list(lines))

# **13 Program to print the last "N" lines of a file.**

# from itertools import islice
#
# with open("demo.txt") as fh:
#     count = 0
#     for line in fh:
#         count += 1
#     fh.seek(0)
#     lines = islice(fh, 3, count)
#     print(list(lines))

# OR

# from collections import deque
# with open("demo.txt") as file:
#     n = 3
#     lines = list(deque(file, n))
#     for line in lines:
#         print(line, end="")

# **14. Write a program to check if the given string is Palindrome or not without using reversed method.**
# def palindrome_string(string):
#     _reverse = ""
#     for char in string.lower():
#         _reverse = char + _reverse
#     if string == _reverse:
#         print(f"'{string}' is a Palindrome")
#     else:
#         print(f"'{string}' is not a Palindrome")
#
#
# my_string1 = "malayalam"
# my_string2 = "nibhun"
#
# palindrome_string(my_string1)
# palindrome_string(my_string2)

# **14. Write a program to check if the given string is Palindrome or not without using reversed method.**

# ps = ["madam", "hello", "bye", "malayalam", "laptop"]
#
# result = list(map(lambda item: f"{item} is Palindrome " if item == item[::-1] else f"{item} is not palindrome", ps))
# print(result)


# **15 Write a program to search for a character in a given string and return the corresponding index. or
# write a program to linear search

def search_character(char_to_find, input_string):
    for index, char in enumerate(input_string):
        if char == char_to_find:
            return index
    return -1

input_string = "Programming language"
char_to_find = "r"

index = search_character(char_to_find, input_string)

if index != -1:
    print(f"'{char_to_find}' found at index {index}")
else:
    print(f"'{char_to_find}' not found in the string")

