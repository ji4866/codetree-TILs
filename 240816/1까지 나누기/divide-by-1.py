n = int(input())
count = 0
i = 1
num = n

for i in range(1, n+1):
  if int(num/i) <=1:
    count += 1
    break;

  num = int(num/i)
  count += 1
  print(num)
  


print(count)