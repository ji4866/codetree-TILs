a, b = map(int, input().split(' '))
mul = 1

for i in range(1, b):
    if i%a == 0:
        mul *= i

print(mul)