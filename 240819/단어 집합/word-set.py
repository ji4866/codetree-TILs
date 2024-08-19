s = list(input().split())
ab = []


while (s != ['end']):
  new = []
  for item in s:
    if item not in new:
      new.append(item)
    if item not in ab:
      ab.append(item)
  
  for item in ab:
    print(item, end= ' ')
    
  print('')
  s = list(input().split())