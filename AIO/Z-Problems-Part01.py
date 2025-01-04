# 1- Write a Python program to find the sum of all multiples of 3 or 5 below 1000.
def sum_of_multiples(limit):
    total = sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)
    return total
# Example usage:
print(sum_of_multiples(1000))  # Output: 233168


# #####################################################################
# 2- Write a Python function to compute the factorial of a given number.
    # The factorial of 0 has value of 1, and 
    # the factorial of a number n is equal to the multiplication between the number n and the factorial of n-1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# Example usage:
print(factorial(5))  # Output: 120

# ========= Another Solution
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Example usage
print(factorial_loop(5))  # Output: 120


# #####################################################################
# 3- Write a Python function that takes a string and returns it reversed.
def reverse_string(s):
    return s[::-1]
# Example usage:
print(reverse_string("hello"))  # Output: "olleh"


# #####################################################################
# 4- Write a Python function that counts the number of vowels (a, e, i, o, u) in a given string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
# Example usage:
print(count_vowels("Python Programming"))  # Output: 5


# #####################################################################
# 5- Write a Python function that finds and returns the largest number in a list.
def find_max(lst):
    return max(lst)
# Example usage:
print(find_max([3, 1, 7, 4, 9, 2]))  # Output: 9


# 6- Write a Python function that finds and returns the smallest number in a list.
def find_min(lst):
    return min(lst)
# Example usage:
print(find_min([3, 1, 7, 4, 9, 2]))  # Output: 1


# #####################################################################
# 7- Write a Python function that returns a list of even numbers from a given list.
def find_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
# Example usage:
print(find_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]


# #####################################################################
# 8- Write a recursive function to generate the Fibonacci sequence up to the nth term.
    # Fibonacci : is defined as the sequence of numbers in which each number in the sequence is equal to the sum of two numbers before it.
# F0=0 and F1=1
    # Using the formula, we get
        # F2 = F1+F0 = 1+0 = 1
        # F3 = F2+F1 = 1+1 = 2
        # F4 = F3+F2 = 2+1 = 3
        # F5 = F4+F3 = 3+2 = 5
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage:
print([fibonacci(i) for i in range(6)])  # Output: [0, 1, 1, 2, 3, 5]


# #####################################################################
# 9- Write a Python function that checks if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Example usage:
print(is_prime(29))  # Output: True
print(is_prime(10))  # Output: False


# #####################################################################
# 10- Write a function that counts the number of words in a given sentence.
def count_words(sentence):
    return len(sentence.split())
# Example usage:
print(count_words("Python is an amazing language!"))  # Output: 5


# #####################################################################
# 11- Write a Python function that checks if a number is prime.
def is_prime(num):
    if num <= 1 :
        return "Not Prime"
    else:
        for i in range(2, num):
            if num % i == 0 :
                return "Not Prime"
                break
        else:
            return "Prime"
print (is_prime(11))


# #####################################################################
# 12- Write a Python function that removes duplicate elements from a list and returns a new list.
def remove_duplicates(lst):
    return list(set(lst))
# Example usage:
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]


# #####################################################################
# 13- Write a Python function that merges two sorted lists into a single sorted list.
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)
# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]


# #####################################################################
# 14- Write a Python function that finds the second largest number in a list.
def second_largest(lst):
    unique_numbers = list(set(lst))  # Remove duplicates
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None
# Example usage:
print(second_largest([1, 3, 5, 5, 4]))  # Output: 4


# #####################################################################
# 15- Write a function that checks if two words are anagrams (contain the same letters in a different order).
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
# Example usage:
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False


# #####################################################################
# 16- Write a Python function that finds the common elements between two lists.
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))
# Example usage:
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]


# #####################################################################
# #############
# 17- Write a Python function that checks if a number is a perfect square.
import math
def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n
# Example usage:
print(is_perfect_square(16))  # Output: True
print(is_perfect_square(18))  # Output: False


# #####################################################################
# 18- Write a function that reverses the order of words in a sentence.
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])
# Example usage:
print(reverse_words("Hello World"))  # Output: "World Hello"


# #####################################################################
# 19- Write a function that returns the longest word in a given sentence.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
# Example usage:
print(longest_word("Python is an amazing programming language"))  
# Output: "programming"


# #####################################################################
# 20- Write a function that finds the intersection (common elements) of two sets.
def set_intersection(set1, set2):
    return set1 & set2
# Example usage:
print(set_intersection({1, 2, 3}, {3, 4, 5}))  # Output: {3}


# #####################################################################
# 21- Write a function that checks if a given string is a palindrome (reads the same forward and backward).
def is_palindrome(s):
    return s == s[::-1]
# Example usage:
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False


# #####################################################################
# 22- Write a function that counts the occurrences of each character in a given string.
from collections import Counter
def char_frequency(s):
    return Counter(s)
# Example usage:
print(char_frequency("hello"))  
# Output: Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1})

# #### Another Solution
def count_characters(s):
    # Create an empty dictionary to store character counts
    char_count = {}
    # Iterate over each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_count[char] = 1
    return char_count


# #####################################################################
# 23- Write a function that returns both the largest and smallest numbers in a given list.
def find_min_max(lst):
    return min(lst), max(lst)
# Example usage:
print(find_min_max([10, 5, 2, 8, 3]))  # Output: (2, 10)


# #####################################################################
# 24- Write a function that counts the number of words in a given sentence.
def count_words(sentence):
    return len(sentence.split())
# Example usage:
print(count_words("Python is fun to learn"))  # Output: 5


# #####################################################################
# 25- Write a function that calculates the sum of the digits of a given number.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
# Example usage:
print(sum_of_digits(1234))  # Output: 10


# #####################################################################
# 26- Write a function that calculates the factorial of a number using recursion.
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
# Example usage:
print(factorial(5))  # Output: 120


# #####################################################################
# 27- Write a function that checks if a list is sorted in ascending order.
def is_sorted(lst):
    return lst == sorted(lst)
# Example usage:
print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([3, 1, 2, 4]))  # Output: False


# #####################################################################
# 28- Write a function that generates the Fibonacci sequence up to n terms.
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]
# Example usage:
print(fibonacci(7))  
# Output: [0, 1, 1, 2, 3, 5, 8]


# #####################################################################
# 29- Write a function that removes duplicate elements from a list while maintaining the original order of the elements.
def remove_duplicates(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
# Example usage:
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(remove_duplicates([10, 10, 20, 30, 20, 10]))  # Output: [10, 20, 30]


# #####################################################################
# 30- Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple words with the same length, return the first one that appears.
def longest_word(sentence):
    words = sentence.split()  # Split sentence into words
    return max(words, key=len)  # Find the longest word
# Example usage:
print(longest_word("The quick brown fox jumps over the lazy dog"))  # Output: "jumps"
print(longest_word("Python is an amazing language"))  # Output: "amazing"


# #####################################################################
# #####################################################################