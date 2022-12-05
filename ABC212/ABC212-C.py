#二分探索らしい。
n,m = map(int,input().split())
a = list(set(list(map(int,input().split()))))
b = list(set(list(map(int,input().split()))))
a.sort()
b.sort(reverse=True)
l = []
i = 0
while i < len(a):
    j = 0
    flg = 0
    tmp = 99999999999
    while j < len(b) and flg == 0:
        c = abs(a[i]-b[j])
        if tmp <= c:
            flg = 1
        l.append(c)
        tmp = c
        j += 1
    i += 1
print(min(l))