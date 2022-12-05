p = list(map(int, input().split()))
s = ""
for i in range(len(p)):
    s = s + chr(96+p[i])
print(s)