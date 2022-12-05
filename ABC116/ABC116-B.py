def f(x,cnt):
    cnt = cnt + 1
    if x == 4 or x == 2 or x == 1:
        return print(cnt+3)
    elif x%2 == 0:
        return f(x//2,cnt)
    else:
        return f(3*x + 1,cnt)

s = int(input())
f(s,0)