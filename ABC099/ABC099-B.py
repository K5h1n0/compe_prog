a,b = map(int,input().split())
l = []
tmp = 0
sa = b-a
for i in range(1,1000):
    tmp += i
    l.append(tmp)
    if sa == i:
        print(l[i-2]-a)
        exit()