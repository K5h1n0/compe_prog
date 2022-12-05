#WA
from collections import deque

h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(input()))
l2 = [[False for _ in range(w)]for _ in range(h)]
x = [0,1,0,-1]
y = [1,0,-1,0]
queue = deque()
ans = 1
cnt = 1
queue.append([1-1,1-1,cnt])
while queue:
    now = queue.popleft()
    #print(now)
    #print(now[0],now[1],cnt)
    l2[now[0]][now[1]] = True
    for i in range(4):
        cnt = now[2]
        #print(now[0]+y[i],now[1]+x[i],now[2])
        if 0 <= now[0]+y[i] < h and 0<= now[1]+x[i] < w:
            if l[now[0]+y[i]][now[1]+x[i]] == "#":
                l2[now[0]+y[i]][now[1]+x[i]] = True
                pass
            elif l[now[0]+y[i]][now[1]+x[i]] == "." and l2[now[0]+y[i]][now[1]+x[i]] == False:
                cnt += 1
                if ans < cnt:
                    ans = cnt
                queue.append([now[0]+y[i],now[1]+x[i],cnt])
print(ans)