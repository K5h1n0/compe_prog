n,q = map(int,input().split())
l = []
for i in range(n):
    c = list(map(int,input().split()))
    c = c[1:]
    l.append(c)
l2 = []
for i in range(q):
    l2.append(list(map(int,input().split())))
for i in range(q):
    print(l[l2[i][0]-1][l2[i][1]-1])