a,b = map(int, input().split())
c = b - a + 1
if c < 0:
    print(0)
else:
    print(c)