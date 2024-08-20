square = []
sum = 0

for i in range(4):
  arr = list(map(int, input().split()))
  square.append(arr)

for i in range(4):
  for j in range(i+1):
    sum += square[i][j]
print(sum)