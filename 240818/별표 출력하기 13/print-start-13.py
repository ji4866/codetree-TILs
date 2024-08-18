n = int(input())
star = n
star_2 = 1
for i in range(n, 0, -1):
  print('* '*star)
  star -= 1

  print('* '*star_2)
  star_2 += 1