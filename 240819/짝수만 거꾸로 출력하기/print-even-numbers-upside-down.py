n = int(input())
num_list = []
y = []

a = int(input())
num_list.append(a)


# y : num_list 중 짝수 list
for i in range(len(num_list)):
  if num_list[i]%2 == 0:
    y.append(num_list[i])


for j in range(len(y)-1, -1, -1):
  print(y[j], end=' ')