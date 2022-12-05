h,w = map(int,input().split())
l = []
s = "#"*(w+2)
l.append(s)
for i in range(h):
    tmp = "#"
    tmp += input()
    tmp += "#"
    l.append(tmp)
l.append(s)
print(*l,sep="\n")