a, b, c = map(int, input().split(' '))

if max(a, b, c) == a:
    if b>= c:
        print(b)
    else:
        print(c)
elif max(a, b, c) == b:
    if(a>= c):
        print(a)
    else:
        print(c)
elif max(a, b, c) == c:
    if(a>= b):
        print(a)
    else:
        print(b)