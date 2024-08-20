a, b = map(int, input().split())
arr = {}
sum = 0


while a>1:
  count = 1
  #print(a,'/',b,'=', end='')
  remain = a%b

  if remain not in arr:
    arr[remain] = count
  else:
    count = arr[remain]+1
    arr[remain] = count
  a = int(a/b)
  #print(a, '...',remain)

for keys in arr:
  sum += arr[keys]**2
print(sum)