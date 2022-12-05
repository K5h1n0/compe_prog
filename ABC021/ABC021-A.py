n = int(input())
l = list(bin(n)[2:])
l.reverse()
l2 = []
for i in range(len(l)):
    if l[i] == "0":
        continue
    s = "1"+"0"*i
    l2.append((int(s,2)))
print(len(l2))
print(*l2,sep="\n")