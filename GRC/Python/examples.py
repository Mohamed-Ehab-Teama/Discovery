# 1- Problem Description
# You need to find the smallest number in a list of integers. The list can have up to 100 elements.


# 2- Write a program to determine if a given word is a palindrome (reads the same forwards and backwards). You can ignore spaces and punctuation.


# 3- Create a program that counts how many times each vowel (a, e, i, o, u) appears in a given sentence.

# 4- Problem Description Develop a program that checks if a number is prime. A prime number is only divisible by 1 and itself.


# 5-Problem Description Write a program that finds the most frequently occurring element in an array. If there is a tie, return the smallest element.


# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

# Solution

# 1- 
# numbers = [34, 12, 56, 78, 2, 45]
# smallest_number = min(numbers)
# print("The smallest number is:", smallest_number)

# ---
# numbers = [34, 12, 56, 78, 2, 45]
# smallest_number = numbers[0]
# for number in numbers:
#     if number < smallest_number:
#         smallest_number = number
# print("The smallest number is:", smallest_number)

# ----------------------------------------------------------
# 2-
# def is_palindrome(word):
#     cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
#     return cleaned_word == cleaned_word[::-1]
# input_word = "A man, a plan, a canal, Panama!"
# if is_palindrome(input_word):
#     print(f'"{input_word}" is a palindrome.')
# else:
#     print(f'"{input_word}" is not a palindrome.')

# ----------------------------------------------------------
# 3- 
# def count_vowels(sentence):
#     vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
#     for char in sentence.lower():  # Convert to lowercase for case-insensitive comparison
#         if char in vowel_counts:  # Check if the character is a vowel
#             vowel_counts[char] += 1  # Increment the count for that vowel
    
#     print(f"a: {vowel_counts['a']}, e: {vowel_counts['e']}, i: {vowel_counts['i']}, o: {vowel_counts['o']}, u: {vowel_counts['u']}")

# sentence = "Hello, how are you?"

# count_vowels(sentence)

# ----------------------------------------------------------
# 4-
# import math

# def is_prime(number):
#     # Handle edge cases
#     if number <= 1:
#         return False  # Numbers less than or equal to 1 are not prime
#     if number == 2:
#         return True  # 2 is the only even prime number
#     if number % 2 == 0:
#         return False  # Other even numbers are not prime
    
#     # Check divisibility from 3 up to the square root of the number
#     for i in range(3, int(math.sqrt(number)) + 1, 2):  # Step by 2 to skip even numbers
#         if number % i == 0:
#             return False  # Number is divisible by i, so it's not prime
    
#     return True  # If no divisors are found, the number is prime

# number = 29

# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")
    
# ----------------------------------------------------------

# 5-
# def most_frequent_element(arr):
#     if not arr:  # Handle empty array
#         return None
    
#     # Count frequencies manually
#     frequency = {}
#     for num in arr:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1
    
#     # Find the most frequent element
#     most_frequent = None
#     max_count = 0
    
#     for num, count in frequency.items():
#         if count > max_count or (count == max_count and (most_frequent is None or num < most_frequent)):
#             most_frequent = num
#             max_count = count
    
#     return most_frequent

# # Input: An array of integers
# arr = [1, 3, 2, 3, 4, 1, 1, 2, 2]

# # Find the most frequent element
# result = most_frequent_element(arr)

# # Output the result
# if result is not None:
#     print("The most frequent element is:", result)
# else:
#     print("The array is empty.")
    
# ----------------------------------------------------------
