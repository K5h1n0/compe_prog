
def f(x):
    if x == 1:
        return 1
    elif x > 1:
        return 1 + 2*f(x//2)

h = int(input())
print(f(h))