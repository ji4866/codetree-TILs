n = int(input())
num_list = []
y = []

a, b, c, d = map(int, input().split(' '))
num_list.append(a)
num_list.append(b)
num_list.append(c)
num_list.append(d)


# y : num_list 중 짝수 list
for i in range(len(num_list)):
  if num_list[i]%2 == 0:
    y.append(num_list[i])


for j in range(len(y)-1, -1, -1):
  print(y[j], end=' ')