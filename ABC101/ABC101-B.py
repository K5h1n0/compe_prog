n = input()
l = []
for i in n:
    l.append(int(i))
if int(n) % sum(l) == 0:
    print("Yes")
else:
    print("No")