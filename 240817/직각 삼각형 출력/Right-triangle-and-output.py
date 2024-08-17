n = int(input())
star = 1
count = 0

while count < n:
  for i in range(star):
    print('*', end='')
  print('')
  star += 2
  count += 1