n = int(input())
a = list(map(int,input().split()))
b = list(range(1,n+1))
c = list(zip(a,b))
c.sort()
for i in range(len(c)):
    print(c[i][1],end=" ")
print()