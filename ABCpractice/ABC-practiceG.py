n = int(input())
list1 = [int(input()) for _ in range(n)]
list1.sort()
a = 0
tmp = 0
for i in range(len(list1)):
    if list1[i] != tmp:
        a += 1
    tmp = list1[i] 
print(a)