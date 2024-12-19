# 1 - Write a function sum_two_numbers(a, b) that takes two integers a and b as arguments and returns their sum.
def sum_two_numbers(a, b):
    return a + b
result = sum_two_numbers(3, 5)
print(result)  # Output: 8



# 2 - Write a function is_even(number) that takes an integer number as an argument and returns True if the number is even, and False otherwise.
def is_even(number):
    return number % 2 == 0
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False



# 3 - Write a function max_of_three(x, y, z) that takes three numbers x, y, and z as arguments and returns the largest of the three.
def max_of_three(x, y, z):
    return max(x, y, z)
print(max_of_three(3, 7, 5))  # Output: 7



# 4 - Write a function factorial(n) that takes a non-negative integer n and returns its factorial. 
    # The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))  # Output: 120



# 5 - Write a function fibonacci(n) that takes a positive integer n and returns a list containing the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]



# 6 - Write a function find_min(a, b, c) that takes three numbers as input and returns the smallest of the three.
def find_min(a, b, c):
    return min(a, b, c)
print(find_min(3, 7, 5))  # Output: 3



# 7 - Write a function count_vowels(text) that takes a string as input and returns the number of vowels in the string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))  # Output: 3



# 8 - Write a function reverse_string(s) that takes a string as input and returns the reversed string.
def reverse_string(s):
    return s[::-1]
print(reverse_string("Python"))  # Output: nohtyP



# 9 - Write a function is_palindrome(s) that checks if a string is a palindrome (reads the same forward and backward). Return True if it is, otherwise False.
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False



# 10 - Write a function list_length(lst) that takes a list as input and returns its length.
def list_length(lst):
    return len(lst)
print(list_length([1, 2, 3, 4, 5]))  # Output: 5



# 11 - Write a function multiply_list(lst, factor) that multiplies each element in a list by a given factor and returns the new list.
def multiply_list(lst, factor):
    return [x * factor for x in lst]
print(multiply_list([1, 2, 3], 2))  # Output: [2, 4, 6]




# 12 - Write a function find_index(lst, element) that returns the index of the first occurrence of an element in a list. If the element is not found, return -1.
def find_index(lst, element):
    if element in lst:
        return lst.index(element)
    return -1
print(find_index([10, 20, 30, 40], 30))  # Output: 2
print(find_index([10, 20, 30, 40], 50))  # Output: -1




# 13 - Write a function list_to_string(lst) that takes a list of strings and concatenates them into a single string with spaces.
def list_to_string(lst):
    return " ".join(lst)
print(list_to_string(["I", "love", "Python"]))  # Output: I love Python




# 14 - Write a function common_elements(list1, list2) that returns a list of elements that are common between two lists.
def common_elements(list1, list2):
    return list(set(list1) & set(list2))
print(common_elements([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]




# 15 - Write a function word_frequency(text) that takes a string and returns a dictionary with each word as a key and its frequency as the value.
def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
print(word_frequency("hello world hello"))  # Output: {'hello': 2, 'world': 1}