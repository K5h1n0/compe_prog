def ReLU(a):
    if a >= 0:
        b = a
    if a < 0:
        b = 0
    return b

x = int(input())
print(ReLU(x))