n = int(input())
count = 0
i = 1

while (n/i >= 1):
  n = int(n/i)
  count += 1
  i += 1

print(count+1)