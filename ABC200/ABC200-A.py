n = int(input())
a = n // 100
if n % 100 != 0:
    a += 1
print(a)