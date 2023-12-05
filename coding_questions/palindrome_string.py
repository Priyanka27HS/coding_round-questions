# 2. Given a string, determine if a permutation of string could be a palindrome.
# Input : abaab
# Output : ababa

input_str = "abaab"


def if_palindrome(s):

    # Initializes an empty dictionary to store the count of each character in the input string
    char_count = {}

    # Count the frequency of each character in the string
    #  Updates the count of the current character in the dictionary.
    #  If the character is not present in the dictionary, it initializes the count to 0 and then increments it by 1.
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Count how many characters have an odd frequency
    odd_count = sum(count % 2 != 0 for count in char_count.values())

    # A palindrome permutation is possible if there is at most one character with an odd frequency
    return odd_count <= 1


result = if_palindrome(input_str)
print(result)
