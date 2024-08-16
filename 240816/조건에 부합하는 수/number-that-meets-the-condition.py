a = int(input())

for i in range(1, a+1):
    if ~((i%2==0) & (i%4 != 0)) & (int(i/8) %2 != 0) & (i%7 >=4):
        print(i, end= ' ')