# Problem 1: Anagram Checker
# Task: Write a function to check if two strings are anagrams of each other.

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Example usage
print(are_anagrams("List en", "Silent"))  # Output: True
print(are_anagrams("He llo", "Olelh"))    # Output: True
print(are_anagrams("Python", "Java"))    # Output: False


# ====================================================================
# ====================================================================
# ====================================================================


# Problem 2: Fibonacci Sequence Generator
# Task: Write a function to generate the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example usage
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ====================================================================
# ====================================================================
# ====================================================================

# Problem 3: Matrix Transposition
# Task: Write a function to transpose a given matrix.

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

# def transpose_matrix(matrix):
    # res = []
    # for row in zip(*matrix):
    #     res.append( list(row) )
    # return res

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print(transposed)
# Output: 
# [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]


# ====================================================================
# ====================================================================
# ====================================================================

# Problem 4: Merge Sorted Lists
# Merge two sorted lists into one sorted list.

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

# Example usage
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]


# ====================================================================
# ====================================================================
# ====================================================================


# Problem 5: Check if a Number is Prime
# Problem: Create a function that determines if a given number is prime.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check till sqrt(n)
        if n % i == 0:
            return False
    return True

print(is_prime(11))  # Output: True


# ====================================================================
# ====================================================================
# ====================================================================


# Problem 6: Find the First Non-Repeating Character
# Problem: Given a string, find the first character that doesn't repeat.

def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

print(first_non_repeating_char("aabccdeff"))  # Output: "b"


# ====================================================================
# ====================================================================
# ====================================================================


# Problem 7: Convert Roman Numerals to Integers
# Problem: Convert a Roman numeral string into an integer.

def roman_to_int(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    total = 0
    prev = 0
    for char in reversed(s):
        current = values[char]
        if current < prev:
            total -= current
        else:
            total += current
        prev = current
    return total

print(roman_to_int("XIV"))  # Output: 14


# ====================================================================
# ====================================================================
# ====================================================================


# Problem 8: Find All Pairs in an Array That Sum to a Target
# Problem: Find all pairs of numbers in an array that add up to a target value.

def find_pairs(arr, target):
    seen = set()
    pairs = []
    for num in arr:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

print(find_pairs([1, 2, 3, 4, 5, 6], 7))  # Output: [(1, 6), (2, 5), (3, 4)]


# ====================================================================
# ====================================================================
# ====================================================================


# Problem 9: Find the Intersection of Two Sorted Arrays
# Problem: Find the common elements between two sorted arrays.

def sorted_intersection(arr1, arr2):
    i, j = 0, 0
    intersection = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return intersection

print(sorted_intersection([1, 3, 4, 6], [2, 3, 6, 8]))  # Output: [3, 6]


# ====================================================================
# ====================================================================
# ====================================================================
