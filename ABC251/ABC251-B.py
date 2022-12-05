n,w = map(int,input().split())
l = list(map(int,input().split()))
cnt = 0
l2 = []
for i in l:
    if i <= w:
        l2.append(i)
for i in range(n-1):
    for j in range(i+1,n):
        if l[i]+l[j] <= w:
            l2.append(l[i]+l[j])
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if l[i] + l[j] + l[k] <= w:
                l2.append( l[i] + l[j] + l[k])
l2 = list(set(l2))
print(len(l2))