n = int(input())
for i in range(1,n):
    n *= i
    if n > 1000000007:
        n %= 1000000007
print(n)