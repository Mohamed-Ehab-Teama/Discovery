# operators:


# + - * / ** //             Arithmatic Operators
# > < >= <= == !=           Comparison Operators
# and or not                Logic Operators


# x = 11
# y = 15
# if ( x > 10 and y > 10 ):
#     print ("great")

# x = 11
# y = 1
# if ( x > 10 or y > 10 ):
#     print ("great")

# x = 0
# print (not x)


#################################################################################

# If Statement

# if (10 > 50):
#     print ('10 is greater than 5')


# if (10 > 50):
#     print ('10 is greater than 5')
# else:
#     print ('10 is less than 50')


# x = 50

# if (x > 50):
#     print ('10 is greater than 50')
# elif (x < 50):
#     print ('10 is less than 50')
# else:
#     print ('10 is equal to 50')


#################################################################################


number1 = int(input("Enter the First number: \n"))
number2 = int(input("Enter the Second number: \n"))
operator = input("Enter the Operation operator [ + , - , * , / , // , ** ] ")

if operator == "+":
    print(number1, " + ", number2, " = ", number1 + number2, "\n")
elif operator == "-":
    print(number1, " - ", number2, " = ", number1 - number2, "\n")
elif operator == "*":
    print(number1, " * ", number2, " = ", number1 * number2, "\n")
elif operator == "/":
    print(number1, " / ", number2, " = ", number1 / number2, "\n")
elif operator == "//":
    print(number1, " Floor Division ", number2, " = ", number1 // number2, "\n")
elif operator == "**":
    print(number1, " Power ", number2, " = ", number1**number2, "\n")
