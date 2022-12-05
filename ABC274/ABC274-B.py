h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(input())
l2 = [0]*w
for i in range(w):
    for j in range(h):
        if l[j][i] == "#":
            l2[i] += 1
print(*l2)