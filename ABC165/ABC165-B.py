#ACにはなったが、何故か分からない。小数の問題が苦手。
x = int(input())
depo = 100
cnt = 0
while depo < x:
    cnt += 1
    depo = depo + depo//100
print(cnt)