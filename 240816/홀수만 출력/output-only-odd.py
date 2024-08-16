a,b = map(int, input().split(' '))

for i in range(b+1):
    if i>=a:
        if i%2 != 0:
            print(i,end=' ')