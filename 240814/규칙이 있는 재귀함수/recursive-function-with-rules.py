n = int(input())

t = 2
num_list = [0, 2]

for i in range(n):
  num_list.append(num_list[int(t/2)] + num_list[t-1])

  if t==n:
    break;

  t += 1


for i in range(n):
    print(num_list[i+1], end=' ')
    if i+1 == n:
        break;