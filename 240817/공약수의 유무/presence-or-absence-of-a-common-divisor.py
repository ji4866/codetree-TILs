x = 1920
y = 2880
x_list, y_list, z_list = [], [], []
for i in range(1, x+1):
  if x%i == 0:
    x_list.append(i)

for i in range(1, y+1):
  if y%i == 0:
    y_list.append(i)

#print(x_list)
#print(y_list)

for item in x_list:
  if item in y_list:
    z_list.append(item)
#print(z_list)

a, b = map(int, input().split(' '))

for i in range(a, b+1):
  if i in z_list:
    answer = 1
    break;
  else:
    answer = 0
print(answer)