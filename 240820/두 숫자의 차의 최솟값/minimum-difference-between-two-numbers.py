n = int(input())
arr = list(map(int, input().split()))
diff = 0
min = arr[1]-arr[0]

for i in range(len(arr)-1):
  diff = arr[i+1] - arr[i]

  if diff<= min:
    min = diff
    #print(arr[i+1], arr[i], diff)

print(min)