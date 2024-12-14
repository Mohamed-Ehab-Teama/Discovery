# 1 - Write a program that takes a person's name and age as input and prints a message in the following format:
    # "Hello, [Name]. You are [Age] years old!"
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print( f"Hello, {name}. You are {age} years old!" )



# 2 - Write a program that reads two numbers as input, converts them into integers, and prints their sum.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The sum is:", num1 + num2)



# 3 - Write a program that calculates the area of a circle given its radius. Use the formula:
    # Area = πr², where π = 3.14.
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area}")



# 4 - Write a program to determine whether a number entered by the user is positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# 5 - Write a program to generate and print the multiplication table for a number entered by the user.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")



# 6 - Write a program that takes a list of numbers as input and prints the largest number.
numbers = list(input("Enter numbers separated by space: ").split())
print("The largest number is:", max(numbers))



# 7 - Write a program that creates a tuple with five numbers. Print the sum and average of the numbers in the tuple.
numbers = (10, 20, 30, 40, 50)
total = sum(numbers)
average = total / len(numbers)
print(f"Sum: {total}, Average: {average}")



# 8 - Write a program that takes a list of numbers as input and prints only the unique numbers using a set.
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
unique_numbers = set(numbers)
print("Unique elements are:", unique_numbers)



# 9 - Write a program that counts the frequency of each word in a sentence provided by the user. 
    # Output the result as a dictionary.
sentence = input("Enter a sentence: ")
# Hello Welcome hi Ahemd hi Hello
words = sentence.split()
# [Hello, Welcome, hi, Ahemd, hi, Hello]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequencies:", word_count)



# 10 - Write a program to reverse a number entered by the user using a while loop.
number = int(input("Enter a number: "))
        # number = 0.7
reverse = 0
        # reverse = 357
        # remainder = 7
while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number //= 10
print("Reversed number:", reverse)



# --------==========----------============------------============---------
# Problems:

# 1 - Write a program that takes a person's name and age as input and prints a message in the following format:
    # "Hello, [Name]. You are [Age] years old!"
    
# 2 - Write a program that reads two numbers as input, converts them into integers, and prints their sum.

# 3 - Write a program that calculates the area of a circle given its radius. Use the formula:
    # Area = πr², where π = 3.14.
    
# 4 - Write a program to determine whether a number entered by the user is positive, negative, or zero.

# 5 - Write a program to generate and print the multiplication table for a number entered by the user.

# 6 - Write a program that takes a list of numbers as input and prints the largest number.

# 7 - Write a program that creates a tuple with five numbers. Print the sum and average of the numbers in the tuple.

# 8 - Write a program that takes a list of numbers as input and prints only the unique numbers using a set.

# 9 - Write a program that counts the frequency of each word in a sentence provided by the user. 
    # Output the result as a dictionary.
    
# 10 - Write a program to reverse a number entered by the user using a while loop.

# --------==========----------============------------============---------