l1,r1,l2,r2 = map(int,input().split())
list1 = [0] * 101
list2 = [0] * 101
for i in range(l1,r1):
    list1[i] = 1
for i in range(l2,r2):
    list2[i] = 1
cnt = 0
for i in range(101):
    if list1[i] == 1 and list2[i] == 1:
        cnt += 1
print(list1)
print(list2)
print(cnt)