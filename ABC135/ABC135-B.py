n = int(input())
l = list(map(int,input().split()))
cnt = 0
for i in range(1,n+1):
    if i != l[i-1]:
        cnt += 1
if cnt >= 3:
    print("NO")
else:
    print("YES")