n,k,m = map(int,input().split())
l = list(map(int,input().split()))
ans = n * m - sum(l)
if ans <= 0:
    print(0)
else:
    if ans <= k:
        print(ans)
    else:
        print(-1)