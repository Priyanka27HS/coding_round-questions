# # 1. Print boundary elements of a 2d array.
# # 3 , 2, 1
# # 4, 5, 6
# # 7, 8, 9
# # Output : 3, 2,1, 6, 9, 8, 7, 4
#
# my_arr = [[3, 2, 1],
#           [4, 5, 6],
#           [7, 8, 9]]
#
#
# def two_d_arr(my_arr):
#     for i in range(len(my_arr)):
#         for j in range(len(my_arr[i])):
#             if i == 0 or i == len(my_arr) - 1 or j == 0 or j == len(my_arr[i]) - 1:
#                 print(my_arr[i][j], end=", ")
#
#
# two_d_arr(my_arr)
# print()
#
# # 2. Deleting a word from a sentence.
# # For ex - Today is a fun day.
# # Output - Today is a day.
# # Delete "fun" from the sentence
#
# sentence = "Today is a fun day."
# remove_word = "fun"
#
#
# def delete_word(sentence, remove_word):
#     return ' '.join([word for word in sentence.split() if word != remove_word])
#
#
# new_sentence = delete_word(sentence, remove_word)
# print(new_sentence)
#
# # Questions :
# # 1. Print the first non-repeating character in a string.
#
# my_str = "Welcome to India"
#
#
# def non_rep_char(my_str):
#     for char in my_str:
#         if my_str.count(char) == 1:
#             return char
#     return None
#
#
# result = non_rep_char(my_str)
#
# if result:
#     print("First non-repeating character is: ", result)
# else:
#     print("No non-repeating characters found")
#
# # 2. Find second smallest number in an integer array.
#
# intgr_array = [17, 38, 65, 74, -9, 88]
#
#
# def second_smallest(intgr_array):
#     if len(intgr_array) < 2:
#         return None
#     sorted_arr = sorted(intgr_array)
#     return sorted_arr[1]
#
#
# result = second_smallest(intgr_array)
#
# if result is not None:
#     print("Second smallest number is: ", result)
# else:
#     print("There is no second smallest number")
#
# # 3. Implement linked list in java using class.
#
#
# # 1. write a java/python code to Swap two strings without using third variable
#
# string1 = "Malayalam"
# string2 = "Tamil"
#
#
# def swap_str(str1, str2):
#     str1, str2 = str2, str1
#     return str1, str2
#
#
# string1, string2 = swap_str(string1, string2)
#
# print("String1 after swapping:", string1)
# print("String2 after swapping:", string2)
#
# # 2. Write a java/python code to merging two arrays
#
# array1 = [15, 27, 88]
# array2 = [34, 50, 91]
#
# merged_array = array1 + array2
# print(merged_array)
# # OR
# array1.extend(array2)
# print(array1)


# November 2
# 1. Write a program to check if given 2 strings are anagrams and what is time and space complexity
# “silent” and “listen”

# string1 = "silent"
# string2 = "listen"
#
#
# def anagram(s1, s2):
#     if "".join(sorted(s1)) == "".join(sorted(s2)):
#         print("Given string is an anagram")
#     else:
#         print("Given string is not an anagram")
#
#
# anagram(string1, string2)

# 2. Input: int[] arr1 ={1, 10, 20, 40, 50};
# int[] arr2 ={1, 5, 10, 20, 20, 65, 100};
# //Output: 1 5 10 20 40 50 65 100
# [Merge 2 arrays and sort in ascending] - And calculate time and space complexity

#
# arr1 = [1, 10, 20, 40, 50]
# arr2 = [1, 5, 10, 20, 20, 65, 100]


# def merge_sort_array(arr1, arr2):
#     merged_array = arr1 + arr2
#     merged_array = list(set(merged_array))
#     merged_array.sort()
#     return merged_array
#
#
# result = merge_sort_array(arr1, arr2)
# print(result)

# 1. Test cases for file upload functionality
# 2. Explain Optimizations in test framework


# November 3

# 1. Get distinct characters and their count in a string
# Input AABBBCCCC -> A2B3C4

# input_string = "AABBBCCCC"
#
# distinct_characters_count = [(char, input_string.count(char)) for char in set(input_string)]
# distinct_characters_count.sort()
# distinct_characters_count = "".join([f"{character}{count}" for character, count in distinct_characters_count])
# print(distinct_characters_count)

# Sort() and join() are the complexity of this program


# 2. Find the pairs in array which give sum of 10 - [1, 4, 5, 6, 3, 9,-1, 11]

# input_array = [1, 4, 5, 6, 3, 9, -1, 11]
# target_sum = 10
#
#
# def sum_of_array(input_arr, given_sum):
#     find_pairs = [(x, y) for i, x in enumerate(input_arr) for y in input_arr[i + 1:] if x + y == given_sum]
#     return find_pairs
#
#
# pairs = sum_of_array(input_array, target_sum)
# print("The pairs of arrays are :", pairs)


# 3. List down the testcases which covers edge cases for amazon search
#
# Positive :
#
# Case insensitive
# Multiple key words
# Partial keyword
# Special chars
# Voice input
# Auto suggestions
#
# Negative :
#
# Blank search
# Non existing product
# Different language
# Mis spelled keywords
# Out of stock product and display its msg


# NOvember 6

# 1. Write a program to calculate the number of vowels and consonants in a String.

# s = "Tuples are more memory efficient than lists"
# vowels = "aeiou"
#
#
# def count_vowels_consonants(string):
#     vowels_count = 0
#     consonants_count = 0
#
#     for char in string.lower():
#         if char in vowels:
#             vowels_count += 1
#         elif char.isalpha():
#             consonants_count += 1
#     return vowels_count, consonants_count
#
#
# vowels_count, consonants_count = count_vowels_consonants(s)
# print("Number of vowels:", vowels_count)
# print("Number of consonants:", consonants_count)

# 2. write a program to show scroll up and scroll down in ui and mobile automation


# November 7

# 1. Find all the sub-strings in a string "abc"
# a, b, c, ab, bc, abc
#
# s = "abc"
# substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
#
# for substring in substrings:
#     print(substring)

# 2. Arrange ODD and Even. Even one's first, odd ones later
# Input : 1 3 2 5 6 4 7 8 9
# Output: 2,4,6,8,1,3,5,7,9

# input_string = [1, 3, 2, 5, 6, 4, 7, 8, 9]
#
#
# def arrange_odd_even_numbers(numbers):
#     even_numbers = [str(num) for num in numbers if num % 2 == 0]
#     odd_numbers = [str(num) for num in numbers if num % 2 != 0]
#
#     even_numbers.extend(odd_numbers)
#     result = ",".join(even_numbers)
#     return result
#
#
# output = arrange_odd_even_numbers(input_string)
# print(output)


# November 8

# Program to find the student who has scored highest marks
# Student {RollNo, Name, Marks}

# student_details = [
#     {"RollNo": 1, "Name": "Ram", "Marks": 97},
#     {"RollNo": 2, "Name": "Priya", "Marks": 88},
#     {"RollNo": 3, "Name": "Pavi", "Marks": 38},
#     {"RollNo": 4, "Name": "Nibhun", "Marks": 76},
#     {"RollNo": 5, "Name": "Anu", "Marks": 17},
# ]
#
# highest_marks = 0
# top_student = None
#
# for student in student_details:
#     if student["Marks"] > highest_marks:
#         highest_marks = student["Marks"]
#         top_student = student
#
# if top_student is not None:
#     print("Student with the highest marks:")
#     print("RollNo:", top_student["RollNo"])
#     print("Name:", top_student["Name"])
#     print("Marks:", top_student["Marks"])
# else:
#     print("No student found")

# 1. How to upload a file in selenium
# 2, How to switch to window and back to default window.


# November 9
#
# 1. MinimumOccurenceOfChar "cdadcda" -> c
# example -> "cdadcdaa"

# input_string = "cdadcdaa"
#
#
# def find_min_occurrence(input_string):
#     char_count = {char: input_string.count(char) for char in set(input_string)}
#     min_char = min(char_count, key=char_count.get)
#     return min_char


# result = find_min_occurrence(input_string)
# print("Minimum occurance of a character is :", result)


# 2. Count number of words in String str = "One two      three\n four\tfive"
# Output : 5

# my_string = "One two      three\n four\tfive"
#
# count_no_of_words = len(my_string.split())
# print("Output is :", count_no_of_words)


# Nov 16 :


# 1. int[] arr = {1,2,3,4}; // output {24, 12, 8, 6}
# 2. int[] arr2 = {-1,1,0,-3,3}; // output {0,0,9,0,0}
# find the product of the other elements in the array -> ProductOfArrayExceptSelf

# arr1 = [1, 2, 3, 4]
# arr2 = [-1, 1, 0, -3, 3]
#
#
# def prod_except_self(nums):
#     n = len(nums)
#
#     left_product = [1] * n
#     right_product = [1] * n
#
#     for i in range(1, n):
#         left_product[i] = left_product[i - 1] * nums[i - 1]
#
#     for i in range(n - 2, -1, -1):
#         right_product[i] = right_product[i + 1] * nums[i + 1]
#
#     result = [left_product[i] * right_product[i] for i in range(n)]
#     return result
#
#
# result1 = prod_except_self(arr1)
# print("Array 1 is :", result1)
#
# result2 = prod_except_self(arr2)
# print("Array 2 is :", result2)


# Nov 20

# Given a number N, check if a number is perfect or not.
# A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.
# Return 1 if the number is Perfect otherwise return 0.
# Factors of 6 are 1, 2, 3 and 6.
# Excluding 6 their sum is 6 which
# is equal to N itself. So, it's a
# Perfect Number.

# def is_perfect(n):
#     if n <= 0:
#         return 0
#
#     sum_of_factors = sum([i for i in range(1, n) if n % i == 0])
#     return 1 if sum_of_factors == n else 0
#
#
# input_number = int(input("Enter a number : "))
# result = is_perfect(input_number)
#
# if result == 1:
#     print(f"{input_number} is a perfect number")
# else:
#     print(f"{input_number} is not a perfect number")

# output -> 6, 28, 496


# Nov 21

# Create a interface "MotorVehicle".
# create a method called "build"
# Create another class Motorcycle which implements MotorVehicle
# Overide the build method and add a print statement.
# Do the same with Car class as well.
# Create a Main class and print all 3 statements

# from abc import abstractmethod
#
#
# class MotorVehicle:
#
#     @abstractmethod
#     def build(self):
#         print("Motor Vehicle")
#
#
# class MotorCycle(MotorVehicle):
#     def build(self):
#         print("Motor Cycle")
#
#
# class Car(MotorVehicle):
#
#     def build(self):
#         print("Car")
#
#
# m = MotorCycle()
# c = Car()
#
# m.build()
# c.build()


# NOv 22

# Given four different points in space. Find whether these points can form a square or not.
# Input:
# x1 = 20, y1 = 10, x2 = 10, y2 = 20,
# x3 = 20, y3 = 20, x4 = 10, y4 = 10

# Output:
# Yes
# Explanation:
# The points (20,10), (10,20), (20,20),
# (10,10) forms a square.

# import math
#
# x1, y1 = 20, 10
# x2, y2 = 10, 20
# x3, y3 = 20, 20
# x4, y4 = 10, 10


#
# This defines a function distance that takes four parameters (coordinates of two points)
# and calculates the Euclidean distance between them using the distance formula.
# def distance(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# This defines a function is_Square that takes eight parameters representing the coordinates of four points.
# It also initializes an empty set called distances to store unique distances.
# def is_Square(x1, y1, x2, y2, x3, y3, x4, y4):
#     distances = set()
#
#     distances.add(distance(x1, y1, x2, y2))
#     distances.add(distance(x2, y2, x3, y3))
#     distances.add(distance(x3, y3, x4, y4))
#     distances.add(distance(x4, y4, x1, y1))
#     distances.add(distance(x1, y1, x3, y3))
#     distances.add(distance(x2, y2, x4, y4))

# This calculates the distances between all pairs of points using the distance function and adds them to the
# distances set

# return len(distances) == 2


# This checks if there are exactly two unique distances in the set.
# In a square, there are two unique distances: one for the sides and one for the diagonals.

#
# if is_Square(x1, y1, x2, y2, x3, y3, x4, y4):
#     print("Yes")
# else:
#     print("No")

# This calls the is_Square function with the given points and prints "Yes" if it returns True,
# indicating that the points form a square. Otherwise, it prints "No".


# Nov 23

