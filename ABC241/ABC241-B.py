n,m = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0
for i in range(m):
    if b[i] in a:
        a.remove(b[i])
        c += 1
    else:
        print("No")
        break
if c == m:
    print("Yes")