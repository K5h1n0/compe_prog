from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
bo = [False]*(n+1)
#print(d)
queue = deque()
queue.append([1,0])
bo[1] = True
while queue:
    nowisland = queue.popleft()
    bo[nowisland[0]] = True
    #print(nowisland)
    cnt = nowisland[1]
    cnt += 1
    for i in d[nowisland[0]]:
        if i == n and cnt == 2:
            print("POSSIBLE")
            exit()
        if bo[i] != True:
            queue.append([i,cnt])
print("IMPOSSIBLE")