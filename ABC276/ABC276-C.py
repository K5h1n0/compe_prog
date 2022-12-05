"""
n = int(input())
l = list(map(int,input().split()))
hozon = []
for i in range(len(l)-1):
    kari = l.pop()
    hantei = kari - 1
    print(hantei)
    if hantei in l: #ある時
        print("ある")
        hozon.append(kari)
        pass
    else: #ない時
        if hantei == 0 and n in l: #しかしある時
            print("ある")
            hozon.append(kari)
            print(hozon)
            pass
        print("ない")
        hozon.append(kari)
        print(hozon)
        hozon.sort()
        l.append(hozon[hozon.index(kari)-1])
        hozon.remove(kari-1)
        break
hozon.sort(reverse=True)
for i in range(len(hozon)):
    l.append(hozon[i])
print(l)
"""

"""
n = int(input())
l = list(map(int,input().split()))
l3 = []
for i in range(len(l)-1):
    kari = l.pop()
    tmp = (kari - 1)%n
    if tmp not in l:
        if tmp == 0:
            l3.append(kari)
            continue
        #print("BREAK!")
        #print(kari)
        break
    else:
        l3.append(kari)
        pass
if kari - 1 == 0:
    l.remove(n)
    l.append(n-1)
    l3.append(n)
    l3.remove(n-1)
else:
    l.append(kari-1)
    l3[l3.index(kari-1)] += 1
#print(l)
#print(l3)
l3.sort(reverse=True)
for i in range(len(l3)):
    l.append(l3[i])
print(*l)
"""