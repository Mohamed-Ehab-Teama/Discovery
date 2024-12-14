# newlist = [expression for item in iterable if condition == True]



# string.join(iterable)
# separator_string.join(iterable)


# dictionary.get(keyname, value)
# keyname : Required :  The keyname of the item you want to return the value from
# value : Optional. A value to return if the specified key does not exist. Default value None


# string.split(separator, maxsplit)
    # => used to split a string into a list of substrings based on a specified separator. 
    # If no separator is provided, the default separator is any whitespace
        # text.split()
        # text.split(',')
        
        

# get method
    # dictionary.get(keyname)
    # dictionary.get(keyname, value)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}


# Get the value of the "model" key
model = car.get("model")
print(model) # Output: Mustang

# Get the value of a non-existing key with a default value
price = car.get("price", 15000)
print(price) # Output: 15000

# Get the value of the "model" key
model = car.get("model", "BMW")
print(model) # Output: Mustang
