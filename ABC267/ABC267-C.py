import sys
sys.setrecursionlimit(100000)

def keisan(kekka,ima,teisuu):
    if teisuu == m-1:
        return kekka,ima,teisuu
    else:
        kekka += (teisuu+1) * l[ima+teisuu]
        teisuu += 1
        return keisan(kekka,ima,teisuu)

n,m = map(int,input().split())
l = list(map(int,input().split()))
maximum = 0
print(n-m+1)
for i in range(n-m+1):
    total,b,c = keisan(0,i,0)
    if total > maximum:
        maximum = total
print(maximum)


"""
#テストケースを作成するためのもの。
import random
m = random.randint(1, 2000)
n = random.randint(m, 2000)
x = [random.randint(-200000,200000) for p in range(n)]
print(n,m)
print(*x)

f = open('ABC267sample.txt', 'w')
n = str(n)
f.write(n)
f.write(" ")
m = str(m)
f.write(m)
f.write("\n")
x = str(x)
x = x.replace("[","").replace("]","").replace(",","")
f.write(x)
f.write("\n")
f.close()
"""