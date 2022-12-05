n = int(input())
if n == 1:
    print(0)
else:
    for i in range(70):
        a = 2 ** i
        if a > n:
            print(i-1)
            break