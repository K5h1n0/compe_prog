a,b = map(int, input().split())  
l = []
m = ""
for i in range(a):
    m=input()
    l.append(list(m))

p, q, r, s = 0,0,0,0
kaisuu = 0

for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == "o":
            if kaisuu == 0:
                p = i
                q = j
                kaisuu += 1
            elif kaisuu == 1:
                r = i
                s = j

c = abs(r - p) + abs(s - q)
print(c)