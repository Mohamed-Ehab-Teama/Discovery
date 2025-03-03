# 1. Print "Hello, World!"

print("Hello, World!")

# 2. Add Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# 3. Check Even or Odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4. Find the Maximum of Three Numbers

a, b, c = map(int, input("Enter three numbers: ").split())
print("Maximum:", max(a, b, c))

# 5. Reverse a String

string = input("Enter a string: ")
print("Reversed:", string[::-1])

# 6. Find the Factorial of a Number

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

# 7. Check for a Palindrome String

string = input("Enter a string: ")
print("Palindrome" if string == string[::-1] else "Not a Palindrome")

# 8. Sum of Natural Numbers

n = int(input("Enter a number: "))
print("Sum:", (n * (n + 1)) // 2)

# 9. Generate Fibonacci Series

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Enter the number of terms: "))
fibonacci(n)

# 10. Find the Largest Element in a List

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest:", max(numbers))


# 11. Find the Smallest Element in a List

numbers = list(map(int, input("Enter numbers: ").split()))
print("Smallest:", min(numbers))

# 12. Count Vowels in a String

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print("Vowel Count:", count)

# 13. Check if a Number is Prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
print("Prime" if is_prime(num) else "Not Prime")

# 14. Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 15. Find the Length of a String

string = input("Enter a string: ")
print("Length:", len(string))

# 16. Swap Two Variables Without a Temporary Variable

a, b = map(int, input("Enter two numbers: ").split())
a, b = b, a
print("Swapped Values:", a, b)

# 17. Count Digits in a Number

num = input("Enter a number: ")
print("Number of digits:", len(num))

# 18. Calculate the Power of a Number

base, exponent = map(int, input("Enter base and exponent: ").split())
print("Result:", base ** exponent)

# 19. Convert a String to Uppercase

string = input("Enter a string: ")
print("Uppercase:", string.upper())

# 20. Convert a String to Lowercase

string = input("Enter a string: ")
print("Lowercase:", string.lower())


# 21. Check Leap Year

year = int(input("Enter a year: "))
print("Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year")

# 22. Calculate the Square of a Number

num = int(input("Enter a number: "))
print("Square:", num ** 2)

# 23. Convert Kilometers to Miles

km = float(input("Enter kilometers: "))
miles = km * 0.621371
print("Miles:", miles)

# 24. Count the Occurrences of an Element in a List

numbers = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter number to count: "))
print("Occurrences:", numbers.count(element))

# 25. Find the ASCII Value of a Character

char = input("Enter a character: ")
print("ASCII Value:", ord(char))

# 26. Check If a String is a Digit

string = input("Enter a string: ")
print("Contains only digits" if string.isdigit() else "Contains non-digit characters")

# 27. Calculate the Area of a Circle

import math
radius = float(input("Enter radius: "))
print("Area:", math.pi * radius ** 2)

# 28. Merge Two Lists

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
print("Merged List:", list1 + list2)

# 29. Find the Second Largest Number in a List

numbers = list(map(int, input("Enter numbers: ").split()))
numbers.remove(max(numbers))
print("Second Largest:", max(numbers))

# 30. Find the Sum of Digits of a Number

num = int(input("Enter a number: "))
sum_digits = sum(int(digit) for digit in str(num))
print("Sum of digits:", sum_digits)
