n = int(input())
lfull = []
l1 = []
l2 = []
l3 = [0]*n
for i in range(n):
    s = input()
    lfull.append(s)
    a,b = s.split()
    l1.append(a)
    l2.append(b)
if len(lfull) != len(list(set(lfull))):
    print("No")
    exit()
else:
    for i in range(len(l1)):
        for j in range(len(l1)):
            if i != j and l1[i] == l1[j]:
                #もし被ったら、
                for k in range(len(l2)):
                    if i != k and l2[i] == l1[k]:
                        print("No")
                        exit()
            if l1[i] in l2 and l1[j] in l1:
                print("No")
                exit()
print("Yes")