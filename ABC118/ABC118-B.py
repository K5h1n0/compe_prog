n,m = map(int,input().split())
l = []
q = [0] * (m+1)
for i in range(n):
    l2 = []
    l2 = list(map(int,input().split()))
    l2.pop(0)
    for j in l2:
        q[j] += 1
cnt = 0
for i in q:
    if i == n:
        cnt += 1
print(cnt)