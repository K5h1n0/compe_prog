n,x,y,z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(1,len(a)+1):
    c.append(i)
maru = []
for i in range(x):
    suumax = max(a)
    jyunum = a.index(suumax)
    del a[jyunum]
    del b[jyunum]
    maru.append(c[jyunum])
    del c[jyunum]

for i in range(y):
    eimax = max(b)
    jyunum = b.index(eimax)
    del a[jyunum]
    del b[jyunum]
    maru.append(c[jyunum])
    del c[jyunum]

for i in range(len(a)):
    a[i] = a[i] + b[i]

for i in range(z):
    goumax = max(a)
    jyunum = a.index(goumax)
    del a[jyunum]
    maru.append(c[jyunum])
    del c[jyunum]

maru.sort()
for i in maru:
    print(i)