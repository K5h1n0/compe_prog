n,k = map(int,input().split())
l = list(map(int,input().split()))
l2 = [0]*min(n,k)
for i in range(min(n,k)):
    l.pop(0)
l = l+l2
print(*l)