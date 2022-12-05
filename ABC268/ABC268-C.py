n = int(input())
l = list(map(int,input().split()))
l = l + l
l2 = list(range(0,n))
l3 = []
minimum = 9999999999
for i in range(n):
    total = 0
    for j in range(n):
        total += abs(l[j]-(l2[j]+i)%n)
    l3.append(total)
    if total < minimum:
        minimum = total
print(l3)
print(minimum)

"""
#TLE解答
n = int(input())
l = list(map(int,input().split()))
l = l + l
maximum = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if l[i+j] == j or (l[i+j]-1) % n == j or (l[i+j]+1) % n == j:
            cnt += 1
    if cnt > maximum:
        maximum = cnt
print(maximum)
"""