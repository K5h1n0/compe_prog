n = int(input())
l = list(map(int, input().split()))
saidai = max(l)
l2 = [0]
for i in range(1,saidai+1):
    l2.append(0)
    for j in range(n):
        if l[j] / i - l[j] // i == 0:
            l2[i] += 1
del l2[0:2]
print(l2.index(max(l2))+2)