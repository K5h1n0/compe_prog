a,b = input().split()
l= []
l.append(a * int(b))
l.append(b * int(a))
l.sort()
print(l[0])