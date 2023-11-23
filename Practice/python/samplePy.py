# String Palindrome
l = ["madam", "bye", "malayalam", "hello"]
result = list(map(lambda item: f"{item} is Palindrome" if item == item[::-1] else f"{item} is not a Palindrome", l))
print(result)

# Palindrome number
num = int(input("Enter a no:"))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# Fibonacci series
def fibo():
    a = 0
    b = 1
    while True:
        yield a
        c = b + a
        a = b
        b = c


f = fibo()
for _ in range(1, 10):
    print(next(f))

# Pattern programs

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(1, 6):
    print(f"{'* ' * i:>10}")

for i in range(1, 6):
    print(f"{'* ' * i:^10}")

# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    print(f"{'* ' * i}")

for i in range(5, 0, -1):
    print(f"{'* ' * i:>10}")

for i in range(5, 0, -1):
    print(f"{'* ' * i:^10}")

# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# vice-versa
for i in range(1, 6):
    s = ""
    for j in range(1, i + 1):
        s = s + str(j) + " "
        print(f"{s:>10}", end=' ')
        print()

#      1
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5

for i in range(1, 6):
    s = ""
    for j in range(1, i + 1):
        s = s + str(j) + " "
        print(f"{s:^10}", end=' ')
        print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def num(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i + 1):
            print(num, end=" ")
            num = num + 1
        print("\r")


n = 5
num(n)


# A
# B B
# C C C
# D D D D
# E E E E E

def alphabet(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
        num = num + 1
        print("\r")


n = 5
alphabet(n)


# A
# B C
# D E F
# G H I J
# K L M N O

def alphamix(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1
        print()


n = 5
alphamix(n)


# Find largest element in an array Using Native Approach
def largest(arr, n):
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [10, 324, 45, 90, 9808]
n = len(arr)
result = largest(arr, n)
print("Largest in given array is : ", result)

# Largest number in a list
numbers = [43, 17, 1504, 21, 30]
large = 0
for number in numbers:
    if number > large:
        large = number
print(large)

# reverse a string without using any inbuilt functions
reverse_ = ""
s = "Welcome to Bengaluru City"
for char in s:
    reverse_ = char + reverse_
print(reverse_)

# Reverse the words in the given string program
str_ = s.split()[::-1]
l = []
for i in str_:
    l.append(i)
print(" ".join(l))


def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False


print(leap_year(1900))
print(leap_year(2004))

from datetime import datetime

date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)


def reverse_string(input_str):
    reversed_string = input_str[::-1]
    return reversed_string


input_string = input("Welcome to Madurai - Temple City : ")

reversed_str = reverse_string(input_string)

print("Reversed string:", reversed_str)


def arr_anangram(str1, str2):
    return sorted(str1) == sorted(str2)


print(arr_anangram("listen", "silent"))


# Write a function to find duplicate elements in a list.
def find_duplicate(l):
    seen = set()
    duplicates = set()
    for item in l:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


print(find_duplicate([1, 2, 3, 2, 4, 5, 3]))


my_str = "City of Nature and peace"
revers_ = ""
for char in my_str:
    revers_ = char + revers_
print(revers_)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)



d = {
    "brand": "Lakme",
    "product": "eyeliner",
    "color": "black",
}
y = d.keys()
print(y)
d["product"] = "lipstick"
print(y)
z = d.values()
print(z)


for x, y in d.items():
    print(x, y)

my_d = d.copy()
print(my_d)
