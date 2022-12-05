s = input()
l = []
for i in range(len(s)):
    s2 = s[0]
    s3 = s[1:]
    s = s3 + s2
    l.append(s)
l.sort()
print(l[0])
print(l[-1])