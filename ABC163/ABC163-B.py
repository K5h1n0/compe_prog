n,m = map(int,input().split())
l = list(map(int,input().split()))
rem = n - sum(l)
if rem >= 0:
    print(rem)
else:
    print(-1)