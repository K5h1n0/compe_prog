n = int(input())
l = list(map(int,input().split()))
l2 = [1]
l3 = [0]
for i in range(len(l)):
    l2.append(l[i]*2)
    l2.append(l[i]*2+1)
    l3.append(l3[l[i]-1]+1)
    l3.append(l3[l[i]-1]+1)
for i in range(len(l3)):
    print(l3[i])
#何でACなのか分からない