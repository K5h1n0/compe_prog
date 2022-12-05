n = int(input())
h = list(map(int,input().split()))
cnt = 0
current = 0
for i in range(n):
    if h[i] >= current:
        current = h[i]
        cnt += 1
print(cnt)