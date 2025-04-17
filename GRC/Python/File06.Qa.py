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

# =========================     ==============================      ==============================
# =========================     ==============================      ==============================
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

# =========================     ==============================      ==============================
# =========================     ==============================      ==============================
# =========================     ==============================      ==============================

# Problem 3: Password Strength Checker
# Scenario:
    # Validate passwords: at least 8 chars, 1 uppercase, 1 number, and 1 symbol (!@#$).

    # Sample Input/Output:
    # Input
        # check_password("Py@2024")  # Output: "Strong"
        # check_password("python")    # Output: "Weak: Add a symbol, number, and uppercase letter"

# =========================     ==============================      ==============================
# =========================     ==============================      ==============================
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

# =========================     ==============================      ==============================
# =========================     ==============================      ==============================
# =========================     ==============================      ==============================


# Problem 5: Event Scheduler Conflict Checker
# Scenario:
    # Check if two events overlap given their start/end times (24h format).

    # Sample Input/Output:
    # Input
        # check_conflict("14:00", "16:00", "15:00", "17:00")  # Output: "Conflict!"