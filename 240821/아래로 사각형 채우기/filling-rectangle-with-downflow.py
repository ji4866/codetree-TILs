n = int(input())
arr = []
num = 1

for i in range(n):
  if i == 0:
    num = 1
  else:
    num = num+n
  arr.append(num)

#print(arr) # [1, 6, 11, 16, 21]


num_list = []
num_list.append(arr) 
#print(num_list) # [[1, 6, 11, 16, 21]]


for i in range(1, n):
  new = []
  
  for item in num_list[i-1]:
    new.append(item+1)

  num_list.append(new)

for item in num_list:
  for item_item in item:
    print(item_item, end=' ')
  print('')