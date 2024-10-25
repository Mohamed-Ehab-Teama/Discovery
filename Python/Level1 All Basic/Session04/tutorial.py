# While loop
    # Continue
    # Break
# Range
    # range(start, stop, step)

# ---------------------------------

# i = 0
# while i < 10 :
#     print( i )
#     i += 1
    
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     else:
#         print (i)
    
# while i < 10:
#     i += 1
#     if i == 5:
#         break
#     else:
#         print (i)

# ---------------------------------

# r = range(6)
# r = range(5,10)
# r = range(3, 20, 4)

# for i in r :
#     print (i)

# ---------------------------------

# Q) Sum of Natural Numbers
# Write a program that uses a while loop to calculate the sum of the first 𝑁 (N natural numbers)
# Input: N (integer)
# Example: Input: N = 5  -> Output: Sum = 15

# Ans)
# n = int(input('Enter Your Number: '))
# i = 0
# sum = 0
# while i <= n : 
#     sum += i
#     i += 1
# print(' The sum is : ', sum)

# ------------------

# Q) Count Even Numbers in a Range
# Use the range() function and a while loop to count how many even numbers are there between two integers, start and end (inclusive).
# Input: start and end (integers)
# Example: Input: start = 3, end = 10  &  Output: Count = 4 (even numbers are 4, 6, 8, 10)

# Ans)
# start = int( input('Enter Start Number \n') )
# end = int( input('Enter End Number \n') )

# x = range( start, end)
# i = start
# count_even = 0
# while i <= end :
#     if i % 2 == 0 :
#         count_even += 1
#     i += 1
    
# print(" The Count of even numbers is : ", count_even)

# ------------------

