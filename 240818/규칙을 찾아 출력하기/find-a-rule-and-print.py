n = int(input())

star = '* '
total_len = n*2 - 2



if n>1:
  print(star*n)
  for i in range(1, n+1):
    star_len = total_len - len(star*i)
    print(star*i+ ' '*star_len + star)
  
    if n-2 == i:
      print(star*n)
      break;
else:
  print(star*n)