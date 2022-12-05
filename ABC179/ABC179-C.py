n = int(input())
cnt = 0
for A in range(1,1000000):
    if A > n:
        continue
    for B in range(1,1000000):
        if B > n or A*B > n:
            continue
        elif A * B + (n-A*B) == n and n-A*B != 0:
            cnt += 1
print(cnt)