n,m,x,y = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
ans = "War"
for z in range(x+1,y+1):
    if max(l1) < z and z <= min(l2):
        ans = "No War"
print(ans)