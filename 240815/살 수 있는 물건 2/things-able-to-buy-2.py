book = 3000
mask = 1000
pen = 500

a = {'book':3000, 'mask':1000, 'pen':500}

n = int(input())

if (n>=book):
    print('book')
elif (n>=mask) & (n<=book):
    print('mask')
elif (n>=pen) & (n<=mask):
    print('pen')
else:
    print('no')