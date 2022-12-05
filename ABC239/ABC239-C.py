x1,y1,x2,y2 = map(int,input().split())
l1 = []
l2 = []
x = [-2,-2,-1,-1,1,1,2,2]
y = [1,-1,2,-2,2,-2,1,-1]
for i in range(8):
    l1.append([x1+x[i],y1+y[i]])
    l2.append([x2+x[i],y2+y[i]])
ans = "No"
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            ans = "Yes"
            break
print(ans)