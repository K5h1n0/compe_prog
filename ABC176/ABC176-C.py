n = int(input())
l = list(map(int,input().split()))
cnt = 0
minimum = 0
for i in range(n):
    if l[i] > minimum:
        minimum = l[i]
    cnt += minimum - l[i]
print(cnt)