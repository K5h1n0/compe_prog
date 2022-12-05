a,b,c,d = map(int,input().split())
l = [0]*101
for i in range(a,b):
    l[i] += 1
for i in range(c,d):
    l[i] += 1
print(l.count(2))