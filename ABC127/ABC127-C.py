n,m = map(int,input().split())
minimum = 999999
maximum = 0
for i in range(m):
    left,right = map(int,input().split())
    maximum = max(maximum,left)
    minimum = min(minimum,right)
print(max(0,minimum - maximum + 1))