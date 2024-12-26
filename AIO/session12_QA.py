# 1- Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("What is your name: ")
age = int(input("How old are you: "))
year = 2024 - age + 100
print(name + ", you will be 100 years old in the year " + str(year))

# -----------------------------------------------------------
# 2- write a program to Take a list from the user and print out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# basic problem:
for x in a:
    if x< 5: print(x)

# combine challenges 1 and 2:
print( [ x for x in a if x<5 ] )


my_list = input( "Enter List Numbers separated by space " ).split()
numbers = list( map(int, my_list ))
print( [x for x in numbers if x < 5 ])

# -----------------------------------------------------------
# 3- Create a program that asks the user for a number and then prints out a list of all the divisors of that number

num = int(input("Please choose a number to divide: "))
divisorList = []
for number in range(1, num+1):
    if num % number == 0:
        divisorList.append(number)
print(divisorList)

# -----------------------------------------------------------
# 4- Take two lists, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = [ x for x in list1 if x in list2 ]
common = list( set(common) )
print( common )

# -----------------------------------------------------------
# 5- Ask the user for a string and print out whether this string is a palindrome or not.
str = input("Enter Your Text  ")
if str == str[::-1]:
    print ( "Palindrom" )
else:
    print ( "Not Palindrom" )

# -----------------------------------------------------------
# 6- li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = [x for x in li if x % 2 == 0]
print ( even )

# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
