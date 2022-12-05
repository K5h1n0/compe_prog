from collections import deque

#入力受け取り
row, column = map(int,input().split())
start_y,start_x = map(int,input().split())
goal_y,goal_x = map(int,input().split())
maze = [list(input()) for _ in range(row)]

reached = [[0] * column for __ in range(row)]
print(reached)

y = [-1,0,1,0]
x = [0,1,0,-1]

start_y -= 1
start_x -= 1
goal_y -= 1
goal_x -= 1

print(*maze,sep="\n")
print()
print(*reached,sep="\n")
reached[start_y][start_x] = 1
queue = deque()
cnt = 0
queue.append([start_y,start_x,cnt])

while queue:
    now = queue.popleft()
    now_y,now_x,now_cnt = now[0],now[1],now[2]
    # reached[now_y][now_x] = 1
    for i in range(4):
        search_y = now_y + y[i]
        search_x = now_x + x[i]
        if search_y == goal_y and search_x == goal_x:
            print(now_cnt+1)
            exit()
        elif maze[search_y][search_x] == "." and reached[search_y][search_x] == 0:
            reached[search_y][search_x] = 1
            queue.append([search_y,search_x,now_cnt+1])
    print(*maze,sep="\n")
    print(*reached,sep="\n")
