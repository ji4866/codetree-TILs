num_list = []
count = 0

for i in range(5):
    x = int(input())
    num_list.append(x)

for i in range(len(num_list)):
    if num_list[i] %2 == 0:
        count += 1
print(count)