#あー……。　連想配列を使うらしい
n,k = map(int,input().split())
c = list(map(int,input().split()))
l = []
for i in range(k):
    l.append(c[i])
maximum = 0
for i in range(k,n):
    l.pop(0)
    l.append(c[i])
    now = len(set(l))
    if maximum < now:
        maximum = now
        if maximum == k:
            break
print(maximum)