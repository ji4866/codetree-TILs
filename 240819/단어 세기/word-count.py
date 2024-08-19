s = list(input().split())
dic = {}

while (s != ['end']):
  for item in s:
    count = 0

    if item not in dic:
      count += 1
      dic[item] = count
    else:
      dic[item] += 1
  for keys in dic.keys():
    print(keys, ':',dic[keys])

  s = list(input().split())