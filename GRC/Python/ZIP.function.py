# Syntax of zip()
    # zip(*iterables)
    # Returns an iterator of tuples, where each tuple contains elements from the input iterables at the same index. 
    # If the input iterables are of unequal length then zip() stops creating tuples when the shortest iterable is exhausted.
    
    # Key Points:
        # If no parameters are passed, zip() returns an empty iterator.
        # If only one iterable is passed, the result will be a series of single-element tuples.
        # If multiple iterables are passed, each tuple will contain one element from each iterable.
        
a = [1, 2, 3]
b = ['a', 'b', 'c']

# No iterable are passed
res = zip()

# Converting iterator to list
print(list(res))                # []

# One iterable is passed
res = zip(a)

# Converting iterator to list
print(list(res))                # [(1,), (2,), (3,)]

# Two iterables are passed
res = zip(a, b)

# Converting iterator to list
print(list(res))                # [(1, 'a'), (2, 'b'), (3, 'c')]


# =========================

names = ['Alice', 'Bob', 'Charlie']
scores = [88, 94]  

res = zip(names, scores)
print(list(res))                # [('Alice', 88), ('Bob', 94)]

# =========================

a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]

fruits, quantities = zip(*a)

print(f"Fruits: {fruits}")                  # Fruits: ('Apple', 'Banana', 'Orange')
print(f"Quantities: {quantities}")          # Quantities: (10, 20, 30)

# =========================

d = {'name': 'Alice', 'age': 25, 'grade': 'A'}

keys = d.keys()
values = d.values()

res = zip(keys, values)
print(list(res))                # [('name', 'Alice'), ('age', 25), ('grade', 'A')]

# =========================

