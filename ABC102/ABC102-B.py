n = int(input())
l = list(map(int,input().split()))
maximum = 0
for i in l:
    for j in l:
        if abs(i-j) > maximum:
            maximum = abs(i-j)
print(maximum)