n,m,t = map(int,input().split())
time = list(map(int,input().split()))
ans = "Yes"
dic = {}
for i in range(m):
    a,b = map(int,input().split())
    dic[a] = b
for i in range(1,n):
    if 0 >= t:
        ans = "No"
        break
    elif i in dic:
        t += dic[i]
    t -= time[i-1]
    if i == n-1 and t <= 0:
        ans = "No"
        break
print(ans)