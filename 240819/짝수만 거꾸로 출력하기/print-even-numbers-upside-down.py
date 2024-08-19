n = int(input())
num_list = []
y = []

a, b, c, d, e, f = map(int, input().split(' '))
num_list.append(a)
num_list.append(b)
num_list.append(c)
num_list.append(d)
num_list.append(e)
num_list.append(f)

for i in range(len(num_list)):
  if num_list[i]%2 == 0:
    y.append(num_list[i])
#print('짝수 리스트 : ', y)


for i in range(len(y)-1, -1, -1):
  print(y[i], end=' ')