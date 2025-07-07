num = int(input('enter no :'))
dupl = num
# reverse_num = int(str(num)[::-1]) #slicing and dicing
reverse_num = 0
while(num > 0):
  last_digit = num % 10
  reverse_num = reverse_num*10 + last_digit
  num = int(num / 10)
print(reverse_num)
if dupl == reverse_num:
    print(f"{dupl} is palindrom")

else:
    print(f"{dupl} is not palindrom")

