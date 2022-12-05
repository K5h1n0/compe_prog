n,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
l.reverse()
if k > n:
    k = n
for i in range(k):
    l[i] = 0
print(sum(l))
