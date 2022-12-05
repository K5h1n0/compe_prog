l = list(map(int, input().split()))
l.sort()
if l[0] == l[1] and l[3] == l[4] and(l[2] == l[0] or l[2] == l[4]):
	print("Yes")
else:
	print("No")