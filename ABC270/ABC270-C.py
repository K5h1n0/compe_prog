from collections import defaultdict,deque

n,x,y = map(int,input().split())
d = defaultdict(list)
for i in range(n-1):
    u,v = map(int,input().split())
    d[u] = v
    d[v] = u
bo = [False]*(n+1)
print(d)
queue = deque()
queue.append([x])
bo[x] = True
while queue:
    now = queue.popleft()
    print(now)
    print(now[0])
    print(d[now[0]])
    for i in d[now[0]]:
        print(i)
        queue.append(i)
