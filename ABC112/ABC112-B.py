n,t = map(int,input().split())
cost = 9999
l = []
for i in range(n):
    a,b = map(int,input().split())
    if b <= t and cost > a:
        cost = a
if cost == 9999:
    print("TLE")
else:
    print(cost)