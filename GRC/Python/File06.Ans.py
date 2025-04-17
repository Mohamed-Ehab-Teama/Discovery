# Problem 1: Library Book Management
# Scenario:
    # You’re building a system to track library books. Users can borrow/return books, and the program should prevent double-borrowing.

    # Tasks:
        # Add/remove books.
        # Borrow/return books (check availability).
        # Print the current status.
       
 
# Input
    # add_book("Python 101")
    # add_book("Algorithms")
    # borrow_book("Python 101")
    # borrow_book("Algorithms")
    # return_book("Python 101")
    # print_status()

# Output:
    # Available: ['Python 101'], Borrowed: ['Algorithms']
    

# Solution:
library = {"available": [], "borrowed": []}

def add_book(title):
    if title not in library["available"] and title not in library["borrowed"]:
        library["available"].append(title)
    else:
        print(f"{title} already exists!")

def borrow_book(title):
    if title in library["available"]:
        library["available"].remove(title)
        library["borrowed"].append(title)
    else:
        print(f"{title} not available!")

def return_book(title):
    if title in library["borrowed"]:
        library["borrowed"].remove(title)
        library["available"].append(title)
    else:
        print(f"{title} wasn't borrowed!")

def print_status():
    print(f"Available: {library['available']}, Borrowed: {library['borrowed']}")

# Test
add_book("Python 101")
add_book("Algorithms")
borrow_book("Python 101")
borrow_book("Algorithms")
return_book("Python 101")
print_status()

# =========================     ==============================      ==============================


# Problem 2: Food Delivery Time Estimator
# Scenario:
    # A food app estimates delivery time based on distance (1 min per 100m) and prep time (5 mins per item).

    # Tasks:
        # Calculate total time given distance (meters) and items.
        # Handle edge cases (e.g., zero distance).

    # Sample Input/Output:
        # Input
        # print(estimate_time(500, 3))  # Output: 20 (5*3 + 500/100)


# Solution:

def estimate_time(distance, items):
    if distance < 0 or items < 0:
        return "Invalid input"
    prep_time = items * 5
    travel_time = distance / 100
    total_time = prep_time + travel_time
    return int(total_time) if total_time.is_integer() else total_time

# Test cases
print(estimate_time(500, 3))  # 20
print(estimate_time(0, 2))    # 10
print(estimate_time(150, 0))  # 1.5

# =========================     ==============================      ==============================


# Problem 3: Password Strength Checker
# Scenario:
    # Validate passwords: at least 8 chars, 1 uppercase, 1 number, and 1 symbol (!@#$).

    # Sample Input/Output:
    # Input
        # check_password("Py@2024")  # Output: "Strong"
        # check_password("python")    # Output: "Weak: Add a symbol, number, and uppercase letter"



# Solution:

def check_password(password):
    errors = []
    if len(password) < 8:
        errors.append("at least 8 characters")
    if not any(c.isupper() for c in password):
        errors.append("an uppercase letter")
    if not any(c.isdigit() for c in password):
        errors.append("a number")
    if not any(c in "!@#$" for c in password):
        errors.append("a symbol (!@#$)")
    
    if not errors:
        return "Strong"
    else:
        return f"Weak: Add {', '.join(errors)}"

# Test
print(check_password("Py@2024"))  # Strong
print(check_password("python"))   # Weak

# =========================     ==============================      ==============================


# Problem 4: Smart Thermostat
# Scenario:
    # A thermostat adjusts temperature based on time of day:
        # Morning (6-12): 22°C
        # Afternoon (12-18): 24°C
        # Night (18-6): 20°C
        
    # Tasks:
        # Take current hour (0-23) and return target temperature.
        # Handle invalid input.

# Solution:

def set_thermostat(hour):
    if not 0 <= hour <= 23:
        return "Invalid hour"
    if 6 <= hour < 12:
        return 22
    elif 12 <= hour < 18:
        return 24
    else:
        return 20

# Test
print(set_thermostat(9))   # 22
print(set_thermostat(15))  # 24
print(set_thermostat(23))  # 20

# =========================     ==============================      ==============================


# Problem 5: Event Scheduler Conflict Checker
# Scenario:
    # Check if two events overlap given their start/end times (24h format).

    # Sample Input/Output:
    # Input
        # check_conflict("14:00", "16:00", "15:00", "17:00")  # Output: "Conflict!"
        
# Solution:

def time_to_minutes(time):
    hh, mm = map(int, time.split(':'))
    return hh * 60 + mm

def check_conflict(start1, end1, start2, end2):
    s1 = time_to_minutes(start1)
    e1 = time_to_minutes(end1)
    s2 = time_to_minutes(start2)
    e2 = time_to_minutes(end2)
    
    if (s1 < e2) and (s2 < e1):
        return "Conflict!"
    else:
        return "No conflict"

# Test
print(check_conflict("14:00", "16:00", "15:00", "17:00"))  # Conflict!
print(check_conflict("09:00", "10:00", "10:00", "11:00"))  # No conflict