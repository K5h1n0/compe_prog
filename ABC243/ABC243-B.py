n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnta = 0
cntb = 0
for i in range(n):
    if a[i] == b[i]:
        cnta += 1
    elif a[i] in b:
        cntb +=1
print(cnta)
print(cntb)