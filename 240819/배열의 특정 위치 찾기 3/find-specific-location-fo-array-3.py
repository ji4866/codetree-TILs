arr = list(map(int, input().split()))
index, sum = 0, 0

for item in arr:
    if item == 0:
      break;
    index += 1

#print(index)

for i in range(index-1, index-4, -1):
    sum += arr[i]
print(sum)