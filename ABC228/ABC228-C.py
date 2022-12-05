import copy

n,k = map(int,input().split())
l = []
for i in range(n):
    l.append(sum(list(map(int,input().split()))))
l2 = copy.copy(l)
l2.sort(reverse=True)
kizyun = l2[k-1]
ans = []
for i in range(len(l)):
    now = l[i] + 300
    if now >= kizyun:
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans,sep="\n")