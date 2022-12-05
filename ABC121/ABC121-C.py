n,m = map(int,input().split())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
l.sort()
cnt = 0
i = 0
