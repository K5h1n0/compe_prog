#bit全探索の練習
n,m,x = map(int,input().split())
l = []
price = []
for i in range(n):
    l.append(list(map(int,input().split())))
    price.append(l[i].pop(0))
minimum = 99999999
for i in range(1<<n):
    l2 = []
    for j in range(n):
        if 1 & i>>j == 1:
            l2.append(j)
    l2 = tuple(l2)
    l3 = [0]*m
    for j in l2:
        for k in range(m):
            l3[k] += l[j][k]
    judge = 0
    for j in range(m):
        if l3[j] >= x:
            judge += 1
    if judge == m:
        summary = 0
        for j in range(len(l2)):
            summary += price[l2[j]]
        if minimum > summary:
            minimum = summary
if minimum == 99999999:
    print(-1)
else:
    print(minimum)