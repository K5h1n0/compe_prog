h,w = map(int,input().split())
s1 = ""
for i in range(h):
    tmp = input()
    s1 += tmp
s2 = ""
for i in range(h):
    tmp = input()
    s2 += tmp
l1 = []
l2 = []
for i in range(w):
    tmp1 = ""
    tmp2 = ""
    for j in range(h):
        tmp1 += s1[i+j*w]
        tmp2 += s2[i+j*w]
    l1.append(tmp1)
    l2.append(tmp2)
l1.sort()
l2.sort()
if l1 == l2:
    print("Yes")
else:
    print("No")

"""
h,w = map(int,input().split())
a = zip(*[input() for _ in range(h)])
b = zip(*[input() for _ in range(h)])
print(list(a))
print(list(b))

if sorted(a) == sorted(b):
  print('Yes')
else:
  print('No')
"""