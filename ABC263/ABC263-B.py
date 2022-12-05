n = int(input())
l = list(map(int,input().split()))
l = [0,0] + l
cnt = 0
while n > 1:
    cnt += 1
    n = l[n]
print(cnt)