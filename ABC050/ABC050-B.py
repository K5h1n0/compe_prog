n = int(input())
l_time = list(map(int,input().split()))
m = int(input())
l_drink = []
for i in range(m):
    p,x = map(int,input().split())
    p -= 1
    l_drink.append([p,x])
for i in range(m):
    ans = sum(l_time)
    ans -= l_time[l_drink[i][0]]
    ans += l_drink[i][1]
    print(ans)