# year = int(input('enter year :'))
# if year % 4 == 0 or :
#     print(f"{year} is leap year")
# elif year % 400 == 0:
#     print(f"{year} is leap year")
# elif year % 100 != 0:
#     print(f"{year} is leap year")

# else:
#     print(f"{year} is not leap year")
# year = int(input('enter year :'))
# if (year % 4 == 0) and (year % 100) != 0:
#     print(f"{year} is leap year")

# elif year % 400 == 0:
#     print(f"{year} is leap year")

# else:
#     print(f"{year} is not leap year")

# a = int(input('enter no :'))
# b = int(input('enter no :'))
# print(f"{a} of square  is {a**b}")

# a = int(input('enter no :'))
# b = 1/3
# print(f"{a} of square root is {a**b}")


# a = 5
# b = 10
# a = (a*b) # 50 
# b = a/b #5
# a = a/b
# print(a," ",b) 

# prime number

# num = int(input('enter no :'))
# divide = 0 #inislition from (o)
# for i in range(1,num+1):#(num start with 1 and increment ++)
#     if num % i == 0:#(check every no but divide only one and itself)
#       divide = divide + 1

# if divide > 2:#(only two step to check it is a prime)
#     print(f"{num} is not prime")

# else:
#     print(f"{num} is prime")


# def prime_num(a):
#     prime = 0
#     for i in range(1,a+1):
#         if i % a == 0:
#             prime = prime + 1

#     if prime > 2:
#         print('prime')

#     else:
#         print('not prime')

# prime_num(5)

# find factorial

# num = int(input('enter no :'))
# for i in range(1,num):
#     # print(i*(num-1))
#     f = num*(num-1)
#     print(i*f)
#     num = num - 1

# num = int(input('enter no :'))
# fact = 1
# for i in range(1,num + 1):
#     # print(f"before {fact}")
#     fact = fact * i 
#     # print(f"after fact {fact}")
# print(f"factorial of {num} is {fact} ")

# num = int(input('enter no :'))
# fact = 1
# for i in range(num,0,-1):
#     # print(f"before {fact}")
#     fact = fact * i 
#     # print(f"after fact {fact}")
# print(f"factorial of {num} is {fact} ")



# # multiple table
# n = int(input('enter your num :'))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

a = int(input('enter n0 '))
for i in range(1,11):
    print(f"{a}*{i} = {a*i}")