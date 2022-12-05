n = input()
l = []
for i in range(len(n)-2):
    s = n[i] + n[i+1] + n[i+2]
    l.append(abs(int(s)-753))
print(min(l))