n = int(input())
star = n
gap = 0 # 공백



for i in range(n):
  if gap == 0:
    gap_str = ''
  else:
    gap_str = ' '*gap
  
  for j in range(2):
    for j in range(star, 0, -1):
      print('*', end='')
    
    print(gap_str, end='')

    

  star -= 1
  gap += 2

  print('')