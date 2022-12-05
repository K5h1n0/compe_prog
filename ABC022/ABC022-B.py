n = int(input())
l = [0]*n
already = set()
cnt = 0
for i in range(n):
    a = int(input())
    if a not in already:
        already.add(a)
    else:
        cnt += 1
print(cnt)