n = int(input())
a = {'book':3000, 'mask':1000}

if (n>=a['book']) & (n>=a['mask']):
    print('book')
elif (n>=a['mask']) & (n<=a['book']):
    print('mask')
else:
    print('no')