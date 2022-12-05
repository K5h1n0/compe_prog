n = int(input())
l = []
for i in range(n):
    l.append(input())
suuji = {"A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"}
for i in range(len(l)):
    s = l[i]
    if s[0] == "H" or s[0] == "D" or s[0] == "C" or s[0] == "S":
        pass
    else:
        print("No")
        exit()
    if s[1] in suuji:
        pass
    else:
        print("No")
        exit()
l2 = len(list(set(l)))
if l2 == len(l):
    print("Yes")
else:
    print("No")