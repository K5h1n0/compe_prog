a,b = map(int,input().split())
cnt = 0
for i in range(a,b+1):
    rev = str(i)
    rev = rev[::-1]
    if str(i) == rev:
        cnt += 1
print(cnt)