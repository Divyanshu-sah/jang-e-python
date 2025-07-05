# find  fibonacci series\

# num = int(input('enter no '))
# fab = 0
# for i in range(num):
#     fab = fab + (i - 1) + (i - 2)
#     print(fab)



# factor of num

# num = int(input('enter no :'))
# for i in range(1,num+1):
#     if num % i == 0:
#         print(i,end = " ") 


# sum of natural number

# num = int(input('enter your num :'))
# sum = 0
# for i in range(1,num+1):
#     # print(sum)
#     sum = sum + i
    
# print(sum)

# find sum of natural number with range

# a = int(input('enter no a '))
# b = int(input('enter no b '))
# sum = 0
# for i in range(a,b+1):
#     sum = sum + i

# print(sum)

# find prfect square

# a = int(input('enter no'))
# b = int(a ** 0.5)
# if b*b == a:
#     print('perfect square')

# else:
#     print('not perfect square')

# Check Armstrong Number

num=12

rev_num=0
while(num):
    last_dist=num%10
    rev_num=rev_num*10+last_dist
    num=int(num/10)
    
print(rev_num)

    

