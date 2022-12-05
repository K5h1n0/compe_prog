n = int(input())
l = list(map(int,input().split()))
l2 = [0]*n
for i in range(n):
    if l[i] % 2 == 1:
        l2[i] = -1
    else:
        if l[i] % 3 == 0 or l[i] % 5 == 0:
            l2[i] = -1
if max(l2) == -1:
    print("APPROVED")
else:
    print("DENIED")