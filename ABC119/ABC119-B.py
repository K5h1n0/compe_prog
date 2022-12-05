n = int(input())
total = 0
for i in range(n):
    a,b = input().split()
    a = float(a)
    if b == "JPY":
        total += a
    else:
        total += a * 380000
print(total)    