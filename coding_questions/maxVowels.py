# DEC 1

# 1. write the program for finding MaxVowelsInGivenSubString
#     Input: s = "abciiidef"
#     output
#     3
#     stringaaaaa
#     5

input_string = "abciiidef"


def max_vowels_in_substring(s):
    vowels = set("aeiouAEIOU")
    max_vowels = 0
    current_vowels = 0

    for char in s:
        if char in vowels:
            current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)
        else:
            current_vowels = 0
    return max_vowels


output = max_vowels_in_substring(input_string)
print("Max Vowels In Given SubString is :", output)
