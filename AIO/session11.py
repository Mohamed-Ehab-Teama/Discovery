# A function is a block of code which only runs when it is called.

# Creating a Function:
def my_function():
    print("Hello from a function")
my_function()




# Function With Arguments:
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")




# From a function's perspective:
    # A parameter is the variable listed inside the parentheses in the function definition.
    # An argument is the value that is sent to the function when it is called.
    
    
    

# Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")




# If you do not know how many arguments that will be passed into your function, 
    # add a * before the parameter name in the function definition.
    # This way the function will receive a tuple of arguments, and can access the items accordingly 
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")




# You can also send arguments with the key = value syntax.
    # This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




# If you do not know how many keyword arguments that will be passed into your function, 
    # add two asterisk: ** before the parameter name in the function definition.
    # This way the function will receive a dictionary of arguments, and can access the items accordingly
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")




# Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")




# Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)




# Return Values
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# Return VS Print in the function definition




# The pass Statement:
    # function definitions cannot be empty, 
    # but if you for some reason have a function definition with no content, 
    # put in the pass statement to avoid getting an error.
def myfunction():
    pass




