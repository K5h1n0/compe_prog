x,y,z = map(int,input().split())
if 0 < y and 0 < x:
    if x < y:
        ans = abs(x)
    elif y < x:
        if 0 < z:
            if z < y:
                ans = abs(x)
            elif y < z:
                ans = -1
        elif z < 0:
            ans = abs(z)*2 + abs(x)
if 0 > y and 0 > x:
    if x > y:
        ans = abs(x)
    elif y > x:
        if 0 > z:
            if z > y:
                ans = abs(x)
            elif y > z:
                ans = -1
        elif z > 0:
            ans = abs(z)*2 + abs(x)
if (y < 0 and 0 < x) or (y > 0 and 0 > x):
    ans = abs(x)
print(ans)


