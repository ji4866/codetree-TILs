a, b = map(int, input().split())
arr = {}
sum = 0

#print(a,'/',b,'=', end='')

while a>1:
  count = 1
  #print(a,'/',b,'=', end='')
  if a%b not in arr:
    arr[a%b] = count
  else:
    count += 1
    arr[a%b] = count
  a = int(a/b)
  #print(a, '...',a%b)

for keys in arr:
  sum += arr[keys]**2
print(sum)