n,m = map(int,input().split())
l2 = [[] for __ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    l2[a].append(b)
    l2[b].append(a)
cnt = 0
for i in range(1,n+1):
    for j in range(0,len(l2[i])-1):
        for k in range(j+1,len(l2[i])):
            if l2[i][k] in l2[l2[i][j]]:
                cnt += 1
print(cnt//3)