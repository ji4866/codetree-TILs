x = int(input())
sum = 0 + x
count = 1
#print('sum = ', sum, 'count = ', count)
while True:
    x = int(input())
    if (x >=20)&(x <30):
      sum += x
      count += 1
    else:
      break;
    #print('sum = ', sum, 'count = ', count)
mean = sum/count
print('%0.2f'%mean)