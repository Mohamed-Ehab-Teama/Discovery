# while
    # while condition:
    #     code
    
# x = 0
# while x <= 12:
#     print (x)
#     x += 1

# x = 1
# while x <= 10:
#     if x == 7:
#         x += 1
#         continue
#     print (x)
#     x += 1


# x = range(0,100,10)
# for i in x :
#     print (i)


num = int(input( 'Enter number: \n' ))
x = range(0,num+1)
sum = 0

for i in x :
    sum = sum + i

print ( 'The sum is ' , sum )