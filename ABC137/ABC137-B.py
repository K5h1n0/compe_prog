k,x = map(int,input().split())
l = []
for i in range(x-k+1,x+k):
    l.append(i)
print(*l)