import math
N,K = map(int, input().split()) 
A = list(map(int, input().split()))
list1 = [list(map(int, input().split())) for l in range(N)]
list2 = []

h = 0
for i in A: #Aの長さだけループ
    for j in list1:
        a = list1[i-1][0] #aはライト持っている人のx
        b = list1[i-1][1] #bはライト持ってる人のy
        c = j[0] #比較対象のx
        d = j[1] #比較対象のy
        e = abs(list1[i-1][0]-j[0])
        f = abs(list1[i-1][1]-j[1])
        g = math.sqrt(e**2 + f**2)
        print(g)
        if h < g: #最大値を探している
            h = g
    list2.append(h)
    h = 0

print(list2)
min = list2[0]
for k in list2:
    if min < k:
        min = k
print("ans" , k)
