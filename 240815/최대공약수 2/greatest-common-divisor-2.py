def func1(x):
  x = int(x)
  return x

# 변수 선언
n = int(input())
num_list = []
x = input().split(' ')


a = 1
sum = 0


#### for문
for i in range(len(x)):
  num_list.append(func1(x[i]))

# 두 수 비교
for i in num_list:
  list1 = []
  for k in range(i):
    if i%(k+1) == 0:
      list1.append(k+1)
  #print(i,"의 약수 : ", list1, '(list1)')


  for j in num_list[a:]:
    list2=[]
    for m in range(j):
      if j%(m+1) == 0:
        list2.append(m+1)
    #print(j,"의 약수 : ", list2, '(list2)')
    
    list3=[]
    for item in list1:
      if item in list2:
        list3.append(item)
    #print("공약수 : ", list3)
    sum = sum + max(list3)
    #print("합 : ", sum)

  a += 1


  if a == len(num_list):
    break;

print(sum)