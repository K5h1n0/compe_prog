n = list(bin(int(input()))[2:])
n.reverse()
l = []
for i in range(len(n)):
    if n[i] == "0":
        continue
    tmp = "0" * i
    tmp = str(n[i]) + tmp
    #print("10shin", int(tmp,2))
    l.append(int(tmp,2))
l = list(set(l))
#print(l)
l3 = []
for i in range(1<<len(l)):
    l2 = []
    for j in range(len(l)):
        if 1 & i>>j == 1:
           l2.append(l[j])
    l3.append(sum(l2))
l3.sort()
for i in l3:
    print(i)