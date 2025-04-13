# Given an integer n, find whether the number is Palindrome or not. 
# A number is a Palindrome if it remains the same when its digits are reversed.

# Examples:
    # Input: n = 12321
    # Output: Yes
    # Explanation: 12321 is a Palindrome number because after reversing its digits, the number becomes 12321 which is the same as the original number.

    # Input: n = 1234
    # Output: No
    # Explanation: 1234 is not a Palindrome number because after reversing its digits, the number becomes 4321 which is different from the original number.
    
    
    
# Method 01
def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

# Example usage
print(is_palindrome(121))  # Output: True
print(is_palindrome(123))  # Output: False


# Method 02
def is_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return original_num == reversed_num

# Example usage
print(is_palindrome(121))  # Output: True
print(is_palindrome(123))  # Output: False




# ---------==============------------=============----------------