import math
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))

l2=[]
for i in range(n):
    for j in range(i+1,n): #そういうミスはよくない。
        l2.append(math.sqrt((l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2))
print(max(l2))

"""
#これは配列を比較していくときの基本形として覚えておこう
l = list(map(int, input().split()))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        print("iは:",i, l[i], l[j])
"""
