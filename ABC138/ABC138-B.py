n = int(input())
a = list(map(int,input().split()))
summary = 0
for i in range(n):
    summary += 100/a[i]
print(100/summary)