def name(x,i):
    if x >= 26:
        x = x - 26**i
        name(x,i+1)
    else:
        return x

n = int(input())
print(name(n,1))