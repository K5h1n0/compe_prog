l = list(map(int, input().split()))
a = l[1]
l.sort()
if a == l[1]:
    print("Yes")
else:
    print("No")