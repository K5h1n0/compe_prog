s = input()
n = int(input())
l = []
for i in range(5):
    for j in range(5):
        a = s[i]+s[j]
        l.append(a)
print(l[n-1])