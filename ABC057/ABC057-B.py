n,m = map(int,input().split())
lgakusei = []
for i in range(n):
    a,b = map(int,input().split())
    lgakusei.append([a,b])
lpoint = []
for i in range(m):
    a,b = map(int,input().split())
    lpoint.append([a,b])
l3 = []
for i in range(len(lgakusei)):
    l4 = []
    for j in range(len(lpoint)):
        l4.append(abs(lpoint[j][0] - lgakusei[i][0])+abs(lpoint[j][1] - lgakusei[i][1]))
    l3.append(l4.index(min(l4))+1)
print(*l3,sep="\n")