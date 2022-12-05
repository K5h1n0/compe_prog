n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(1,n):
    for j in range(i+1,n+1):
        if min(a[i-1],a[j-1]) == i and max(a[i-1],a[j-1])== j and i < j:
            cnt += 1
print(cnt)