num = int(input('enter no :'))
dupl = num
power = len(str(num))
sum = 0
while(num > 0):
    last = num % 10
    sum = last**power + sum
    num = int(num / 10)
# print(sum, dupl)

if sum == dupl:
    print(f"{dupl} is armstrong")

else:
    print(f"{dupl} is not armstrong")


