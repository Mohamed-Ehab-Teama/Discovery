# 1- Write a function that swaps two numbers without using a third variable.
def swap(a, b):
    a, b = b, a  # Swap using tuple unpacking
    return a, b
# Example usage:
print(swap(5, 10))  # Output: (10, 5)
print(swap(-1, 3))  # Output: (3, -1)


# #####################################################################
# 2- Write a function that checks if a given number is a perfect square (e.g., 4, 9, 16, 25).
import math
def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n
# Example usage:
print(is_perfect_square(25))  # Output: True
print(is_perfect_square(26))  # Output: False

# Explain: math.isqrt() => returns the largest integer whose square is less than or equal to the specified number.


# #####################################################################
# 3- Write a function that reverses the digits of a given number.
def reverse_number(n):
    return int(str(n)[::-1])
# Example usage:
print(reverse_number(12345))  # Output: 54321
print(reverse_number(9876))  # Output: 6789


# #####################################################################
# 4- Write a function that returns the sum of digits of a given number.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
# Example usage:
print(sum_of_digits(123))  # Output: 6
print(sum_of_digits(9876))  # Output: 30


# #####################################################################
# 5- Write a function that checks if a list of numbers is a palindrome (reads the same forward and backward).
def is_palindrome(lst):
    return lst == lst[::-1]
# Example usage:
print(is_palindrome([1, 2, 3, 2, 1]))  # Output: True
print(is_palindrome([1, 2, 3, 4, 5]))  # Output: False


# #####################################################################
# 6- Write a function that merges two sorted lists into one sorted list.
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)
# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([10, 20], [15, 25]))  # Output: [10, 15, 20, 25]


# #####################################################################
# 7- Write a function that counts the number of words in a given string.
def count_words(sentence):
    return len(sentence.split())
# Example usage:
print(count_words("Hello world! Python is awesome."))  # Output: 5
print(count_words("This is a test sentence."))  # Output: 5


# #####################################################################
# 8- Write a function that converts a list of characters into a string.
def list_to_string(char_list):
    return "".join(char_list)
# Example usage:
print(list_to_string(['P', 'y', 't', 'h', 'o', 'n']))  # Output: "Python"
print(list_to_string(['H', 'e', 'l', 'l', 'o']))  # Output: "Hello"


# #####################################################################
# 9- Write a function that finds the common elements between two lists.
def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
# Example usage:
print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]
print(list_intersection(["apple", "banana", "cherry"], ["banana", "cherry", "date"]))  # Output: ["banana", "cherry"]


# #####################################################################
# ##################################################################### NEW & GOOD
# #####################################################################
# 10- Write a function that removes duplicate elements from a list while maintaining the order.
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
# Example usage:
print(remove_duplicates([1, 2, 3, 2, 1, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(remove_duplicates(["apple", "banana", "apple", "cherry"]))  # Output: ["apple", "banana", "cherry"]

# Explain : dict.fromkeys(lst) => Will take the list items and make them keys for the dictionary


# #####################################################################
# 11- Write a function that finds the second largest number in a list.
def second_largest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort(reverse=True)
    return unique_lst[1] if len(unique_lst) > 1 else None
# Example usage:
print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
print(second_largest([5, 5, 5, 5]))  # Output: None


# #####################################################################
# 12- Write a function that checks if two strings are anagrams of each other (i.e., have the same characters in different orders).
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
# Example usage:
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))  # Output: False


# #####################################################################
# ##################################################################### GOOD
# #####################################################################
# 13- Write a function that calculates the factorial of a number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# Example usage:
print(factorial(5))  # Output: 120
print(factorial(7))  # Output: 5040

# Explain : Recursion => Call the function inside itself.


# #####################################################################
# 14- Write a function that finds the common elements in three lists.
def common_elements(lst1, lst2, lst3):
    return list(set(lst1) & set(lst2) & set(lst3))
# Example usage:
print(common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5]))  # Output: [3]
print(common_elements(["a", "b", "c"], ["b", "c", "d"], ["c", "d", "e"]))  # Output: ["c"]


# #####################################################################
# 15- Write a function that finds the missing number in a list of consecutive numbers.
def find_missing(lst):
    return set(range(lst[0], lst[-1] + 1)) - set(lst)
# Example usage:
print(find_missing([1, 2, 4, 5, 6]))  # Output: {3}
print(find_missing([10, 11, 13, 14]))  # Output: {12}


# #####################################################################
# 16- Write a function that checks if two strings are rotations of each other.
def are_rotations(str1, str2):
    return len(str1) == len(str2) and str2 in (str1 + str1)
# Example usage:
print(are_rotations("abcd", "cdab"))  # Output: True
print(are_rotations("hello", "lohel"))  # Output: True
print(are_rotations("hello", "world"))  # Output: False


# #####################################################################
# 17- Write a function to find the Greatest Common Divisor (GCD) of two numbers.
import math
def find_gcd(a, b):
    return math.gcd(a, b)
# Example usage:
print(find_gcd(48, 18))  # Output: 6
print(find_gcd(100, 25))  # Output: 25


# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
# #####################################################################
