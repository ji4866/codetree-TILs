n = int(input())
num= n+1

for i in range(1,n+1):
  for j in range(1,num):
    if j==(num-1):
      print(i,'*',j,'=',i*j, end='')
      continue
    
    print(i,'*',j,'=',i*j, end=' / ')
  
  num -= 1
  print('')