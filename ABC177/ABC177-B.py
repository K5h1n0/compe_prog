s = list(input())
t = list(input())
l = []
for i in range(0,len(s)-len(t)+1):
    tmp = 0
    for j in range(len(t)):
        if s[i+j] != t[j]:
            tmp += 1
    l.append(tmp)
print(min(l))