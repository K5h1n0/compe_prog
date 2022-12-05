n = int(input())
m = 21
if n >= 60:
    m = m + 1
    n = n - 60
n = str(n)
s = str(m) +":"+n.zfill(2)
print(s)

