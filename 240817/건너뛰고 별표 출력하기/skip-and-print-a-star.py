n = int(input())
star = 1

for i in range(n):
  for j in range(star):
    print('*', end='')
  print('\n')
  star += 1

for i in range(n-1, 0, -1):
  for j in range(star-2):
    print('*', end='')
  print('\n')
  star -= 1