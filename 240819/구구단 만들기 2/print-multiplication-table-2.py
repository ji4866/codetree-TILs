a, b = map(int, input().split(' '))
mul = 2

for i in range(4):

  for j in range(b, a-1, -1):
    print(j,'*',mul,'=',j*mul, end=' ')
    if j == a:
      break;
    print('/', end=' ')

  print('')
  mul += 2