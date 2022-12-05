n = int(input())
a = list(map(int, input().split()))
l = []
for i in range(1,n+1):
    l.append(i)
a.sort()
if a == l:
    print("Yes")
else:
    print("No")