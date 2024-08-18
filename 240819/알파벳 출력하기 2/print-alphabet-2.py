n = int(input())
start_num, last_num = 0, n
gap = 0
num = n

c = 0

str_list = ['A', 'B', 'C', 'D', 'E' , 'F', 'G', 'H','I', 'J','K', 'L','M','N', 'O','P','Q','R','S','T','U','V','W','X','Y','Z']


for i in range(n):
  print(' '*gap, end='')
  
  if last_num>len(str_list):
    for k in range(start_num, len(str_list)):
      print(str_list[k], end= ' ')
    start_num = 0
    last_num -= len(str_list)
  
  for j in range(start_num, last_num):    
    #print(start_num, last_num)
    print(str_list[j], end= ' ')



  num -= 1
  gap += 2
  #print(start_num, last_num)
  start_num =j+1
  last_num += num
  print('')