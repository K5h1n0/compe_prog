n = int(input())
l = sorted(list(map(int,input().split())))
for i in range(1,len(l)):
    l[i] = (l[i-1] + l[i])/2
print(l[-1])