n = int(input())
l = list(map(int,input().split()))
l2 = []
for i in range(1,len(l)):
    l2.append(abs(sum(l[:i])-sum(l[i:])))
print(min(l2))