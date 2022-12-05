n = int(input())
cnt = 0
for i in range(1,n+1):
    if i < 10:
        cnt += 1
    if 99 < i and i < 1000:
        cnt += 1
    if 9999 < i and i < 100000:
        cnt += 1
print(cnt)