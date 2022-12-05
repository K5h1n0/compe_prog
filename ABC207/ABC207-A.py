a,b,c = map(int, input().split())
d = a + b
if d < b + c:
    d = b + c
if d < a + c:
    d = a + c
print(d)