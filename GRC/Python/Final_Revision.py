# Scenario:

# You are developing a user registration system for a new social media platform called "ConnectSphere." To ensure usernames are unique, secure, and user-friendly, you need to implement a function that validates usernames based on specific rules. The platform has the following requirements for a valid username:

# The username must be between 3 and 16 characters long (inclusive).
# The username can only contain:
# Lowercase letters (a-z)
# Numbers (0-9)
# Underscores (_)
# The username must start with a letter (a-z).
# The username cannot contain consecutive underscores (e.g., user__name is invalid).
# The username cannot end with an underscore.
# Task:

# Write a function isValidUsername(username) that takes a string username as input and returns true if the username is valid according to the rules above, and false otherwise.

# Example Test Cases:

# isValidUsername("john123") → true
# isValidUsername("a") → false (too short)
# isValidUsername("toolongusername123") → false (too long)
# isValidUsername("123user") → false (starts with a number)
# isValidUsername("user_name") → true
# isValidUsername("user__name") → false (consecutive underscores)
# isValidUsername("user_") → false (ends with underscore)
# isValidUsername("user#name") → false (contains invalid character #)
# Challenge:

# Write the function in a programming language of your choice (e.g., Python, JavaScript, Java, etc.).
# Ensure the solution is efficient and handles edge cases like empty strings or null inputs.
# Optionally, provide a brief explanation of your approach.
# Bonus Question:

# How would you modify the function to also check if the username is not a reserved word (e.g., "admin", "root", "system") from a given list of reserved words?


# Solution
def isValidUsername(username):
    # Check for null or empty string
    if not username or not isinstance(username, str):
        return False
    
    # Rule 1: Check length (3 to 16 characters)
    if len(username) < 3 or len(username) > 16:
        return False
    
    # Rule 3: Must start with a letter
    if not username[0].islower():
        return False
    
    # Rule 5: Cannot end with an underscore
    if username[-1] == '_':
        return False
    
    # Rule 4: Check for consecutive underscores
    if '__' in username:
        return False
    
    # Rule 2: Check valid characters (lowercase letters, numbers, underscore)
    for char in username:
        if not (char.islower() or char.isdigit() or char == '_'):
            return False
    
    return True

# Bonus: Check against reserved words
def isValidUsernameWithReserved(username, reserved_words=None):
    if reserved_words is None:
        reserved_words = ["admin", "root", "system"]
    
    # First, check if username is valid per rules
    if not isValidUsername(username):
        return False
    
    # Check if username is a reserved word
    if username.lower() in reserved_words:
        return False
    
    return True

# Test cases
test_cases = [
    "john123",           # True
    "a",                 # False (too short)
    "toolongusername123",# False (too long)
    "123user",           # False (starts with number)
    "user_name",         # True
    "user__name",        # False (consecutive underscores)
    "user_",             # False (ends with underscore)
    "user#name",         # False (invalid character)
    "admin"              # False (reserved word, if using bonus function)
]

for test in test_cases:
    print(f"Username: {test} -> {isValidUsername(test)}")
    
    
# # ---------===============-----------------=====================
# # ---------===============-----------------=====================
# # ---------===============-----------------=====================
# # ---------===============-----------------=====================
# # ---------===============-----------------=====================


# Problem 02
# Scenario:

# You are developing a user authentication system for a secure online banking app called "SafeVault." To ensure user accounts are protected, you need to implement a function that validates passwords based on specific security requirements. The app has the following rules for a valid password:

# The password must be between 8 and 20 characters long (inclusive).
# The password must contain at least:
    # One uppercase letter (A-Z)
    # One lowercase letter (a-z)
    # One digit (0-9)
    # One special character from the set: !@#$%^&*
# The password cannot contain spaces.
# The password cannot have three or more consecutive identical characters (e.g., aaa or 111 is invalid).
# The password cannot start or end with a special character (!@#$%^&*).
# Task:

# Write a function isValidPassword(password) that takes a string password as input and returns true if the password meets all the rules above, and false otherwise.

# Example Test Cases:

# isValidPassword("Secure123!") → true
# isValidPassword("pass") → false (too short)
# isValidPassword("ThisIsAVeryLongPassword123!") → false (too long)
# isValidPassword("NoDigitsHere!") → false (no digit)
# isValidPassword("NoSpecial123") → false (no special character)
# isValidPassword("Pass word123!") → false (contains space)
# isValidPassword("Pass111!word") → false (three consecutive identical characters)
# isValidPassword("!Password123") → false (starts with special character)
# isValidPassword("Password123@") → false (ends with special character)
# Challenge:

# Write the function in a programming language of your choice (e.g., Python, JavaScript, Java, etc.).
# Ensure the solution is efficient and handles edge cases like empty strings or null inputs.
# Optionally, provide a brief explanation of your approach.
# Bonus Question:

# How would you modify the function to also check if the password contains the user’s username (or part of it) to prevent weak passwords like John123!john?


# Solution 

def isValidPassword(password):
    # Check for null or empty string
    if not password or not isinstance(password, str):
        return False
    
    # Rule 1: Check length (8 to 20 characters)
    if len(password) < 8 or len(password) > 20:
        return False
    
    # Rule 3: No spaces allowed
    if ' ' in password:
        return False
    
    # Rule 5: Cannot start or end with a special character
    special_chars = set('!@#$%^&*')
    if password[0] in special_chars or password[-1] in special_chars:
        return False
    
    # Rule 4: Check for three or more consecutive identical characters
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return False
    
    # Rule 2: Check for required character types
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    return has_upper and has_lower and has_digit and has_special

# Bonus: Check if password contains username
def isValidPasswordWithUsernameCheck(password, username):
    # First, check if password is valid per rules
    if not isValidPassword(password):
        return False
    
    # Check if username is provided and not empty
    if not username or not isinstance(username, str):
        return True  # No username to check against, so pass
    
    # Rule: Password cannot contain username (case-insensitive)
    if username.lower() in password.lower():
        return False
    
    return True

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("Secure123!", True),
        ("pass", False),  # Too short
        ("ThisIsAVeryLongPassword123!", False),  # Too long
        ("NoDigitsHere!", False),  # No digit
        ("NoSpecial123", False),  # No special character
        ("Pass word123!", False),  # Contains space
        ("Pass111!word", False),  # Three consecutive identical characters
        ("!Password123", False),  # Starts with special character
        ("Password123@", False),  # Ends with special character
    ]

    for password, expected in test_cases:
        result = isValidPassword(password)
        print(f"Password: {password} -> {result} (Expected: {expected})")

    # Bonus test
    print("\nBonus Tests:")
    print(isValidPasswordWithUsernameCheck("John123!john", "john"))  # False (contains username)
    print(isValidPasswordWithUsernameCheck("Secure123!", "john"))  # True (valid and no username)
    
    
# # ---------===============-----------------=====================
# # ---------===============-----------------=====================
# # ---------===============-----------------=====================
# # ---------===============-----------------=====================
# # ---------===============-----------------=====================

# Problem 03

# Scenario:

# You are developing an online ordering system for a pizzeria called "PizzaPalace." Customers can choose a pizza by selecting its size, crust type, and toppings. Each choice affects the final cost, and prices are stored in dictionaries for easy lookup. Your task is to create a function that calculates the total cost of a pizza order based on the customer’s selections.

# Requirements:

# The function takes a dictionary representing a pizza order with:
# size: String (e.g., "small", "medium", "large")
# crust: String (e.g., "thin", "regular", "stuffed")
# toppings: List of strings (e.g., ["pepperoni", "mushrooms"])
# Pricing is stored in dictionaries:
# Size prices (base price in USD):
    # "small": $8.00
    # "medium": $12.00
    # "large": $16.00
# Crust prices (additional cost in USD):
    # "thin": $0.00
    # "regular": $1.00
    # "stuffed": $3.00
# Topping prices (per topping in USD):
    # "pepperoni": $1.50
    # "mushrooms": $1.00
    # "onions": $0.75
    # "extra cheese": $2.00
    # Any other topping: $1.25 (default price)
# The function calculates the total cost by summing:
# Base price for the size
# Additional cost for the crust
# Cost of all toppings
# Input validation:
    # size must be one of "small", "medium", "large".
    # crust must be one of "thin", "regular", "stuffed".
    # toppings must be a list of strings (can be empty).
# If any input is invalid (e.g., wrong size, non-string topping, null inputs), return -1.
# Round the final cost to 2 decimal places.
# The topping list cannot contain duplicates (e.g., ["pepperoni", "pepperoni"] is invalid).
# Task:

# Write a function calculatePizzaCost(order) that takes a dictionary order and returns the total cost (float) of the pizza. If the input is invalid, return -1.

# Example Test Cases:

# Input: {"size": "medium", "crust": "regular", "toppings": ["pepperoni", "mushrooms"]}
# Output: 15.50 ($12.00 + $1.00 + $1.50 + $1.00 = $15.50)
# Input: {"size": "small", "crust": "thin", "toppings": []}
# Output: 8.00 ($8.00 + $0.00 + $0.00 = $8.00)
# Input: {"size": "large", "crust": "stuffed", "toppings": ["extra cheese", "olives"]}
# Output: 22.25 ($16.00 + $3.00 + $2.00 + $1.25 = $22.25)
# Input: {"size": "xlarge", "crust": "regular", "toppings": ["onions"]}
# Output: -1 (invalid size)
# Input: {"size": "medium", "crust": "regular", "toppings": ["pepperoni", "pepperoni"]}
# Output: -1 (duplicate toppings)
# Input: {"size": "medium", "crust": "deep", "toppings": ["mushrooms"]}
# Output: -1 (invalid crust)
# Input: {"size": "small", "crust": "thin", "toppings": [123]}
# Output: -1 (non-string topping)
# Bonus Question:

# How would you modify the function to apply a discount (e.g., 10% off) if the order includes three or more toppings?


# Solution:
def calculatePizzaCost(order):
    # Pricing dictionaries
    size_prices = {
        "small": 8.00,
        "medium": 12.00,
        "large": 16.00
    }
    crust_prices = {
        "thin": 0.00,
        "regular": 1.00,
        "stuffed": 3.00
    }
    topping_prices = {
        "pepperoni": 1.50,
        "mushrooms": 1.00,
        "onions": 0.75,
        "extra cheese": 2.00
    }
    default_topping_price = 1.25
    
    # Validate input is a dictionary
    if not isinstance(order, dict):
        return -1
    
    # Validate required keys
    if not all(key in order for key in ["size", "crust", "toppings"]):
        return -1
    
    # Extract order details
    size = order["size"]
    crust = order["crust"]
    toppings = order["toppings"]
    
    # Rule 4: Validate size
    if size not in size_prices:
        return -1
    
    # Rule 4: Validate crust
    if crust not in crust_prices:
        return -1
    
    # Rule 4: Validate toppings is a list
    # if current_date > cutoff_date:
    #     return -1
    
    # Rule 4: Validate each topping is a string
    for topping in toppings:
        if not isinstance(topping, str):
            return -1
    
    # Rule 6: Check for duplicate toppings
    if len(toppings) != len(set(toppings)):
        return -1
    
    # Calculate cost
    total_cost = size_prices[size] + crust_prices[crust]
    
    # Add topping costs
    for topping in toppings:
        total_cost += topping_prices.get(topping, default_topping_price)
    
    # Rule 5: Round to 2 decimal places
    return round(total_cost, 2)

# Bonus: Apply discount for 3+ toppings
def calculatePizzaCostWithDiscount(order, discount_percent=10):
    # Calculate base cost
    base_cost = calculatePizzaCost(order)
    
    # If base_cost is -1, input is invalid
    if base_cost == -1:
        return -1
    
    # Apply discount if 3 or more toppings
    if len(order.get("toppings", [])) >= 3:
        discount = base_cost * (discount_percent / 100)
        return round(base_cost - discount, 2)
    
    return base_cost

# Test cases
if __name__ == "__main__":
    test_cases = [
        (
            {"size": "medium", "crust": "regular", "toppings": ["pepperoni", "mushrooms"]},
            15.50
        ),
        (
            {"size": "small", "crust": "thin", "toppings": []},
            8.00
        ),
        (
            {"size": "large", "crust": "stuffed", "toppings": ["extra cheese", "olives"]},
            22.25
        ),
        (
            {"size": "xlarge", "crust": "regular", "toppings": ["onions"]},
            -1
        ),
        (
            {"size": "medium", "crust": "regular", "toppings": ["pepperoni", "pepperoni"]},
            -1
        ),
        (
            {"size": "medium", "crust": "deep", "toppings": ["mushrooms"]},
            -1
        ),
        (
            {"size": "small", "crust": "thin", "toppings": [123]},
            -1
        )
    ]

    for order, expected in test_cases:
        result = calculatePizzaCost(order)
        print(f"Order: {order}")
        print(f"Cost: {result} (Expected: {expected})")

    # Bonus test
    print("\nBonus Tests:")
    bonus_order = {"size": "large", "crust": "regular", "toppings": ["pepperoni", "mushrooms", "onions"]}
    print(f"Order with 3 toppings: {bonus_order}")
    print(f"Cost with 10% discount: {calculatePizzaCostWithDiscount(bonus_order)}")  # Should be 19.35 (21.50 - 10%)