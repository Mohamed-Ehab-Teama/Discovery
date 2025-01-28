# HiGeen
def hiGeen(T, A, B, C):
    if T < A:
        return "Y"
    T -= A
    if T < B:
        return "A"
    T -= B 
    if T < C:
        return "O"
    return "H"

# Input
T, A, B, C = map(int, input().split())
print(hiGeen(T, A, B, C))

# -----------------------------------------------------------------

# Reverse Array
def reverse_array(arr):
    return arr[::-1]

# Input
N = int(input())
arr = list(map(int, input().split()))
print(*reverse_array(arr))



# Input
N = int(input())  # Read the size of the array
arr = list(map(int, input().split()))  # Read the array

# Output the array in reversed order
print(*arr[::-1])

# -----------------------------------------------------------------

# Compare Strings : Compare strings character by character to determine if one is greater, less, or equal.
def compare_strings(s, t):
    s = s.lower()
    t = t.lower()
    if s > t:
        return 1
    elif s < t:
        return -1
    else:
        return 0

# Input
s = input().strip()
t = input().strip()

# Output
print(compare_strings(s, t))


# -----------------------------------------------------------------

# The Final Contest
def final_contest(P, N, M, testers):
    problem_count = [0] * P
    for solved in testers:
        for problem in solved:
            problem_count[problem - 1] += 1

    good_problems = sum(1 for count in problem_count if count >= N // 2)
    return max(0, M - good_problems)

# Input
P, N, M = map(int, input().split())
testers = []
for _ in range(N):
    line = list(map(int, input().split()))
    testers.append(line[1:])
print(final_contest(P, N, M, testers))

# -----------------------------------------------------------------

# Palindromic Handle : Check if the characters can form a palindrome by counting odd frequencies.
def is_palindromic_handle(S):
    freq = {}
    for char in S:
        freq[char] = freq.get(char, 0) + 1

    # odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    # return "Yes" if odd_count <= 1 else "No"
    for i in freq.values():
        if i % 2 != 0:
            oc += 1
            
    if oc <= 1 :
        return "Yes"
    else:
        return "No"

   

# Input
S = input()
print(is_palindromic_handle(S))

# -----------------------------------------------------------------


