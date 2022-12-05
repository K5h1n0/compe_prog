a,b,c = map(int,input().split())
k = int(input())
l = [a,b,c]
for i in range(k):
    index = l.index(max(l))
    l[index] *= 2
print(sum(l))