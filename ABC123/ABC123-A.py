# ^^;
l = []
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))
l.append(int(input()))
k = int(input())
l2 = []
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        l2.append(l[j]-l[i])
if max(l2) <= k:
    print("Yay!")
else:
    print(":(")