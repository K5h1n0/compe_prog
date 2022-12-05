n,m = map(int,input().split())
h = [0] + list(map(int,input().split()))
l = []
for i in range(m):
    l.append(list(map(int,input().split())))
l2 = [[] for _ in range(n+1)]
for i in range(len(l)):
    l2[l[i][0]].append(l[i][1])
    l2[l[i][1]].append(l[i][0])
goodlighthouse = 0
for i in range(1,n+1):
    tmp = 0
    for j in range(len(l2[i])):
        if tmp < h[l2[i][j]]:
            tmp = h[l2[i][j]]
    if tmp < h[i]:
        goodlighthouse += 1
print(goodlighthouse)