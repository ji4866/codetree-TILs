num_list = []

for i in range(5):
    x = int(input())
    num_list.append(x)

for num in num_list:
    if num%3 == 0:
        answer = 1
    else:
        answer = 0
        break;

print(answer)