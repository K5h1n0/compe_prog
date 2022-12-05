s = list(input())
t = list(input())
for i in range(len(s)):
    s[i] = ord(s[i])-97
    t[i] = ord(t[i])-97
a = t[0]-s[0]
for i in range(len(s)):
    t[i] = t[i] - a
    t[i] %= 26
if s == t:
    print("Yes")
else:
    print("No")

"""
def add(x):
    a = x + 1
    a %= 25
    return a

s = list(input())
t = list(input())
abc = "abcdefghijklmnopqrstuvwxyz"
abc = list(abc)

for i in range(len(s)):
    s[i] = abc.index(s[i])
    t[i] = abc.index(t[i])
for i in range(25):
    s1 = map(add, s)
    print(list(s1))
    s = list(s1)

for i in range(25):
    for j in range(len(t)):
        print(i,j)
        if s[j] != t[j]:
            break
"""