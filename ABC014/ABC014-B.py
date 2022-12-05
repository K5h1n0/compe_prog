#bit全探索の基礎？
n,x = map(int,input().split())
l = list(map(int,input().split()))
s = list(bin(x)[2:].zfill(len(l)))
s.reverse()
total = 0
for i in range(len(s)):
    if s[i] == "1":
        total += l[i]
print(total)