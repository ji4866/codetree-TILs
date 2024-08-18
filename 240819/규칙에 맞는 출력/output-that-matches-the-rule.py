n = int(input())
num = n

#print(n)

for i in range(n):
  for j in range(num, n+1):
    print(j, end=' ')

    
  print('')
  num -= 1