# Session 2 Task

# name = "Mohamed Ehab Teama"
# age = 22
# height = 175

# print("Mohamed Ehab Teama")
# print(name)
# print(age)
# print(height)




##########################################################
# Session 2 Task

# Develop a Python program that asks the user for their name, age, and height, and then prints a summary using the provided information.

# name = input("Enter Your name: ")
# age = input("Enter Your age: ")
# height = input("Enter Your height: ")

# print('Your name is: ', name)
# print('Your age is: ', age)
# print('Your height is: ', height)

##########################################################
# Session 3 Task

# Develop a program that asks the user to input 2 numbers and do the following operation on them: Addition, Substraction, Multiplication, Division, Floor division, Exponentiation.

# num1 = float(input("Enter the first number please "))
# num2 = float(input("Enter the second number please "))

# print("Addition: ", num1 + num2)
# print("Substraction: ", num1 - num2)
# print("Multiplication: ", num1 * num2)
# print("Division: ", num1 / num2)
# print("Floor Division: ", num1 // num2)
# print("Exponentiation: ", num1 ** num2)



##########################################################
# Session 4 Task

# Write a Python script that checks of a number is posative, negative, or zero

# num = int(input("Enter a number ,please!!  "))

# if num > 0 :
#     print("Number is Posative")
# elif num < 0:
#     print("Number is Nagative")
# else:
#     print("Number is Zero")


##########################################################
# Session 5 Task

# Iterate through a list of numbers and print each number. 
# list = [10,20,30,40,50,60,70,80,90,100,120,150]

# myList = [10,20,30,40,50,60,70,80,90,100,120,150]
# for x in myList:
#     print(x)



# Print every second number from 0 to 20 using the range() function with a step parameter

# nums = range(0,20,2)
# for x in nums:
#     print(x)

##########################################################
##########################################################
# Session 6 Task

# Write a script that prints numbers from 1 to 15 except 8 using a while loop

# x = 1
# while x < 15:
#     if x == 8:
#         x += 1
#         continue
#     print(x)
#     x += 1

# Write a script that prints numbers from 1 to 15 while loop and when the number is 12, exit the loop

# x = 1
# while x < 15:
#     if x == 12:
#         break
#     print(x)
#     x += 1


##########################################################
##########################################################
##########################################################
# project

# Q) Take the id, name, email, the marks of Arabic, English, Math from the user and calculate the grade of each subject and the overall grade:
# 	0 : 50			=> 	Fail
# 	50 : 65		=> 	Pass
# 	65 : 75		=>	Good
# 	75 : 85		=> 	Very good
# 	85 : 95		=>	Excellent
# 	95 : 100		=>	Excellent (H)
# Output the id, name, email, grade of each subject, overall grade
# Note :    overall = (arabicGrade + endlishGrade + mathGrade) / 3


# id = int(input('Enter Your id please    '))
# name = str(input('Enter Your name please    '))
# email = str(input('Enter Your email please  '))
# arabicGrade = float(input('Enter Your Arabic Grade please   '))
# endlishGrade = float(input('Enter Your endlish grade please '))
# mathGrade = float(input('Enter Your math Grade please   '))

# print("ID: ",id)
# print("Name: ",name)
# print("Email: ",email)


# if endlishGrade > 0 and endlishGrade < 50:
#     print("Fail in English")
# elif endlishGrade >= 50 and endlishGrade < 65:
#     print("Pass in English")
# elif endlishGrade >= 65 and endlishGrade < 75:
#     print("Good in English")
# elif endlishGrade >= 75 and endlishGrade < 85:
#     print("Very good in English")
# elif endlishGrade >= 85 and endlishGrade < 95:
#     print("Excellent in English")
# elif endlishGrade >= 95 and endlishGrade <= 100:
#     print("Excellent high in English")
# else:
#     print("Enter a valid mark between 0 and 100")



# if arabicGrade > 0 and arabicGrade < 50:
#     print("Fail in arabic")
# elif arabicGrade >= 50 and arabicGrade < 65:
#     print("Pass in arabic")
# elif arabicGrade >= 65 and arabicGrade < 75:
#     print("Good in arabic")
# elif arabicGrade >= 75 and arabicGrade < 85:
#     print("Very good in arabic")
# elif arabicGrade >= 85 and arabicGrade < 95:
#     print("Excellent in arabic")
# elif arabicGrade >= 95 and arabicGrade <= 100:
#     print("Excellent high in arabic")
# else:
#     print("Enter a valid mark between 0 and 100")



# if mathGrade > 0 and mathGrade < 50:
#     print("Fail in Math")
# elif mathGrade >= 50 and arabicGrade < 65:
#     print("Pass in Math")
# elif mathGrade >= 65 and arabicGrade < 75:
#     print("Good in Math")
# elif mathGrade >= 75 and mathGrade < 85:
#     print("Very good in Math")
# elif mathGrade >= 85 and mathGrade < 95:
#     print("Excellent in Math")
# elif mathGrade >= 95 and mathGrade <= 100:
#     print("Excellent high in Math")
# else:
#     print("Enter a valid mark between 0 and 100")

# overall = (arabicGrade+endlishGrade+mathGrade) / 3

# if overall > 0 and overall < 50:
#     print("Overall grade is : Fail")
# elif overall >= 50 and overall < 65:
#     print("Overall grade is : Pass")
# elif overall >= 65 and overall < 75:
#     print("Overall grade is : Good")
# elif overall >= 75 and overall < 85:
#     print("Overall grade is : Very good")
# elif overall >= 85 and overall < 95:
#     print("Overall grade is : Excellent")
# elif overall >= 95 and overall <= 100:
#     print("Overall grade is : Excellent high")
# else:
#     print("overall grade is incorrect")

##########################################################