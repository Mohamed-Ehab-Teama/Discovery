        
    # 1. Sum of All Numbers in a List

# def sum_all_nums( numbers ):
#     return sum( numbers )

# def sum_all_nums( numbers ):
#     sum = 0
#     for i in numbers:
#         sum += i
    
#     return sum

# list = [10,20,30,40,50,60]
# print ( sum_all_nums( list ) )


# ------------------------------------------------------------

    # 2. Find the Maximum in a List

# def find_max( nums ):
#     return max( nums )

# list = [100,201,130,40,87,12]
# print ( find_max( list ) )

# ------------------------------------------------------------

    # 3. Find the minimum in a List

# def find_max( nums ):
#     return max( nums )

# list = [100,201,130,40,87,12]
# print ( find_max( list ) )


# ------------------------------------------------------------

    # 4. FizzBuzz : 
        # if the number is divisible by 3 => Fizz
        # if the number is divisible by 5 => Buzz
        # if the number is divisible by 3 and 5 => FizzBuzz


# def fizzBuzz( num ):
#     if num % 3 == 0 and num % 5 == 0 :
#         return 'FizzBuzz'
#     elif num % 3 == 0 :
#         return 'Fizz'
#     elif num % 5 == 0 :
#         return 'Buzz'        

# print ( fizzBuzz(10) )



# ------------------------------------------------------------

    # 5. Palindrome Checker
    
    
# def is_palidrom ( txt ):
#     if txt == txt[::-1]:
#         return 'Palindrom'
#     else:
#         return 'Not Palindrom'

# def is_palidrom ( txt ):
#     if txt == ''.join(reversed(txt)):
#         return 'Palindrom'
#     else:
#         return 'Not Palindrom'

# print ( is_palidrom('lolol') )



# ------------------------------------------------------------

    # 7. Reverse a String

# def revers_string( txt ):
#     return txt[::-1]

# def revers_string( txt ):
#     return ''.join(reversed(txt))
    
    
# print ( revers_string( 'Mohamed' ) )

# ------------------------------------------------------------

    # 8. Count Vowels in a String

# def count_vowels ( txt ):
#     count = 0
#     for i in txt:
#         if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or 
#             i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#             count += 1
#     return count

# def count_vowels ( txt ):
#     count = 0
#     for i in txt:
#         if i in ('aeiouAEIOU'):
#             count += 1
#     return count


# print ( count_vowels('Ahmed Mohamed Ehab') )

# ------------------------------------------------------------

    
        # Lists => are ordered, mutable collections that allow duplicate elements.
            # my_list = [1, 2, 3, 4, 5]
        # Tuples => are ordered, immutable collections that allow duplicate elements.
            # my_tuple = (1, 2, 3, 4, 5)
        # Dictionaries => are collections of key-value pairs. They are ordered, mutable, and do not allow duplicate keys
            # my_dict = {'a': 1, 'b': 2, 'c': 3}
        # Sets => are unordered collections of unique elements. They are mutable and do not allow duplicate elements.
            # my_set = {1, 2, 3, 4, 5}
            
        # mutable object can be changed after it is created
        # immutable object can’t be changed after it is created


# ------------------------------------------------------------

    # 9. Remove Duplicates from List

# def remove_duplicates (myList):
#     return list( set(myList) )

# list1 = [10,20,10,30,10,50,20,30,40,50]

# print ( remove_duplicates(list1) )

# ------------------------------------------------------------

    # 11. Factorial of a Number

# def factorial ( num ):
#     fact = 1
#     for i in range (1, num + 1):
#         fact *= i
#     return fact

# print ( factorial(6) )