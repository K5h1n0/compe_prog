r, c = map(int, input().split())
e, f = map(int, input().split())
g, h = map(int, input().split())

if r == 1:
    if c == 1:
        print(e)
    else:
        print(f)
else:
    if c == 1:
        print(g)
    else:
        print(h)
