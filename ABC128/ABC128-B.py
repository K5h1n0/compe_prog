n = int(input())
l = []
l2 = []
for i in range(1,n+1):
    a,b = input().split()
    l.append(a) 
    l2.append([a,b + " " + str(i)])
l = list(set(l))
l.sort()
for i in l:
    guidebook = []
    for j in range(n):
        if l2[j][0] == i:
            guidebook.append(list(map(int,l2[j][1].split())))
    guidebook.sort(key=lambda x:x[0],reverse=True) 
    for i in guidebook:
        print(i[1])