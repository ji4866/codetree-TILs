n = int(input())
line = 1
num = 0
for i in range(n):

  for j in range(n):
    if line %2 == 0:
      num += 2
      print(num, end=' ')
    else:
      num += 1
      print(num, end=' ')

  print('')
  line += 1