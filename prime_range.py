num = int(input('enter no :'))
for num in range(1,num+1):
  prime = 0
  for i in range(1,num + 1):
    if num % i == 0:
      prime = prime + 1

  if prime <= 2:
    print(f"{num} is  prime")
   