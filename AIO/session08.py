# 1 - Write a function to check if a string is palindrome python
def is_palindrome(str):
    return str == str[::-1]


# 2 - Write a function to check if a substring exists within a given string
def contains_substring(str , substring):
    return substring in str


# 3 - Write a function that counts the number of uppercase and lowercase letters in a string
def count_case(str):
    upper_count = sum( 1 for char in str if char.isupper() )
    lower_count = sum( 1 for char in str if char.islower() )
    return upper_count, lower_count


# 4 - Write a function that removes all digits from a string.
def remove_digits( str ):
    return ''.join( char for char in str if not char.isdigit() )


# 5 - Write a function that capitalizes the first letter of every word in a string
def capitalize_words(s):
    return s.title()


# 6 - Write a function to count how many times each character appears in a string.
def char_repeat(str):
    repeat = {}
    for char in str:
        repeat[char] = repeat.get(char, 0) + 1
    return repeat


