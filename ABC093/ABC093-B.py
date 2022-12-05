a,b,k = map(int,input().split())
if k > b - a:
    print(*list(range(a,b+1)),sep="\n")
else:
    l = []
    for i in range(k):
        l.append(a+i)
        l.append(b-i)
    l = list(set(l))
    l.sort()
    print(*l,sep="\n")