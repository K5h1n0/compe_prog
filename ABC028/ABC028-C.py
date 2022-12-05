l = list(map(int,input().split()))
total = []
for i in range(0,3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            total.append(l[i]+l[j]+l[k])
total.sort(reverse=True)
print(total[2])

#解説。頭良い。
#print(max(l[0]+l[3]+l[4],l[1]+l[2]+l[4]))