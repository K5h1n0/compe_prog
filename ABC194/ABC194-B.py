import itertools
n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
l = list(itertools.chain.from_iterable(l))
a = []
b = []
for i in range(len(l)):
    if i % 2 == 0:
        a.append(l[i])
    else:
        b.append(l[i])
l = []
for i in range(n):
    for j in range(n):
        if i == j:
            l.append(a[i]+b[j])
        elif a[i] >= b[j]:
            l.append(a[i])
        elif a[i] < b[j]:
            l.append(b[j])
print(min(l))
