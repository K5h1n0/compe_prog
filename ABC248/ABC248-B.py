a,b,k = map(int, input().split())
i = 0
while a < b:
    a = a * k
    i = i + 1
print(i)
