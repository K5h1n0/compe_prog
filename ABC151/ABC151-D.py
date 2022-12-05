#解説AC
h,w = map(int,input().split())
maze = []
zahyo = []
for i in range(h): #迷路の用意とともに、"."の座標を記録する。
    tmp = list(input())
    maze.append(tmp)
    for j in range(w):
        if tmp[j] == ".":
            zahyo.append([i,j])

"""
せっかく書いたのに、例えば、
5 5
.....
.###.
..#..
.###.
.....
の時に、不正解になる。
計算量を減らすために最も遠い点の時の距離をmaximumに入れておいて、最も遠いときのみ幅優先という方針だったが。

from collections import deque

h,w = map(int,input().split())
maze = []
zahyo = []
for i in range(h): #迷路の用意とともに、"."の座標を記録する。
    tmp = list(input())
    maze.append(tmp)
    for j in range(w):
        if tmp[j] == ".":
            zahyo.append([i,j])
maximum = 0
for i in range(0,len(zahyo)-1):
    for j in range(i+1,len(zahyo)):
        kyori = abs(zahyo[i][0] - zahyo[j][0]) + abs(zahyo[i][1] - zahyo[j][1])
        if kyori > maximum:
            maximum = kyori

ans = []
y = [-1,0,1,0]
x = [0,1,0,-1]
for i in range(0,len(zahyo)-1):
    for j in range(i+1,len(zahyo)):
        if maximum != abs(zahyo[i][0] - zahyo[j][0]) + abs(zahyo[i][1] - zahyo[j][1]):
            continue
        elif maximum == abs(zahyo[i][0] - zahyo[j][0]) + abs(zahyo[i][1] - zahyo[j][1]):
            #ここから幅優先
            bo = [[False for _ in range(w)] for _ in range(h)]
            queue = deque()
            cnt = 0
            queue.append([zahyo[i][0],zahyo[i][1],cnt])
            bo[zahyo[i][0]][zahyo[i][1]] = True
            while queue:
                now = queue.popleft()
                cnt = now[2] + 1
                for k in range(4):
                    tansakuy = now[0] + y[k]
                    tansakux = now[1] + x[k]
                    if 0 <= tansakuy < h and 0 <= tansakux < w:
                        if tansakuy == zahyo[j][0] and tansakux == zahyo[j][1]:
                            ans.append(cnt)
                            break
                        elif maze[tansakuy][tansakux] == "." and bo[tansakuy][tansakux] == False:
                            bo[tansakuy][tansakux] = True
                            queue.append([tansakuy,tansakux,cnt])
print(max(ans))
"""