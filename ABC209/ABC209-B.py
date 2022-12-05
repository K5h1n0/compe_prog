n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n//2):
   a[(i*2)+1] = a[(i*2)+1] - 1
if sum(a) <= x:
    print("Yes")
else:
    print("No")