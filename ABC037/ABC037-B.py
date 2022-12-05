n,q = map(int,input().split())
l_n = [0]*n
for i in range(q):
    l,r,t = map(int,input().split())
    l -= 1
    r -= 1
    for j in range(l,r+1):
        l_n[j] = t
print(*l_n,sep="\n")