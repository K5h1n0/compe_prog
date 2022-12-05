h,w,x,y = map(int, input().split())
l = [input() for _ in range(h)]
x -= 1
y -= 1
cnt = 0
tmp = x
for i in range(x+1): #上
    if l[tmp][y] == ".":
        cnt += 1
    else:
        break
    tmp -= 1
tmp = y
for i in range(y+1): #左
    if l[x][tmp] == ".":
        cnt += 1
    else:
        break
    tmp -= 1
tmp = x
for i in range(h-x): #下
    if l[tmp][y] == ".":
        cnt += 1
    else:
        break
    tmp += 1
tmp = y
for i in range(w-y): #右
    if l[x][tmp] == ".":
        cnt += 1
    else:
        break
    tmp += 1
print(cnt-3)