n,x = map(int, input().split())
l = list(map(int, input().split()))
l2 = []
for ___ in range(len(l)):
    l2.append(0)
i = x - 1
while l2[i] == 0:
    l2[i] = 1
    i = l[i]-1
print(l2.count(1))