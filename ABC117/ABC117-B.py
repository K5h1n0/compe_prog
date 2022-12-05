n = int(input())
l = list(map(int,input().split()))
maximum = max(l)
l.pop(l.index(maximum))
if maximum < sum(l):
    print("Yes")
else:
    print("No")