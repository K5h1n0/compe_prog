n = int(input())
t,a = map(int,input().split())
l = list(map(int,input().split()))
l2 = []
for i in range(n):
    temperture = t*1000 - (l[i] * 6)
    l2.append(abs(temperture - a * 1000))
print(l2.index(min(l2))+1)