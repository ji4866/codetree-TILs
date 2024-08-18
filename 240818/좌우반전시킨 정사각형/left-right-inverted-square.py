n = int(input())
count = 1

num = n
for i in range(1, n+1):
    for j in range(num, 0, -i):
      print(j, end= ' ')
    num = num+n
    count += 1
    print('')