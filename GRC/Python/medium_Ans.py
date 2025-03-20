# 1- Remove Duplicates from a List
# Problem: Write a Python program to a list from the user then remove duplicates from the list.
def remove_duplicates(lst):
    return list(set(lst))

lst = [1, 2, 2, 3, 4, 4, 5]
print("List after removing duplicates:", remove_duplicates(lst))


# =======================================================

# 2- Find the Longest Word in a Sentence
# Problem: Write a Python program to find the longest word in a sentence.

def longest_word(sentence):
    return max(sentence.split(), key=len)

sentence = "I love eating pizza and burger too much"
print("Longest word:", longest_word(sentence))


# =======================================================

# 3- Check if Two Strings are Anagrams
# Problem: Write a Python program to check if two strings are anagrams.

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

s1, s2 = "listen", "silent"
print("Are anagrams:", are_anagrams(s1, s2))


# =======================================================

# 4- Find the Missing Number in a List
# Problem: Write a Python program to find the missing number in a list of integers from 1 to n.

def find_missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

nums = [1, 2, 4, 6, 3, 7, 8]
print("Missing number:", find_missing_number(nums))


# =======================================================

# 5- Find the GCD of Two Numbers
# Problem: Write a Python program to find the greatest common divisor (GCD) of two numbers.

import math
a, b = 12, 15
print("GCD of", a, "and", b, "is:", math.gcd(a, b))


# =======================================================

# 6- Count Words in a Sentence
# Illustration: Count the number of words in a sentence.

def count_words(sentence):
    return len(sentence.split())

sentence = "This is a sample sentence"
print("Word Count:", count_words(sentence))


# =======================================================

# 7-Find All Duplicates in a List

def find_duplicates(lst):
    duplicates = []
    for i in lst:
        if lst.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates

print(find_duplicates([1, 2, 3, 4, 4, 5, 2]))  # Output: [4, 2]


# =======================================================

# 8- Matrix Transposition

def transpose_manual(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Manual Transposition:", transpose_manual(matrix))


# =======================================================

# 9- Check if Two Lists are Permutations of Each Other

def are_permutations(list1, list2):
    return sorted(list1) == sorted(list2)

print(are_permutations([1, 2, 3], [3, 2, 1]))  # True
print(are_permutations([1, 2, 3], [4, 5, 6]))  # False


# =======================================================

# 10- Find the Intersection of Two Lists

def list_intersection(list1, list2):
    return list( set(list1) & set(list2) )

print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]


# =======================================================

# 11- Check if a List is Sorted

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([5, 3, 1]))  # False


# =======================================================

# 12- Check if a String Can Form a Palindrome

def can_form_palindrome(s):
    # Create a dictionary to count character frequencies
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Count characters with odd occurrences
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    # A string can form a palindrome if at most one character has an odd count
    return odd_count <= 1

# Test cases
print(can_form_palindrome("civic"))  # True
print(can_form_palindrome("ivicc"))  # True
print(can_form_palindrome("hello"))  # False
print(can_form_palindrome("aabbccdde"))  # True


# =======================================================