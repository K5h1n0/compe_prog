n = int(input())
s = input()
l = [s[0]]
tmp = s[0]
for i in range(1,n):
    if tmp != s[i]:
        l.append(s[i])
        tmp = s[i]
print(len(l))