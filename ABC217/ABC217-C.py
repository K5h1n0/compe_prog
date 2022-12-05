n = int(input())
p = list(map(int,input().split()))
l = [0]*n
for i in range(1,n+1):
    l[p[i-1]-1] = i
print(*l)