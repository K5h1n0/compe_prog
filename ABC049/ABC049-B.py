h,w = map(int,input().split())
l = []
for i in range(h):
    tmp = input()
    l.append(tmp)
    l.append(tmp)
print(*l,sep="\n")