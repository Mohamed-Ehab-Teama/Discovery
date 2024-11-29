# Create a List:
# list = ["apple", "banana", "cherry"]

# List items are ordered, changeable, and allow duplicate values.

# List Length
# print(len(list))

# List items can be of any data type:

# type() : To get type of any variabel

# The list() Constructor:
# mylist = list(("apple", "banana", "cherry")) # note the double round-brackets

# ---------------------------------------------------------

# Access Items
# thislist = ["apple", "banana", "cherry"]
# print(thislist[0])
# print(thislist[1])
# print(thislist[-1])
# print(thislist[-2])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])

# print(thislist[-4:-1])
# print(thislist[-1:-4])

# ---------------------------------------------------------

# Check if Item Exists in a list
# thislist = ["apple", "banana", "cherry"]
# if "Apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# ---------------------------------------------------------

# Change list Values
# thislist[1] = "blackcurrant"
# thislist[1:3] = ["blackcurrant", "watermelon"]


# Append Items    :   To add an item to the end of the list
# hislist.append("orange")

# Insert Items    :   To insert a list item at a specified index
# thislist.insert(1, "orange")

# Extend List     :   To append elements from another (list, tuples, sets, dictionaries ) to the current list
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# ---------------------------------------------------------

# Remove Items
# The remove() method removes the specified item
# thislist.remove("banana")

# pop() method removes the specified index
# thislist.pop(1)
# thislist.pop()    => Remove the last index

# del keyword also removes the specified index
# del thislist[0]   =>  Remove specified index
# del thislist      => Remove list completly : The list is not existed anymore

# clear() method empties the list : The list still remains, but it has no content.
# thislist.clear()

# ---------------------------------------------------------

# Loop Through a List
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# Looping Using List Comprehension
    # List Comprehension offers the shortest syntax for looping through lists
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# ---------------------------------------------------------

    # List Comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]

# newlist = [x for x in fruits]
# newlist = [x for x in range(10)]
# newlist = [x.upper() for x in fruits]

# ---------------------------------------------------------

# Sort Lists:
# `sort() method that will sort the list alphanumerically, ascending, by default`

# thislist.sort()                   => Ascending
# thislist.sort(reverse = True)     => Descinding

# ---------------------------------------------------------

# Reverse Order
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# ---------------------------------------------------------

# Make a copy of a list with the copy() method
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# ---------------------------------------------------------

# Join Two Lists

    # + Operator
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

    # Extend
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

# ---------------------------------------------------------

# List Methods
# append()	        Adds an element at the end of the list
# clear()	            Removes all the elements from the list
# copy()	            Returns a copy of the list
# count()	            Returns the number of elements with the specified value
# extend()	        Add the elements of a list (or any iterable), to the end of the current list
# index()	            Returns the index of the first element with the specified value
# insert()	        Adds an element at the specified position
# pop()	            Removes the element at the specified position
# remove()	        Removes the item with the specified value
# reverse()	        Reverses the order of the list
# sort()	            Sorts the list


# x = fruits.count("cherry")
# x = fruits.index("cherry")
# x = fruits.index(32)

# ---------------------------------------------------------
# ---------------------------------------------------------