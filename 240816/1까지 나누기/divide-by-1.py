n = int(input())
count = 0
i = 1

while (True):
    
  if int(n/i) <=1:
    count += 1
    break;

  n = int(n/i)
  #print(n)
  count += 1
  i += 1


print(count)