import itertools
h,w = map(int,input().split())
l = []
for i in range(h):
    l.append(list(map(int,input().split())))
min = min(list(itertools.chain.from_iterable(l)))
cnt = 0
for i in range(h):
    for j in range(w):
        if l[i][j] > min:
            cnt += l[i][j]-min
            l[i][j] = min
print(cnt)