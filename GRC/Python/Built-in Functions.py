# Basic I/O & Conversion

    # Print
        # print(object(s), end=end) 
            # end : Optional. Specify what to print at the end. Default is '\n' (line feed)

    # str(), int(), float(), bool()	    =>      Type conversion

    # bin(), hex(), oct()	    Convert numbers to binary, hex, or octal
    # ord(), chr()	            Character ↔ ASCII code



# -------------------------------------------------------------

# Mathematical Functions

    # abs()	                            Absolute value
    # pow(x, y), x**y	                Power calculation
    # round(), sum(), max(), min()	    Aggregation functions
    # divmod(a, b)	                    quotient & remainder

# -------------------------------------------------------------

# Data Structure Operations

    # len()	                        Returns length

    # sorted(), reversed()	        Sorting & reversing
        # sorted(iterable, key=key, reverse=reverse)
        # reversed(sequence)

    # enumerate()	                Iterate with index
        # enumerate(iterable, start=0)
        # for index, value in enumerate(itrable)

    # zip()	                        Combine multiple iterables
        # zip(iterator1, iterator2, iterator3 ...)
        # Use tuple to print it in a pretty format

# -------------------------------------------------------------

# Functional Programming

    # map(), filter()        Apply functions to sequences
        # map(function, iterables)
            # def myfunc(n):
            #     return len(n)
            # x = map(myfunc, ('apple', 'banana', 'cherry'))
            
        # filter(function, iterable)
            # ages = [5, 12, 17, 18, 24, 32]

            # def myFunc(x):
            #     if x < 18:
            #         return False
            #     else:
            #         return True
            # adults = filter(myFunc, ages)
            # for x in adults:
            # print(x)
        

# -------------------------------------------------------------

# Boolean aggregation

    # all()
        # The all() function returns True if all items in an iterable are true, otherwise it returns False.
        # If the iterable object is empty, the all() function also returns True.
        # all(iterable)

    # any()
        # The any() function returns True if any item in an iterable are true, otherwise it returns False.
        # If the iterable object is empty, the any() function will return False.
        # any(iterable)

# -------------------------------------------------------------

# Type Checking

# type() => return the data type of a value
    # type( value ) 

# isinstance() => returns True if the specified object is of the specified type, otherwise False.
    # isinstance(object, type)
    # x = isinstance(5, int)
    # x = isinstance("Hello", (float, int, str, list, dict, tuple))
    
# -------------------------------------------------------------
