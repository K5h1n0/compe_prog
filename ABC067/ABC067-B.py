n,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort(reverse=True)
total = 0
for i in range(k):
    total += l[i]
print(total)