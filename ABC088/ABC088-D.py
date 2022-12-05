from collections import deque

h,w = map(int,input().split())
l = []
cnt_black = 0
for i in range(h):
    tmp = list(input())
    cnt_black += tmp.count("#")
    l.append(tmp)


y = [-1,0,1,0]
x = [0,1,0,-1]

queue = deque()
cnt = 0
cnt += 1
queue.append([0,0,cnt])
bo = [[False for __ in range(w)]for __ in range(h)]
bo[0][0] = True
while queue:
    now = queue.popleft()
    # print(now)
    cnt = now[2]
    cnt += 1
    for i in range(4):
        tansakuy = now[0] + y[i]
        tansakux = now[1] + x[i]
        # print(tansakuy,tansakux)
        if 0 <= tansakuy < h and 0 <= tansakux < w: #そもそも探索箇所がマス目の外なら何もしない。
            if tansakuy == h-1 and tansakux == w-1:
                print(h*w-cnt_black-cnt)
                exit()
            elif l[tansakuy][tansakux] == "." and bo[tansakuy][tansakux] == False:
                bo[tansakuy][tansakux] = True
                # print("append",[tansakuy,tansakux,cnt])
                queue.append([tansakuy,tansakux,cnt])
print(-1)