a,outlets = map(int,input().split())
cnt = 0
kosuu = 0
if outlets == 1:
    cnt = 0
else:
    while outlets > kosuu + 1:
        kosuu = kosuu + a - 1
        cnt += 1
print(cnt)
