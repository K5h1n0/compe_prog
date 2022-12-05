n = int(input())
cnt = 0
ans = "No"
for i in range(n):
    a,b = map(int,input().split())
    if a == b:
        cnt += 1
        if cnt >= 3:
            ans = "Yes"
    else:
        cnt = 0
print(ans)