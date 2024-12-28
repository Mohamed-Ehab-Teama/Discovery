# 1- Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# 2- write a program to Take a list from the user and print out all the elements of the list that are less than 5.

# 3- Create a program that asks the user for a number and then prints out a list of all the divisors of that number

# 4- Take two lists, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).

# 5- Ask the user for a string and print out whether this string is a palindrome or not.

# 6- li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# 7 - Write a function word_frequency(text) that takes a string and returns a dictionary with each word as a key and its frequency as the value.

# 8 - Write a function fibonacci(n) that takes a positive integer n and returns a list containing the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(5)) 
