l = list(map(int, input().split()))
l.sort()
if l[1] - l[0] == l[2] - l[1]:
    print("Yes")
else:
    print("No")