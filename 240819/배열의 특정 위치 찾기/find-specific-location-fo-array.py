arr = list(map(int, input().split()))
count, avg, total = 0,0,0


for i in range(len(arr)):
    if i%2 != 0:
        total += arr[i]
    if (i+1)%3 == 0:
        avg += arr[i]
        count += 1

#print(avg)
avg /= count

print(total, avg)