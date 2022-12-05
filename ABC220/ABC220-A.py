a,b,c = map(int, input().split())
i = 1
d = 0
while d < 1000:
    d = c * i
    if a <= d and d <= b:
        print(d)
        break
    else:
        i = i + 1
    if d >= 1000:
        print(-1)