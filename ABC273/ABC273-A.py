def a(x):
    if x == 0:
        y = 1
        return y
    else:
        y = x-1
        return x * a(y)

n = int(input())
print(a(n))