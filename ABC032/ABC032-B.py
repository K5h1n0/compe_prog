s = input()
k = int(input())
l = []
for i in range(len(s)-k+1):
    tmp = ""
    for j in range(k):
        tmp += s[i+j]
    l.append(tmp)
l = list(set(l))
print(len(l))