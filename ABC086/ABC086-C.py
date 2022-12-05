n = int(input())
l = []
l_time = []
l.append([0,0])
l_time.append(0)
for i in range(n):
    t,x,y = map(int,input().split())
    l_time.append(t)
    l.append([x,y])
ans = "Yes"
for i in range(1,len(l_time)):
    idoujikan = l_time[i] - l_time[i-1]
    kyori = abs(l[i][0] + l[i][1] - (l[i-1][0] + l[i-1][1])) 
    if kyori <= idoujikan and kyori%2 == idoujikan%2:
        pass
    else:
        ans = "No"
        break
print(ans)