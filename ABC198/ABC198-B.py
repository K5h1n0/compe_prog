import copy
n = input()
n1 = list(n)
n2 = copy.copy(n1)
n2.reverse()
if n1 == n2:
    print("Yes")
else:
    cnt = 0
    l = []
    for i in range(1,len(n1)):
        if n1[-i] == "0":
            cnt += 1
    n3 = "0"*cnt + n
    n3 = list(n3)
    n4 = copy.copy(n3)
    n4.reverse()
    if n3 == n4:
        print("Yes")
    else:
        print("No")