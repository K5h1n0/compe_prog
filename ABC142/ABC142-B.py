n,k = map(int,input().split())
l = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if l[i] >= k:
        cnt += 1
print(cnt)