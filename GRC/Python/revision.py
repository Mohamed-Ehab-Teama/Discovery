# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# x, y = map(int, input().split())

# if (x*y <= 1000):
#     print(x*y)
# else:
#     print(x+y)

# ---------------------------------------------------------------------------------------------

# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# for i in range(1, 11):
#     print( f"{i} + {i-1} = {i+i-1}" )

# previous = 0
# for number in range(1,11):
#     print( f" the sum of {number} and {previous} is {number + previous} " )
#     previous = number


# ---------------------------------------------------------------------------------------------

# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

# word = input()
# print( word[::2] )

# word = input()  # AhmedHere
# n = len(word)   # 9

# for i in range(0 , n ):   # 0 1 2 3 4 5 6 7 8
#     if i % 2 == 0 :
#         print( word[i] )

# ---------------------------------------------------------------------------------------------

# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

# For Example:
# remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
# remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.

# def remove_chars( word, n ):
#     print( word[n:] )

# remove_chars("PYnative", 4)

# ---------------------------------------------------------------------------------------------

# Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.


# myList = list( map( int, input().split()) )
# if myList[0] == myList[-1]:
#     print( True )
# else:
#     print( False )


# ---------------------------------------------------------------------------------------------

# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5 in this list:
# [10, 20, 33, 46, 55, 68, 90, 48, 40, 251, 250, 245, 536, 520]

# my_list = [10, 20, 33, 46, 55, 68, 90, 48, 40, 251, 250, 245, 536, 520]

# for i in my_list:
#     if i % 5 == 0:
#         print(i, end=" ")

# ---------------------------------------------------------------------------------------------

# Exercise 7: Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.
# "Emma is good developer. Emma is a writer. Emma is good, Emma is great"


# def how_many( statement ):
#     return statement.count("Emma")

# sta = "Emma is good developer. Emma is a writer. Emma is good, Emma is great"
# print( how_many(sta) )


# ---------------------------------------------------------------------------------------------

# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()

# ---------------------------------------------------------------------------------------------

# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.

# ---------------------------------------------------------------------------------------------

# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write a Python code to create a new list such that:
# - the latest list should contain odd numbers from the first list and even numbers from the second list.

# ---------------------------------------------------------------------------------------------