h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(input()))
for i in range(h):
    for j in range(w):
        if l[i][j] == ".":
            l[i][j] = 0
x = [-1,0,1,-1,1,-1,0,1]
y = [-1,-1,-1,0,0,1,1,1]
for i in range(h):
    for j in range(w):
        if l[i][j] == "#":
            #print("ここを起点に","i",i,"j",j)
            for k in range(8):
                if 0 <= i+x[k] < h and 0 <= j+y[k] < w:
                    if not (l[i+x[k]][j+y[k]] == "#"):
                        l[i+x[k]][j+y[k]] += 1
for i in range(h):
    print(*l[i],sep="")