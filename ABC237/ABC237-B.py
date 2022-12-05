h,w = map(int, input().split())
l = []
for i in range(h):
    l.append(list(map(int,input().split())))
l2 = []
for i in range(w):
    for j in range(h):
        l2.append(l[j][i])   
    print(*l2)
    l2 = []