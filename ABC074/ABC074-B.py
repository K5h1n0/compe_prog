n = int(input())
k = int(input())
l = list(map(int,input().split()))
total = 0
for i in range(len(l)):
    tmp = min(abs(0-l[i]),abs(k-l[i]))
    total += tmp * 2
print(total)