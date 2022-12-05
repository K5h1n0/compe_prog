n,x = map(int,input().split())
l = list(map(int,input().split()))
cnt = 1
summary = 0
for i in range(n):
    summary += l[i]
    if summary <= x:
        cnt += 1
print(cnt)