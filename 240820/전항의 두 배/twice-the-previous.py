a, b = map(int, input().split())
arr = [a, b]

for i in range(2, 10):
  x = arr[i-1] + 2*arr[i-2]
  arr.append(x)

for item in arr:
  print(item, end=' ')