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


# 7 - Write a function to find the longest word in a sentence.
def longest_word(s):
    words = s.split()
    return max(words, key=len)


# 8 - Write a function that removes all vowels from a string.
def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)


# 9 - Write a function that replaces all spaces in a string with a specified character
def replace_spaces(s, char):
    return s.replace(" ", char)


# 10 - Write a function that finds all the words in a string that start with a specific letter.
def words_starting_with( s , letter):
    words = s.split()
    return [word for word in words if word.lower().startswith(letter.lower())]


# 11 - Write a function that checks if two strings are anagrams of each other (contain the same characters in a different order)
def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())


# 12 - Write a function to check if a string contains only unique characters (no repeated characters)
def has_unique_characters(s):
    s = s.replace(" ", "").lower()  # Remove spaces and make lowercase
    return len(s) == len(set(s))

