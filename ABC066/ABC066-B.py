s = input()
l = []
for i in range(1,len(s)):
    tmp = s[:i]
    if len(tmp)%2 == 1:
        pass
    else:
        cutpoint = len(tmp)//2
        mae = tmp[:cutpoint]
        ushiro = tmp[cutpoint:]
        if mae == ushiro:
            l.append(cutpoint*2)
print(max(l))