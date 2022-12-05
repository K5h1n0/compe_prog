n,m,x = map(int,input().split())
l = list(map(int,input().split()))
tmp = 0
for i in range(x,n+1):
    if i in l:
        tmp += 1
ans = tmp
tmp = 0
for i in range(x,-1,-1):
    if i in l:
        tmp += 1
if ans > tmp:
    ans = tmp
print(ans)