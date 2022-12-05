from collections import defaultdict

n,q = map(int,input().split())
ans = []
d = defaultdict(set)
for i in range(q):
    t,a,b = map(int,input().split())
    if t == 1:
        d[b].add(a)
    elif t == 2:
        if a in d[b]:
            d[b].remove(a)
    elif t == 3:
        if a in d[b] and b in d[a]:
            ans.append("Yes")
        else:
            ans.append("No")
print(*ans,sep="\n")