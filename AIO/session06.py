# rows = int( input('Enter Number of rows : ') )

# for i in range(0, rows - 1):
#     for j in range(i):
#         print("*" , end='')
#     print('')


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# l = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k == n:
#                 continue
#             l.append([i,j,k])                
# print(l)

# ls = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
# print(ls)