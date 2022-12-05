n = input()
n2 = list(map(int,n))
if int(n)%sum(n2) == 0:
    print("Yes")
else:
    print("No")