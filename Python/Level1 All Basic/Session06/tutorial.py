# Lists
    # Lists are used to store multiple items in a single variable
    # List items are ordered, changeable, and allow duplicate values
    
# To create list:
    # my_list = ["apple", "banana", "cherry"]
    
# List items can be of any data type
    # list1 = ["apple", "banana", "cherry"]
    # list2 = [1, 5, 7, 9, 3]
    # list3 = [True, False, False]

# A list can contain different data types
    # my_list = ["apple", 200, True]
    
# List Length: To determine how many items a list has:
    # len()
    # print( len(my_list) )
    
# type() => to get the type of any variable
    # print( type(my_list) )

# Access Items: List items are indexed and you can access them by referring to the index number:
    # print( my_list[0] )
    # print( my_list[1] )
    # print( my_list[-1] )
    # print( my_list[-2] )
    
    # print( my_list[2:5] )
    # print( my_list[:5] )
    # print( my_list[2:] )
    # print( my_list[:] )
    # print( my_list[1:6:1] )
    # print( my_list[::1] )
    # print( my_list[1:6:-1] )
    # print( my_list[::-1] )
    
# Change List Items:
    # my_list[0] = 'Ali'
    # my_list[3] = 201
    # my_list[1:3] = ["Ali", "Mai"]
    
# Add List Items:
    # append() => add an item to the end of the list
    # insert() => inserts an item at the specified index

# Remove List Items: 
    # remove() => removes the specified item
    # pop() => removes the specified index
    
# Clear the list:
    # clear() => empties the list
    # my_list.clear()
    
# ------------------------------------------------------

# Tuples:
    # Tuples are used to store multiple items in a single variable

    # Tuple items are ordered, unchangeable, and allow duplicate values
    
# Create a Tuple:
    # thistuple = ("apple", "banana", "cherry")
    # print(thistuple)
    
# To determine how many items a tuple has, use the len() function
# You can access tuple items by referring to the index number


# If you want to change Tuple values:
    # Convert it to list and then add or change items then convert it back to tuple:
        # x = ("apple", "banana", "cherry")
        # y = list(x)
        # y[1] = "kiwi"
        # x = tuple(y)
        # print(x)

# ------------------------------------------------------

# Set
    # Sets are used to store multiple items in a single variable.
    
    # Set items can be of any data type
    
    # Set items are unordered, unchangeable, and do not allow duplicate values.
    
    # Set items are unchangeable, but you can remove items and add new items.
    
    # Sets are unordered, so you cannot be sure in which order the items will appear.
    
    # The values True and 1 are considered the same value in sets, and are treated as duplicates
    # The values False and 0 are considered the same value in sets, and are treated as duplicates:
    

# Get the Length of a Set:
    # len():
        # print( len( my_set ) )
        
        
# Access Set Items:
    # You cannot access items in a set by referring to an index or a key.
    # But you can loop through the set items using a for loop
        # thisset = {"apple", "banana", "cherry"}
        # for x in thisset:
        #   print(x)

        # print("banana" in thisset) => Check if "banana" is present in the set
        # print("banana" not in thisset) => Check if "banana" is not present in the set
