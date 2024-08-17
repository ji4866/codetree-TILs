n = int(input())
star = 1
gap = n-1


for i in range(n):
  print(' '*gap, end='')
  
  for j in range(star):
    print("*", end=' ')
  
  print('')  
  star += 1
  gap -= 1

  if star == (n+1):
    star = n-1
    gap = 1
    break;

for i in range(n-1, 0, -1):
  print(' '*gap, end='')
  for j in range(star):
    print("*", end=' ')
  print('')  
  star -= 1
  gap += 1