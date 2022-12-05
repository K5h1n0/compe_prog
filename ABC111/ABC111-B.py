n = input()
if n[0] == n[1] == n[2]:
    print(n)
else:
    for i in range(1000):
        n = int(n)
        n += 1
        n = str(n)
        if n[0] == n[1] == n[2]:
            print(n)
            break