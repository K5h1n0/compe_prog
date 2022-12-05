l = list(map(int,input().split()))
a = l[0]*l[1]*l[2]
b = l[3]*l[4]*l[5]
print((a-b)%998244353)