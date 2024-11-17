# 1. Convert Temperature
# Problem: Write a function to convert temperature from Celsius to Fahrenheit.
# Formula: F = C × 9/5 + 32

# def celsius_to_fahrenheit( celsius ):
#     return (celsius * 9/5 ) + 32
# print ( celsius_to_fahrenheit(25) )

# ------------------------------------------------------------------------------------------------------

# 2. Check if a Number is Divisible by Another
# Problem: Write a function that checks if one number is divisible by another.

# def is_divisible(num1, num2):
#     return num1 % num2 == 0
# print(is_divisible(10, 2))

# ------------------------------------------------------------------------------------------------------

# 3. Write a function that takes the radius of a circle and returns its area
# Formula: Area = 3.14 * (r * r) 

# def circle_area(radius):
#     return 3.14 * (radius ** 2)
# print(circle_area(5)) 

# ------------------------------------------------------------------------------------------------------

# 4. Calculate the Average of a List of Numbers
# Problem: Write a function that takes a list of numbers and returns their average.

# def average(numbers):
#     if len(numbers) > 0 :
#         return sum(numbers) / len(numbers)
#     else:
#         return 0
# print( average([]) )

# ------------------------------------------------------------------------------------------------------

# 5. Remove All Whitespaces from a String
# Problem: Write a function that removes all spaces from a string.

# def remove_whitespace(str):
#     return str.replace(" ", "")
# print(remove_whitespace(" H e l l o W o r l d "))

# ------------------------------------------------------------------------------------------------------

# 6. Count Words in a Sentence
# Problem: Write a function that counts the number of words in a given sentence.

# def count_words(str):
#     words = str.split()
#     return len(words)
# print(count_words("Hello, how are you?"))


# ------------------------------------------------------------------------------------------------------

# 7. Count the Occurrences of a Character in a String
# Problem: Write a function that takes a string and a character, and counts the occurrences of that character in the string

# def count_character(str, char):
#     return str.count(char)
# print(count_character("hello world", "o"))

# ------------------------------------------------------------------------------------------------------

# 8. Check if a String Contains Only Digits
# Problem: Write a function that checks if a given string contains only numeric digits.

# def is_numeric(str):
#     return str.isdigit()
# print(is_numeric("12345"))

# ------------------------------------------------------------------------------------------------------

# 9. Check if a List is Sorted
# Problem: Write a function that checks if a list is sorted in ascending order.

# def is_sorted(lst):
#     return lst == sorted(lst)
# print(is_sorted([1, 2, 3, 4, 5]))
# print(is_sorted([1, 2, 3, 8, 5]))


# ------------------------------------------------------------------------------------------------------

# 10. Replace All Vowels in a String with ‘*’
# Problem: Write a function that replaces all vowels in a string with the character '*'

# def replace_vowels(str):
#     vowels = 'aeiouAEIOU'
#     for vowel in vowels:
#         str = str.replace(vowel, '*')
#     return str
# print(replace_vowels("hello, Mohamed Ehab"))

    
# ------------------------------------------------------------------------------------------------------

# 11. Calculate the Product of All Numbers in a List
# Problem: Write a function that returns the product of all numbers in a list.

# def product_of_list(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return product
# print(product_of_list([1, 2, 3, 4]))

# ------------------------------------------------------------------------------------------------------

# 12. Sum of Even Numbers in a List
# Problem: Write a function that takes a list of numbers and returns the sum of all even numbers.

# def sum_of_even(numbers):
#     return sum(num for num in numbers if num % 2 == 0)
# print(sum_of_even([1, 2, 3, 4, 5, 6]))

# ------------------------------------------------------------------------------------------------------

