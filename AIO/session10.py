

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# Dictionary
    # store data values in key:value pairs
    # ordered*, changeable and do not allow duplicates
            # thisdict = {
            #     "brand": "Ford",
            #     "model": "Mustang",
            #     "year": 1964
            # }
            
    # ordered, changeable, and do not allow duplicates.
        
        
    # As of Python version 3.7, dictionaries are ordered. 
    # In Python 3.6 and earlier, dictionaries are unordered.


    # Duplicates Not Allowed : Duplicate values will overwrite existing values.
            # thisdict = {
            #     "brand": "Ford",
            #     "model": "Mustang",
            #     "year": 1964,
            #     "year": 2020
            # }
            # print(thisdict)
            
            
            
    # Dictionary Length : len()
        # print(len(thisdict))
        
        
    # dict() Constructor
        # thisdict = dict(name = "John", age = 36, country = "Norway")

# ---------------------------------------------------------
    # Accessing Items
        # You can access the items of a dictionary by referring to its key name, inside square brackets
            # print ( thisdict["model"] )
        
        # get()
            # print ( thisdict.get("model") )
            
            
            
            
    # Get Keys : 
        # keys() method will return a list of all the keys in the dictionary.
            # print ( thisdict.keys() )
            
    
    # Get Values
        # The values() method will return a list of all the values in the dictionary.
            # print ( thisdict.values() )
            
    
    # Get Items
        # The items() method will return each item in a dictionary, as tuples in a list.
            # print ( thisdict.items() )
        
        
        
    # Check if Key Exists:
        # if "model" in thisdict:
        #   print("Yes, 'model' is one of the keys in the thisdict dictionary")
        
# ---------------------------------------------------------
    # Change Values
        # by referring to its key name:
            # thisdict["year"] = 2018
            
        # Update Dictionary
            # thisdict.update( {"year": 2020} )
    

# ---------------------------------------------------------
    # Adding Items
        # using a new index key and assigning a value to it:
            # thisdict["Color"] = 'red'
            
        # Update method:
            # thisdict.update({"color": "red"})


# ---------------------------------------------------------
    # Removing Items:
        # pop() method : removes the item with the specified key name: (Must take the kay to remove)
            # thisdict.pop("model")
            
        # popitem() method removes the last inserted item : (in versions before 3.7, a random item is removed instead):
            # thisdict.popitem()
            
        # del keyword : removes the item with the specified key name:
            # del thisdict["model"]
            # del thisdict      =>  delete the dictionary completely
    
        # clear() method : empties the dictionary
            # thisdict.clear()

# ---------------------------------------------------------
    # Loop Through a Dictionary:
        # For:
            # for x in thisdict:
                # print(x)              =>  Print all key names in the dictionary
                # print(thisdict[x])    =>  Print all Values in the dictionary
                
            # for x in thisdict.keys():
                # print(x)
                
            # for x in thisdict.values():
                # print(x)
                
            # for x, y in thisdict.items():
                # print(x, y)
# ---------------------------------------------------------
    # Copy a Dictionary:
        # mydict = thisdict.copy()
        
    # dict() function:
        # mydict = dict(thisdict)
        
    
        # Note:
            # dict2 = dict1 : You cannot copy a dictionary simply by typing dict2 = dict1
            # because: dict2 will only be a reference to dict1, 
            # and changes made in dict1 will automatically also be made in dict2

# ---------------------------------------------------------
    # Dictionary Methods:
        # clear()	        Removes all the elements from the dictionary
        # copy()	        Returns a copy of the dictionary
        # get()	            Returns the value of the specified key
        # items()	        Returns a list containing a tuple for each key value pair
        # keys()	        Returns a list containing the dictionary's keys
        # pop()	            Removes the element with the specified key
        # popitem()	        Removes the last inserted key-value pair
        # update()	        Updates the dictionary with the specified key-value pairs
        # values()	        Returns a list of all the values in the dictionary

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# Sets:
    # thisset = {"apple", "banana", "cherry"}

    # unordered, unchangeable, and unindexed
    
    # Set items are unchangeable, but you can remove items and add new items.
        # Sets are unordered, so you cannot be sure in which order the items will appear.
        
    # The values [True and 1] [False and 0] are considered the same value in sets, and are treated as duplicates.
    
    
    # Get the Length: len()

    # set() Constructor:
        # thisset = set(("apple", "banana", "cherry"))


# ---------------------------------------------------------
    # Access Items:
        # You cannot access items in a set by referring to an index or a key
        # But you can loop through the set items using a for loop, 
        # or ask if a specified value is present in a set, by using the in keyword
        
            # for x in thisset:
            #     print(x)
            # print("banana" in thisset)
            # print("banana" not in thisset)
        
        # Once a set is created, you cannot change its items, but you can add new items.

# ---------------------------------------------------------
    # Add Items:
        # add() method:
            # thisset.add("orange")
            
        # update() method : To add items from another set into the current set
            # thisset = {"apple", "banana", "cherry"}
            # tropical = {"pineapple", "mango", "papaya"}
            # thisset.update(tropical)
            
        # The object in the update() method does not have to be a set, 
            # it can be any iterable object (tuples, lists, dictionaries etc.)
                # thisset = {"apple", "banana", "cherry"}
                # mylist = ["kiwi", "orange"]
                # thisset.update(mylist)               
    
    
# ---------------------------------------------------------
    # Remove Item:
        # remove() or discard() method:
            # thisset.remove("banana")
            # thisset.discard("banana")
            
            # If the item to remove does not exist: 
                # remove() will raise an error
                # discard() will NOT raise an error
                
                
        # pop() method:
            # thisset.pop()
            
            # The return value of the pop() method is the removed item
                # x = thisset.pop()
                # print(x)
                
        # clear() method : empties the set
            # thisset.clear()
            
        # del keyword will delete the set completely:
            # del thisset

# ---------------------------------------------------------
    # Loop Items:
        # for x in thisset:
            # print(x)

# ---------------------------------------------------------
    # Join Sets:
        # The union() and update()      joins all items from both sets.
        # The intersection()            keeps ONLY the duplicates.
        # The difference()              keeps the items from the first set that are not in the other set(s).
        # The symmetric_difference()    keeps all items EXCEPT the duplicates.
        
            # You can use the | operator instead of the union() method
                # set3 = set1.union(set2)
                # set3 = set1 | set2
                # myset = set1.union(set2, set3, set4)
                # myset = set1 | set2 | set3 |set4
                
        # Join a Set and a Tuple:
            # x = {"a", "b", "c"}
            # y = (1, 2, 3)
            # z = x.union(y)
            # The  | operator only allows you to join sets with sets, 
            # and not with other data types like you can with the  union() method
            
        # Update:
            # set1.update(set2)
            
        # Both union() and update() will exclude any duplicate items
            
    
        # The intersection() : Keep ONLY the duplicates
            # You can use the & operator instead of the intersection() method
            
                # set3 = set1.intersection(set2)
                # set3 = set1 & set2

# ---------------------------------------------------------
    # Set Methods
    
        # add()	 	        Adds an element to the set
        # clear()	 	    Removes all the elements from the set
        # copy()	 	    Returns a copy of the set
        # discard()	 	    Remove the specified item
        # intersection()    Returns a set, that is the intersection of two other sets
        
        # isdisjoint()	 	Returns whether two sets have a intersection or not
            # isdisjoint() method returns True if none of the items are present in both sets, 
            # otherwise it returns False
                # z = x.isdisjoint(y)
                
        # issubset()		Returns whether another set contains this set or not
            # returns True if all items in the set exists in the specified set, 
            # otherwise it returns False
                # z = x.issubset(y)
        
        # issuperset()		Returns whether this set contains another set or not
            # returns True if all items in the specified set exists in the original set, 
            # otherwise it returns False
                # z = x.issuperset(y)
        
        # pop()	 	        Removes an element from the set
        # remove()	 	    Removes the specified element
        # union()		    Return a set containing the union of sets
        # update()		    Update the set with the union of this set and others

# ---------------------------------------------------------
