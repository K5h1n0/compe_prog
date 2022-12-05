S = input()
l = []
a = 0
if S.isupper() == 0 and S.islower() == 0:
    for i in range(len(S)):
        l.append(S[i])

    for i in range(len(l)):
        for j in range(len(l)-i):
            if i != j+i:
                if l[i] == l[j+i]:
                    a = 1
    if a ==1:
        print("No")
    else:
        print("Yes")
else:
    print("No")
