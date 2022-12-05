n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
    l[i].pop(0)
l2 = []
for i in range(len(l)):
    l2.append(str(l[i]))
l2 = list(set(l2))
print(len(l2))