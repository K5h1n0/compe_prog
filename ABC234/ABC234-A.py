def kan(a):
    x = a**2 + 2*a +3
    return x
t = int(input())
print(kan(kan(kan(t)+t)+kan(kan(t))))