l = list(map(int, input().split())) 
if 0 in l == True:
    a = l.index(0)
else:
    a = 0
b = l[a]
a = l[b]
b = l[a]
print(b)
