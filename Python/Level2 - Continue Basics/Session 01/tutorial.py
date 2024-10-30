# Strings => Sequence of characters
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
    # 'Hello'   -   "Hello"
    
# Quotes Inside Quotes
    # print("He is called 'Johnny' ")
    # print('He is called "Johnny" ')
    
# Creating strings:
    # name = 'Mohamed'
    
# Multiline Strings:
        # str = """Lorem ipsum dolor sit amet,
        # consectetur adipiscing elit,
        # sed do eiusmod tempor incididunt
        # ut labore et dolore magna aliqua."""
    # or
        # a = '''Lorem ipsum dolor sit amet,
        # consectetur adipiscing elit,
        # sed do eiusmod tempor incididunt
        # ut labore et dolore magna aliqua.'''
        
# Accessing characters in a string:
    # messgae = "Hello, World"
    # print ( message[0] )
    
# String Methods:
    # capitalize() : Upper case the first letter in this sentence
    # upper() : Upper case the string
    # lower() : Lower case the string
    
    
    # split() : splits a string into a list.
        # string.split(separator(optional), maxsplit(optional))


    # join() : takes all items in an iterable and joins them into one string [A string must be specified as the separator]
        # string.join(iterable)
            # EX)
            # str = "__".join( ('Ahmed', 'Mohamed', 'Ali') )
            # print (str)


    # strip() : removes any leading, and trailing whitespaces.
        # string.strip(characters)
            # EX)
            # txt = "     banana     "
            # x = txt.strip()
            
            # txt = ",,,,,rrttgg.....banana....rrr"
            # x = txt.strip(",.grt")
            
            
    # count() : returns the number of times a specified value appears in the string.
        # string.count( value(Required), start(Optional), end(Optional) )
            # txt = "I love apples, apple are my favorite fruit"
            # x = txt.count("apple", 10, 24)
            
            
    # startswith() : returns True if the string starts with the specified value, otherwise False.
        # string.startswith(value, start, end)
            # x = txt.startswith("Hello")
    # endswith() : returns True if the string ends with the specified value, otherwise False
        # string.endswith(value, start, end)
            # x = txt.endswith("my world.")
            
    
    # find() : finds the first occurrence of the specified value. [ returns -1 if the value is not found ]
        # string.find(value, start, end)
            # x = txt.find("welcome")
    # index() : finds the first occurrence of the specified value. [ raises an exception if the value is not found ]
        # string.index(value, start, end)
            # x = txt.index("e")
            
            
# In Python: we cannot combine strings and numbers like this:
        # print ( 'I am ' + 35 )   => Error
        
        # age = 32
        # print ('I am age years old')        =>  I am age years old
        
# F-Strings:
    # put an f in front of the string - add curly brackets {} as placeholders for variables and other operations.

        # age = 36
        # txt = f"My name is John, I am {age}"
        
        # price = 59
        # txt = f"The price is {price} dollars"
        
        # txt = f"The price is {20 * 59} dollars"