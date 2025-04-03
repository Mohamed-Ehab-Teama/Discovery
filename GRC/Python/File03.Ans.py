# 1
# Python Program to print star pattern
'''
*
* *
* * *
* * * *
* * * * *
'''
# define a Function
def star_pattern1(n):
    # Use outer for loop for rows

    for i in range(1, n+1):

        # Use inner for loop for columns / stars

        for j in range(1, i + 1):
            # print stars in each row
            print("* ", end="")

        # End of line after each row
        print()

n = int(input("Enter number of rows:"))
star_pattern1(n)


# ----

n = int(input("Enter Rows number: "))
for i in range(1, n+1 ):
    for j in range(1, i+1) :
        print( "* ", end='' )
    print()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# 2
# Python Program to print star pattern 2
'''

* * * * *
* * * *
* * *
* *
*

'''
# define a function to print star shape
def star_pattern2(n):
    # Use outer for loop for rows

    for i in range(n, 0, -1 ):

        # Use inner for loop for columns / stars

        for j in range(1, i + 1):
            # print stars in each row
            print("* ", end="")

        # End of line after each row
        print()

n = int(input("Enter number of rows:"))
star_pattern2(n)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# 3
# Python Program to print star Triangle pattern 3
'''
     Enter number of rows:5
     *
    **
   ***
  ****
 *****

'''

# define a function to print star shape
def star_pattern3(n):
    # Use outer for loop for rows
    spaces = n
    for i in range(1, n + 1):

        # Use inner for loop 1  for spaces before stars

        for j in range(1, spaces + 1):
            # print spaces
            print(" ", end="")
        # Use inner for loop 2  for columns / stars

        for k in range(1, i + 1):
            # print stars in each row
            print("*", end="")

        # End of line after each row
        print()
        # decrease spaces
        spaces = spaces - 1


n = int(input("Enter number of rows:"))
star_pattern3(n)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# 4
# Python Program to print star Triangle pattern 4
'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 

'''


# define a function to print star shape
def star_pattern4(n):
    # Use outer for loop for rows
    spaces = n
    for i in range(1, n + 1):

        # Use inner for loop 1  for spaces before stars

        for j in range(1, spaces + 1):
            # print spaces
            print(" ", end="")
        # Use inner for loop 2  for columns / stars

        for k in range(1, i + 1):
            # print stars in each row
            print("* ", end="")

        # End of line after each row
        print()
        # decrease spaces
        spaces = spaces - 1


n = int(input("Enter number of rows:"))
star_pattern4(n)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# 5
# Python Program to Print Filled Square Star Pattern 6
'''
Please Enter any Side of a Square  : 5
Filled Square Star Pattern
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 


'''
side = int(input("Please Enter any Side of a Square  : "))

print("Filled Square Star Pattern")
for i in range(side):
    for j in range(side):
        print('*', end = ' ')

    print()

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# 6
# Python Star Pattern Printing Program 8
'''
Enter number of rows:5
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

rows = int(input("Enter number of rows:"))
for i in range(1, rows+1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print()

for i in range(rows, 1, -1):
    for j in range(1, i):
        print("*", end=' ')
    print()

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------