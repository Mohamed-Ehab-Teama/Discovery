# 1- WaterMelon :
w = int(input())
 
if w > 2 and w % 2 == 0:
    print("YES")
else:
    print("NO")
    
    
# -----------------------------------------------------
# 2- Way Too Long Words
n = int(input())
 
for _ in range(n):
    word = input().strip()
    if len(word) > 10 :
        abbreviation = word[0] + str(len(word) - 2 ) + word[-1]
        print(abbreviation)
    else:
        print(word)
        
        
# -----------------------------------------------------
# 3- Team
n = int(input())
count = 0

for _ in range(n):
    p, v, t = map(int, input().split())
    if p + v + t >= 2:
        count += 1

print( count )


# -----------------------------------------------------
# 4- Bit++
n = int(input())
x = 0
 
for _ in range(n):
    statement = input().strip()
    if "++" in statement:
        x += 1
    elif "--" in statement:
        x -= 1
        
print(x)


# -----------------------------------------------------
# 5- Next Round
n, k = map(int, input().split())
    # Read the list of scores
scores = list(map(int, input().split()))
    # Get the k-th place score
kth_score = scores[k - 1]
    # Count the number of participants who advance
count = 0
for score in scores:
    if score >= kth_score and score > 0:
        count += 1
# Print the result
print(count)


# -----------------------------------------------------
# 6- Domino Piling
M , N = map( int, input().split() )

max_domains = M * N // 2

print(max_domains)


# -----------------------------------------------------
# 7- Beautiful Matrix
for i in range(5):
    row = list( map( int, input().split() ) )
    if 1 in row :
        x, y = i+1 , row.index(1)+1
        
print( abs(x-3) + abs(y-3) )


# -----------------------------------------------------
# 8-Petya and Strings
s1 = input().lower()
s2 = input().lower()

if s1 < s2 :
    print(-1)
elif s1 == s2 :
    print(0)
elif s1 > s2 :
    print(1)
    

# -----------------------------------------------------
# 9-Helpful Maths
s = input()
nums = s.split('+')
nums.sort()
print( '+'.join(nums) )


# -----------------------------------------------------
# 10- Word Capitalization
word = input()
finalWord = word[0].upper() + word[1:]
 
print(finalWord)
