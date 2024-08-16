n = int(input())
num_list = []

for i in range(n):
    x = int(input())
    num_list.append(x)

for i in range(len(num_list)):
    if (num_list[i]%2 != 0) & (num_list[i]%3 == 0):
        print(num_list[i])